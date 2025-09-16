import requests
import json
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


def start_vm(token_auth, url_instance, vm_name):
    vm_id = get_vm_id(token_auth, url_instance, vm_name.upper())

    print(f"Performing on: {vm_name.upper()}")

    resp = requests.post(f"https://{url_instance}/api/vcenter/vm/{vm_id}/power?action=start", headers={"vmware-api-session-id": token_auth})
    resp_code = ''.join([n for n in str(resp) if n.isdigit()])

    if resp_code == '204':
        return 'The vm powered on as intended'
    elif resp_code == '400':
        return 'The vm is already powered on'
    else:
        raise RuntimeError(f'ErrorRest{resp_code}')


if __name__ == '__main__':
    url_instance = "" # To MODIFY

    # sys.argv[1] for the credential file, argv[2] for the instance
    credential_file = vSphereModule.auth_vsphere(url_instance, 'credentials.json')

    #print(get_vm_id(credential_file, url_instance, "PUT THE VM NAME"))
    print(start_vm(credential_file, url_instance, "PUT THE VM NAME"))
