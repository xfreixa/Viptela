
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

with open('./templates.json', 'r') as f:
    oldTemplates=f.read()

featureTemplates = json.loads(oldTemplates)["data"]

for i in range (0,len(featureTemplates)):
    newTemplate = {}
    if(featureTemplates[i]["factoryDefault"] == False):
        newTemplate["deviceType"] = featureTemplates[i]["deviceType"]
        newTemplate["templateType"] = featureTemplates[i]["templateType"]
        newTemplate["templateMinVersion"] = featureTemplates[i]["templateMinVersion"]
        newTemplate["factoryDefault"] = featureTemplates[i]["factoryDefault"]
        newTemplate["templateName"] = featureTemplates[i]["templateName"]
        newTemplate["templateDescription"] = featureTemplates[i]["templateDescription"]
        newTemplate["templateDefinition"] = json.loads(featureTemplates[i]["templateDefinition"])
        url = 'https://198.18.1.10/dataservice/template/feature'
        response = sess.post(url=url, json=newTemplate, verify=False)
        if response.status_code !=  200:
            print('Create FeatureTemplates Failed. Status code = ' + str(response.status_code))
            sys.exit(0)
