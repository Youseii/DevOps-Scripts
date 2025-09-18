import sys
import requests
import json
import vSphereModule


def get_vm_id(token_auth, url_instance, vm_name):

    # Get the list of all the vms
    resp = requests.get(f"https://{url_instance}/api/vcenter/vm", headers={"vmware-api-session-id": token_auth})
    list_vms = json.loads(str(resp.text))

    for vm in list_vms:
        try:
            if vm['name'] == vm_name:
                return vm['vm']
        except Exception as e:
            print("Error while trying to get the VM -- get_vm_id function\n")
            print(e)


def get_vm_info(token_auth, url_instance, vm_id):

    resp = requests.get(f"https://{url_instance}/api/vcenter/vm/{vm_id}", headers={"vmware-api-session-id": token_auth})
    info_vm = json.loads(str(resp.text))

    return info_vm


if __name__ == '__main__':

    url_instance = "" # To MODIFY

    credential_file = vSphereModule.auth_vsphere(url_instance, sys.argv[1])

    id_vm = get_vm_id(credential_file, url_instance, "PUT NAME OF VM")
    print(get_vm_info(credential_file, url_instance, id_vm))
