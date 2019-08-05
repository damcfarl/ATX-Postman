#!/usr/local/bin/python3.7

import requests
import json

#python3
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#python2
#from requests.packages.urllib3.exceptions import InsecureRequestWarning
#requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

apic = '10.122.143.36'
tenant = 'ATX14-test5'
aci_user = 'apic:ACI_TOA\\damcfarl'
aci_pwd = 'cisco!123'

headers = {'content-type': "application/json"}

s = (requests.Session())
print('\n')

# Login to ACI fabric
print("login to ACI fabric: " " "+ apic + "")
url = 'https://' + apic + '/api/mo/aaaLogin.json'
payload = {'aaaUser': {'attributes': {'name': aci_user, 'pwd': aci_pwd}}}
r = s.post(url, data=json.dumps(payload), verify=False)
cookies = r.cookies
print(r.status_code)
print('\n')

url = "https://" + apic + "/api/node/mo/uni/tn-" + tenant + ".json"
payload = \
    {"fvTenant": {
                "attributes": {
                    "dn": "uni/tn-" + tenant + "",
                    "name": "" + tenant + "",
                    "rn": "tn-" + tenant + "",
                    "status": "created"
                    },
                "children": []
                }
    }
r = s.post(url, data=json.dumps(payload), verify=False)
print(payload)
print(r.text)
print(r.status_code)
print('\n')
