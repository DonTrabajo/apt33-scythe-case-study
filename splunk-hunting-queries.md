## Splunk Queries from APT33 Hunting

### Detect whoami.exe run via rundll32
```
index=main source="WinEventLog:Microsoft-Windows-Sysmon/Operational" Image="*whoami.exe" ParentImage="*rundll32.exe"
| table _time ComputerName ParentImage Image ParentCommandLine CommandLine
```

### Sigma Rule Translated to SPL
```
CommandLine IN ("*whoami*", "*vssadmin*", "*msiexec*", "*mstsc*", "*mshta*", "*netsh*", "*set*", "*arp -*", "*netstat*", "*net *", "*w32tm*", "*schtasks*", "*systeminfo*", "*tasklist*", "*ipconfig*", "*qwinsta*", "*quser*")
```

### Detect PowerShell Get-CimInstance Usage
```
index=main source="WinEventLog:Microsoft-Windows-PowerShell/Operational" Message="*Get-CimInstance*" EventCode=4104
| stats count by Message
```
