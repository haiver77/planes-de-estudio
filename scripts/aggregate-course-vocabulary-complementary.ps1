param(
    [Parameter(Mandatory = $true)]
    [string]$CoursePath
)

function Get-ComparableVocabularyToken {
    param([string]$RawToken)

    $token = [System.Text.RegularExpressions.Regex]::Replace(
        $RawToken,
        '^[\p{P}\p{S}]+|[\p{P}\p{S}]+$',
        ''
    )
    if (-not $token -or $token -match '^\p{N}+$') {
        return $null
    }

    return $token -replace "(?i)^(?:l|un)['\u2018\u2019]", ''
}

$courseRoot = (Resolve-Path -LiteralPath $CoursePath).Path
$focusPath = Join-Path $courseRoot "course_vocabulary_focus_by_unit.csv"
$unitsRoot = Join-Path $courseRoot "Units"
$outputPath = Join-Path $courseRoot "course_vocabulary_complementary_by_unit.csv"

$focusByUnit = @{}
$unitOrder = [System.Collections.Generic.List[string]]::new()
$knownUnits = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)
$focusLines = [System.IO.File]::ReadAllLines($focusPath, [System.Text.Encoding]::UTF8)

for ($lineNumber = 1; $lineNumber -lt $focusLines.Length; $lineNumber++) {
    $fields = $focusLines[$lineNumber].Split(';', 2)
    if ($fields.Length -ne 2) {
        throw "No se puede leer la fila $($lineNumber + 1) de $focusPath."
    }

    $focusWord = $fields[0].Trim()
    $unitName = $fields[1].Trim()

    if (-not $focusByUnit.ContainsKey($unitName)) {
        $focusByUnit[$unitName] = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)
    }
    foreach ($rawToken in ($focusWord -split '\s+')) {
        $comparableToken = Get-ComparableVocabularyToken -RawToken $rawToken
        if ($comparableToken) {
            [void]$focusByUnit[$unitName].Add($comparableToken)
        }
    }

    if ($knownUnits.Add($unitName)) {
        $unitOrder.Add($unitName)
    }
}

$unitOrder.Sort([System.Comparison[string]]{
    param($left, $right)
    $leftNumber = [int]($left -replace '^Unit_', '')
    $rightNumber = [int]($right -replace '^Unit_', '')
    return $leftNumber.CompareTo($rightNumber)
})

$rows = [System.Collections.Generic.List[string]]::new()
$rows.Add("vocabulary_complementary;unit")

foreach ($unitName in $unitOrder) {
    $lessonsPath = Join-Path (Join-Path $unitsRoot $unitName) "Lessons"
    $lessonFiles = @(Get-ChildItem -LiteralPath $lessonsPath -File -Filter "*.csv" | Sort-Object -Property Name)
    $seenWords = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)

    foreach ($lessonFile in $lessonFiles) {
        $lessonLines = [System.IO.File]::ReadAllLines($lessonFile.FullName, [System.Text.Encoding]::UTF8)
        foreach ($lessonLine in $lessonLines) {
            $fields = $lessonLine.Split(';', 2)
            if ($fields.Length -ne 2) {
                throw "No se puede extraer la segunda columna de $($lessonFile.FullName)."
            }

            foreach ($rawToken in ($fields[1] -split '\s+')) {
                $token = [System.Text.RegularExpressions.Regex]::Replace(
                    $rawToken,
                    '^[\p{P}\p{S}]+|[\p{P}\p{S}]+$',
                    ''
                )
                $comparableToken = Get-ComparableVocabularyToken -RawToken $rawToken
                if (-not $comparableToken) {
                    continue
                }

                if ($focusByUnit[$unitName].Contains($comparableToken)) {
                    continue
                }

                if ($seenWords.Add($token)) {
                    $rows.Add("$token;$unitName")
                }
            }
        }
    }
}

$utf8WithoutBom = New-Object System.Text.UTF8Encoding -ArgumentList $false
[System.IO.File]::WriteAllLines($outputPath, $rows, $utf8WithoutBom)
Write-Output "CSV complementario escrito: $outputPath ($($rows.Count - 1) registros)."
