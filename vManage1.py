'''
Library to import to facilitate calls to the vManage API
'''

# Import section
import requests
import sys
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#Class definition
class vManage:
    def __init__(self, vmanageip, username, password):
        self.vmanageip = vmanageip
        self.session = {}
        self.login(self.vmanageip, username, password)

    def login(self, vmanageip, username, password):
        # Function to perform a login to vManage
        url = 'https://' + vmanageip + '/j_security_check'
        data = {"j_username" : username, "j_password" : password}
        sess = requests.session()
        response = sess.post(url=url, data=data, verify=False)
        
        if response.status_code !=  200:
                print('Login Failed')
                sys.exit(0)
        
        self.session[vmanageip] = sess

    def get(self, apiurl):
        # Function to perform a GET request to vManage
        url = 'https://' + self.vmanageip + '/dataservice' + apiurl
        response = self.session[self.vmanageip].get(url, verify=False)
        
        if response.status_code !=  200:
            print('Get request failed\nStatus Code: ' + str(response.status_code))
            sys.exit(0)
        
        return(response.content)
    
    def post(self, apiurl, payload, headers={'Content-Type': 'application/json'}):
        url = 'https://' + self.vmanageip + '/dataservice' + apiurl
        payload = json.dumps(payload)
        response = self.session[self.vmanage_ip].post(url=url, data=payload, headers=headers, verify=False)
        return(response.content)

    def getdevlistform(self):
        devices = json.loads(self.get('/device'))
        devicelist = '\nList of devices:\n'
        for i in range(0,len(devices["data"])):
            if "vedge" in devices["data"][i]["device-type"]:
                devicelist = devicelist + devices["data"][i]["system-ip"].ljust(18)
                devicelist = devicelist + devices["data"][i]["site-id"].ljust(12)
                devicelist = devicelist + devices["data"][i]["uuid"].ljust(18) + '\n'
        return(devicelist)

    def gettempfeatform(self):
        featureTemplates = json.loads(self.get('/template/feature'))
        featureTemplatesList = '\nList of Feature Templates:\n'
        featureTemplatesList = featureTemplatesList + 'Template Name'.ljust(60) + 'Template ID'.ljust(60) + '\n'
        for i in range (0,len(featureTemplates["data"])):
            featureTemplatesList = featureTemplatesList + (featureTemplates["data"][i]["templateName"].ljust(60))
            featureTemplatesList = featureTemplatesList + (featureTemplates["data"][i]["templateId"].ljust(60)) + '\n'
        featureTemplatesList = featureTemplatesList + 'Total number of Templates: ' + str(len(featureTemplates["data"]))
        return(featureTemplatesList)

def main(args):
    if not len(args) == 3:
        print(__doc__)
        return
    vmanageip, username, password = args[0], args[1], args[2]
    myvManage = vManage(vmanageip, username, password)
    #Example request to get devices from the vmanage "url=https://vmanageip/dataservice/device"
    response = myvManage.get('/device')
    print(response)
    
if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
