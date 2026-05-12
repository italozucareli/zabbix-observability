Import-Module WebAdministration
$pools = Get-ChildItem -Path IIS:\AppPools
$data = @()
foreach ($pool in $pools) {
    $data += @{ "{#APPPOOL_NAME}" = $pool.Name; "state" = $pool.State }
}
ConvertTo-Json @{ "data" = $data } -Compress