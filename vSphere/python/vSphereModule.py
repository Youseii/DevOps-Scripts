import requests
import json


def credentials(credential_file):
    """
    Get the credentials from the json file
    @return: credentials
    @rtype: dict
    """
    with open(credential_file) as json_file:
        data = json.load(json_file)

    return data


def auth_vsphere(vcenter, credential_file):
    auth = credentials(credential_file)['credentials']["vsphere"]

    print("Beginning the auth to vSphere")
    # Authentication to vSphere
    sess = requests.post(f"https://{vcenter}/rest/com/vmware/cis/session", auth=(auth['login'], auth['password']), verify=False, timeout=30)
    session_id = sess.json()['value']

    return session_id
