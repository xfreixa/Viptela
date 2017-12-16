'''
Make some calls to the vManage API
'''

# Import section
from vManage import vManage
import json

# Constants definition
VMANAGEIP = '198.18.1.10'
USERNAME = 'admin'
PASSWORD = 'admin'

# Main
myvManage = vManage(VMANAGEIP, USERNAME, PASSWORD)

    # Make an API GET request for feature templates
featureTemplates = json.loads(myvManage.get('/template/feature'))
print('\nList of Feature Templates: ')
print('%-60s%-60s' %('Template Name' , 'Template ID'))
for i in range (0,len(featureTemplates["data"])-1):
	print('%-60s%-60s'%(featureTemplates["data"][i]["templateName"] ,featureTemplates["data"][i]["templateId"]))
print('\nTotal number of Templates: ' , len(featureTemplates["data"])-1)

    # Make an API GET request for device list
devices = json.loads(myvManage.get('/device'))
print('\nList of devices:')
print('%-18s%-12s%-40s' % ('System IP', 'Site-ID', 'UUID'))
for i in range (0,len(devices["data"])-1):
	if "vedge" in devices["data"][i]["device-type"]:
		print('%-18s%-12s%-40s' % (devices["data"][i]["system-ip"], devices["data"][i]["site-id"], devices["data"][i]["uuid"]))
