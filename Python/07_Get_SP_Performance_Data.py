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

data = '''
{"query":{"condition":"AND","rules":[{"value":["3"],"field":"entry_time","type":"date","operator":"last_n_hours"}]}}
'''

url = 'https://198.18.1.10/dataservice/statistics/approute/transport/summary/latency?limit=5&query=' + quote(data)
response = sess.get(url=url, data=data, verify=False)

if response.status_code !=  200:
	print('Get SP Performance Data Statistics Failed')
	sys.exit(0)

recordsList = json.loads(response.content)["data"]
print(recordsList)
print('%-18s%-28s%-10s%-10s%-10s' % ('Entry Time', 'Color', 'Latency', 'Jitter', 'Loss'))
for i in range(0, len(recordsList)):
    print('%-18s%-28s%-10s%-10s%-10s' % (recordsList[i]["entry_time"], \
                                        recordsList[i]["color"], \
                                        recordsList[i]["latency"], \
                                        recordsList[i]["jitter"], \
                                        recordsList[i]["loss_percentage"]))


