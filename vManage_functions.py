'''
Example script to perform some vManage REST API calls through functions.
'''

# Import section
import requests
import sys
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Constants definition
VMANAGEIP = '198.18.1.10'
USERNAME = 'admin'
PASSWORD = 'admin'

# Functions definition
def login(vmanageip, username, password):
    # Function to perform a login to vManage
    url = 'https://' + vmanageip + '/j_security_check'
    data = {"j_username" : username, "j_password" : password}
    sess = requests.session()
    response = sess.post(url=url, data=data, verify=False)

    if response.status_code !=  200:
        print('Login Failed')
        sys.exit(0)

    return(sess)

def get(vmanageip, apiurl):
    # Function to perform a GET request to vManage
    url = 'https://' + vmanageip + '/dataservice' + apiurl
    response = sess.get(url=url, verify=False)

    if response.status_code !=  200:
        print('Get request failed\nStatus Code: ' + str(response.status_code))
        sys.exit(0)

    return(response.content)

# Main
    # Login to vmanage
sess = login(VMANAGEIP, USERNAME, PASSWORD)

    # Make an API GET request for feature templates
featureTemplates = json.loads(get(VMANAGEIP, '/template/feature'))
print('\nList of Feature Templates: ')
print('%-60s%-60s' %('Template Name' , 'Template ID'))
for i in range (0,len(featureTemplates["data"])-1):
	print('%-60s%-60s'%(featureTemplates["data"][i]["templateName"] ,featureTemplates["data"][i]["templateId"]))
print('\nTotal number of Templates: ' , len(featureTemplates["data"])-1)

    # Make an API GET request for device list
devices = json.loads(get(VMANAGEIP, '/device'))
print('\nList of devices:')
print('%-18s%-12s%-40s' % ('System IP', 'Site-ID', 'UUID'))
for i in range (0,len(devices["data"])-1):
	if "vedge" in devices["data"][i]["device-type"]:
		print('%-18s%-12s%-40s' % (devices["data"][i]["system-ip"], devices["data"][i]["site-id"], devices["data"][i]["uuid"]))
