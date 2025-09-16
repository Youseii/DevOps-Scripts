import requests
import json
import sys
import vSphereModule


def get_vm_id(token_auth, url_instance, vm_name):

    resp = requests.get(f"https://{url_instance}/rest/vcenter/vm", headers={"vmware-api-session-id": token_auth})
    list_vms = json.loads(str(resp.text))
    
    # Get the list of all the VMs
    for vm in list_vms['value']:
        try:
            if vm['name'] == vm_name:
                return vm['vm']
        except Exception as e:
            print("Error while trying to get the VM -- get_vm_id function\n")
            print(e)


def stop_vm(token_auth, url_instance, vm_name):
    vm_id = get_vm_id(token_auth, url_instance, vm_name.upper())

    print(f"Performing on: {vm_name.upper()}")

    resp = requests.post(f"https://{url_instance}/api/vcenter/vm/{vm_id}/power?action=shutdown", headers={"vmware-api-session-id": token_auth})
    resp_code = ''.join([n for n in str(resp) if n.isdigit()])

    if resp_code == '204':
        return 'The vm powered off as intended'
    elif resp_code == '400':
        return 'The vm is already powered off'
    else:
        raise RuntimeError(f'Error Rest {resp_code}')


if __name__ == '__main__':
    url_instance = "" # To MODIFY
    credential_file = vSphereModule.auth_vsphere(url_instance, sys.argv[1])

    #print(get_vm_id(credential_file, url_instance, sys.argv[1]))
    print(stop_vm(credential_file, url_instance, sys.argv[2]))
