function gitIP {
(Get-NetIPAddress) IPv4Address | Select-String "192"
}
write-host(getIP)
$IP = getIP
$Date = Get-Date
$Body = "This machine's IP is SIP. User is env:username. Hostname is $. PowerShell Version. Today's date is $DATE"

write-host($Body)
