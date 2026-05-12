# Retorna 1 se reboot pendente, 0 se não
$needsReboot = 0
$reg1 = Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Component Based Servicing\RebootPending" -ErrorAction SilentlyContinue
$reg2 = Get-ItemProperty "HKLM:\SYSTEM\CurrentControlSet\Control\Session Manager" -Name "PendingFileRenameOperations" -ErrorAction SilentlyContinue
if ($reg1 -or $reg2) { $needsReboot = 1 }
Write-Output $needsReboot