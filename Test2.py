import requests
import sys
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


url = 'https://198.18.1.10/j_security_check'
data = {"j_username" : "admin", "j_password" : "admin"}
sess = requests.session()
response = sess.post(url=url, data=data, verify=False)

if response.status_code !=  200:
	print('Login Failed')
	sys.exit(0)


url = 'https://198.18.1.10/dataservice/device'
response = sess.get(url=url, data=data, verify=False)
if response.status_code !=  200:
	print('Get Devices List Failed')
	sys.exit(0)

devices = json.loads(response.content)
print('List of devices:')
print('%-18s%-12s%-40s' % ('System IP', 'Site-ID', 'UUID'))
for i in range (0,len(devices["data"])-1):
	if "vedge" in devices["data"][i]["device-type"]:
		print('%-18s%-12s%-40s' % (devices["data"][i]["system-ip"], devices["data"][i]["site-id"], devices["data"][i]["uuid"]))
