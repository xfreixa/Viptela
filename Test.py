
from Viptela import Viptela

VMANAGEIP = '18.194.16.179'
USERNAME = 'admin'
PASSWORD = 'admin'

vManage = Viptela(VMANAGEIP, USERNAME, PASSWORD)
vManage.status()
print(vManage.vManageIP)
