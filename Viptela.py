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

    def status(self):
        print(self.vManageIP)
        print(self.username)
        print(self.password)
