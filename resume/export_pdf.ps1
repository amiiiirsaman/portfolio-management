# Exports resume/Sam_Mahdavian_Resume.docx to PDF with Microsoft Word (no LibreOffice needed).
# Usage: powershell -ExecutionPolicy Bypass -File resume/export_pdf.ps1 [-Out <path.pdf>]
param([string]$Out = "")
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$docx = Join-Path $here "Sam_Mahdavian_Resume.docx"
if ($Out -eq "") { $Out = Join-Path $here "Sam_Mahdavian_Resume.pdf" }
$word = New-Object -ComObject Word.Application
$word.Visible = $false
try {
  $doc = $word.Documents.Open($docx, $false, $true)
  # 17 = wdExportFormatPDF ; OptimizeFor 0 = print ; include doc props + create bookmarks off
  $doc.ExportAsFixedFormat($Out, 17, $false, 0, 0, 0, 0, 0, $true, $true, 0, $true, $true, $false)
  $doc.Close(0)
  Write-Output "wrote $Out"
} finally {
  $word.Quit()
}
