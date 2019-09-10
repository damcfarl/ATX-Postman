#
# cleanup.sh
# Takes the first argument, the raw ACI Inspector output 
# Select the https/payload lines 
# Replace IP with {{apic}} Tenant name with {{tenant}
# Remove leading "url: ", not used in Postman
# Remove "payload", not used in Postman
#

APIC="10.122.143.36"
TENANT="ATX14b"

cat $1 | egrep 'https|payload' | sed s/"url: "//g | sed s/"payload"//g | sed s/"$APIC"/"{{apic}}"/g | sed s/"$TENANT"/"{{tenant}}"/g
