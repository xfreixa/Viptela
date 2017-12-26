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


url = 'https://198.18.1.10/dataservice/template/config/running/ddd801b2-8cbe-4394-abd1-3b71e39886e3'
response = sess.get(url=url, verify=False)

if response.status_code !=  200:
	print('Get Device Running Config Failed. Code: ' + str(response.status_code))
	sys.exit(0)
config = json.loads(response.content)
print(config["config"])


# data = '''
# {
#     "query":
#     {
#       "condition":"AND",
#       "rules":
#       [
#         {
#           "value":["10.4.0.1"],
#           "field":"vdevice_name",
#           "type":"string",
#           "operator":"in"
#         }
#       ]
#     },
#     "aggregation":
#     {
#       "field":
#       [
#         {
#           "property":"interface",
#           "sequence":1
#         }
#       ],
#     "histogram":
#     {
#       "property":"entry_time",
#       "type":"minute",
#       "interval":5,
#       "order":"asc"
#     },
#     "metrics":
#     [
#       {
#         "property":"rx_kbps",
#         "type":"avg"
#       },
#       {
#         "property":"tx_kbps",
#         "type":"avg"
#       }
#     ]
#     }
#   }
# '''
# a = b
# '''
# {
#     "query":
#     {
#       "condition":"AND",
#       "rules":
#       [
#         {
#           "value":["3"],
#           "field":"entry_time",
#           "type":"date",
#           "operator":"last_n_hours"
#         },
#         {
#           "value":["10.4.0.1"],
#           "field":"vdevice_name",
#           "type":"string",
#           "operator":"in"
#         },
#         {
#           "value":
#             [
#               "ge0/0",
#               "ge0/1",
#               "system",
#               "eth0",
#               "ge0/2"
#             ],
#           "field":"interface",
#           "type":"string",
#           "operator":"in"
#         }
#       ]
#     },
#     "sort":
#     [
#       {
#         "field":"entry_time",
#         "type":"date","order":"asc"
#       }
#     ],
#     "aggregation":
#     {
#       "field":
#       [
#         {
#           "property":"interface",
#           "sequence":1
#         }
#       ],
#     "histogram":
#     {
#       "property":"entry_time",
#       "type":"minute",
#       "interval":5,
#       "order":"asc"
#     },
#     "metrics":
#     [
#       {
#         "property":"rx_kbps",
#         "type":"avg"
#       },
#       {
#         "property":"tx_kbps",
#         "type":"avg"
#       }
#     ]
#     }
#   }
#   '''

# url = 'https://198.18.1.10/dataservice/statistics/interface/aggregation?query=' + quote(data)
# response = sess.get(url=url, data=data, verify=False)
# if response.status_code !=  200:
# 	print('Get Interface Statistics Failed')
# 	sys.exit(0)
# print(response.text)

