"""

"""

import requests
import sys
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class Viptela:
    def __init__(self, vManageIP, username, password):
        self.vManageIP = vManageIP
        self.username = username
        self.password = password
        self.session = {}

    def status(self):
        print(self.vManageIP)
        print(self.username)
        print(self.password)

    def login(self):

        url = 'https://' + self.vManageIP + '/j_security_check'
        data = {'j_username' : self.username, 'j_password' : self.password}
        sess = requests.session()
        response = sess.post(url=url, data=data, verify=False)

        if response.status_code !=  in response.content:
            print('Login Failed')
            sys.exit(0)

        self.session[vManageIP] = sess


    def getDevices(self):
        url = "https://%s:8443/dataservice/%s"%(self.vmanage_ip, mount_point)
        print url
        response = self.session[self.vmanage_ip].get(url, verify=False)
        data = response.content
        return data
