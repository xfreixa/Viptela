    """

    """

    import requests
    import sys
    import json
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


    url = 'https://18.194.16.179/j_security_check'
    data = {"j_username" : "admin", "j_password" : "admin""}
    sess = requests.session()
    response = sess.post(url=url, data=data, verify=False)

    if response.status_code !=  200:
        print('Login Failed')
        sys.exit(0)


    url = 'https://18.194.16.179/dataservice/device'
    response = sess.get(url=url, data=data, verify=False)
    if response.status_code !=  200:
        print('Get Devices List Failed')
        sys.exit(0)
    print(response.text)
