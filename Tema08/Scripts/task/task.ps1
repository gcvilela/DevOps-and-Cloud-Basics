$Action = New-ScheduledTaskAction -Execute 'Powershell.exe' -Argument 'path\Scripts\task\script.ps1'
$Trigger = New-ScheduledTaskTrigger -Daily -At 4pm
$Settings = New-ScheduledTaskSettingsSet
$Task = New-ScheduledTask -Action $Action -Trigger $Trigger -Settings $Settings
Register-ScheduledTask -TaskName "TwitterAPI-Tema08" -InputObject $Task 
