import requests
import json
import sys
import vSphereModule


def get_all_datastore(token_auth, url_instance):
    resp = requests.get(f"https://{url_instance}/api/vcenter/datastore", headers={"vmware-api-session-id": token_auth})
    list_datastore = json.loads(str(resp.text))
    # Get the list of all the datastore
    for datastore in list_datastore:
        try:
            print(datastore['name'])

        except Exception as e:
            print("Error while trying to get datastore -- get_all_datastore function\n")
            print(e)


def get_datastore_info(token_auth, url_instance, datastore_name):
    resp = requests.get(f"https://{url_instance}/api/vcenter/datastore", headers={"vmware-api-session-id": token_auth})
    list_datastore = json.loads(str(resp.text))

    for datastore in list_datastore:
        try:
            if datastore['name'] == datastore_name:
                return datastore

        except Exception as e:
            print("Error while trying to get datastore -- get_datastore_info function\n")
            print(e)


if __name__ == '__main__':
    url_instance = ""  # To MODIFY
    credential_file = vSphereModule.auth_vsphere(url_instance, sys.argv[1])

    # Get information about a specific datastore
    print(get_datastore_info(credential_file, url_instance, sys.argv[2]), '\n')

    # List all the datastore that are in the vcenter
    print(get_all_datastore(credential_file, url_instance))
