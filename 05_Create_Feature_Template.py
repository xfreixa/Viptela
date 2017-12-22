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

# data = {}
# data["deviceType"] = ["vedge-100-B"]
# data["templateType"] = "vpn-vedge"
# data["templateMinVersion"] = "vpn-vedge"
# data["factoryDefault"] = False
# data["templateName"] = "Tenant1"
# data["templateDescription"] = "Tenant1"
# data["templateDefinition"] = {}
# data["templateDefinition"]["vpn-id"] = {}
# data["templateDefinition"]["vpn-id"]["vipObjectType"] = "object"
# data["templateDefinition"]["vpn-id"]["vipType"] = "constant"
# data["templateDefinition"]["vpn-id"]["vipValue"] = 1
# data["templateDefinition"]["name"] = {}
# data["templateDefinition"]["name"]["vipObjectType"] = "object"
# data["templateDefinition"]["name"]["vipType"] = "constant"
# data["templateDefinition"]["name"]["vipValue"] = "Tenant1"
# data["templateDefinition"]["name"]["vipVariableName"] = "vpn_name"

data = '''
{
    "deviceType": ["vedge-100-B"],
    "templateType": "vpn-vedge",
    "templateMinVersion": "vpn-vedge",
    "templateDefinition" : {
          "vpn-id":
  {
    "vipObjectType":"object",
    "vipType":"constant",
    "vipValue":1
  },
  "name":
  {
    "vipObjectType":"object",
    "vipType":"constant",
    "vipValue":"Tenant1",
    "vipVariableName":"vpn_name"
  },
  "ecmp-hash-key":
  {
    "layer4":
    {
      "vipObjectType":"object",
      "vipType":"ignore",
      "vipValue":"false",
      "vipVariableName":"vpn_layer4"
    }
  },
  "tcp-optimization":
  {
    "vipObjectType":"node-only",
    "vipType":"ignore",
    "vipValue":"false",
    "vipVariableName":"vpn_tcp_optimization"
  },
  "host":
  {
    "vipType":"ignore",
    "vipValue":[],
    "vipObjectType":"tree",
    "vipPrimaryKey":["hostname"]
  },
  "service":
  {
    "vipType":"ignore",
    "vipValue":[],
    "vipObjectType":"tree",
    "vipPrimaryKey":["svc-type"]
  },
  "ip":
  {
    "gre-route":{}
  },
  "ipv6":
  {
  },
  "omp":
  {
    "advertise":
    {
      "vipType":"ignore",
      "vipValue":[],
      "vipObjectType":"tree",
      "vipPrimaryKey":["protocol"]
    }
  }
    },
    "factoryDefault": false,
    "templateName": "Tenant1",
    "templateDescription": "Tenant1"
}
'''

data = json.loads(data)

url = 'https://198.18.1.10/dataservice/template/feature'
response = sess.post(url=url, json=data, verify=False)
if response.status_code !=  200:
	print('Create FeatureTemplates Failed. Status code = ' + str(response.status_code))
	sys.exit(0)
