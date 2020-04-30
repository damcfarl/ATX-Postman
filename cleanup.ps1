#
# cleanup.ps1 damcfarl
# Windows PowerShell
# Takes the first argument, the raw ACI Inspector output 
# Select the https/payload lines 
# Replace IP with {{apic}} Tenant name with {{tenant}
# add these variables to the Postman environement file
# Remove leading "url: ", not used in Postman
# Remove "payload", not used in Postman
#
# PS C:> .\cleanup.ps1 .\api_inspector.txt
#



$filename=$args[0]
$APIC="10.122.143.36"
#$APIC
$TENANT="ATX14b"
#$TENANT

#Get-Content $filename


(((((Get-Content $filename | Select-String -pattern https,payload) -replace 'url: ') -replace 'payload') -replace $TENANT,'{{tenant}}') -replace $APIC,'{{apic}}')

