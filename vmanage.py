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
