'''
Make some calls to the vManage API
'''

# Import section
from vManage1 import vManage
import json

# Constants definition
VMANAGEIP = '198.18.1.10'
USERNAME = 'admin'
PASSWORD = 'admin'

# Main
myvManage = vManage(VMANAGEIP, USERNAME, PASSWORD)

    # Make an API GET request for device list and receive it in a formatted string
print(myvManage.getdevlistform())

    # Make an API GET request for feature templates and receive it in a formatted string
print(myvManage.gettempfeatform())

