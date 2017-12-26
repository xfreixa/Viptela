import requests
import sys
import json
from urllib.parse import quote
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


url = 'https://198.18.1.10/j_security_check'
data = {"j_username" : "admin", "j_password" : "admin"}
sess = requests.session()
response = sess.post(url=url, data=data, verify=False)

if response.status_code !=  200:
	print('Login Failed')
	sys.exit(0)


url = 'https://198.18.1.10/dataservice/template/config/running/ddd801b2-8cbe-4394-abd1-3b71e39886e3'
response = sess.get(url=url, verify=False)

if response.status_code !=  200:
	print('Get Device Running Config Failed. Code: ' + str(response.status_code))
	sys.exit(0)
    
config = json.loads(response.content)
print(config["config"])