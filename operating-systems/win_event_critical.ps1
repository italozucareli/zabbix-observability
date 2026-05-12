# Uso no Zabbix Agent Windows
$minutes = 5
$events = Get-EventLog -LogName System -EntryType Error,Critical -After (Get-Date).AddMinutes(-$minutes) -ErrorAction SilentlyContinue
if ($events) { $events.Count } else { 0 }