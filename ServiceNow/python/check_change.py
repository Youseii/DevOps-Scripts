"""
Parameters need:
- the credetials file json
"""
import requests
import sys
import ServiceNowModule


# Get data about a current open change
def check_for_open_change(token, url_instance, title):

    url = f'https://{url_instance}/api/now/table/change_request?sysparm_query=GOTOshort_descriptionLIKE{title}&sysparm_limit=1'

    headers = {'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer ' + token}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("error check of open change using the title")
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
        exit()
    response = response.json()

    return response


def check_for_open_change_with_number(token, url_instance, change_number):

    url = f'https://{url_instance}/api/now/table/change_request?sysparm_query=GOTOnumberLIKE{change_number}&sysparm_limit=1'

    headers = {'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer ' + token}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("error check of open change using the change's number")
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
        exit()
    response = response.json()

    return response


# state = the number ( 0 = Not registered, 1 registered, ect.. )
def list_all_current_change(token, url_instance, state, assignment_group):

    url = f'https://{url_instance}/api/now/table/change_request?sysparm_query=state={state}&assignment_group={assignment_group}'

    headers = {'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer ' + token}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("error list all current change")
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
        exit()
    response = response.json()

    return response


if __name__ == '__main__':

    url_instance = '' # MODIFY THIS VALUE

    # token, specify the credential file in parameters of the script
    auth_sn = ServiceNowModule.auth_service_now(url_instance, sys.argv[1])
    sntoken = auth_sn['access_token']

    """
    print(check_for_open_change(sntoken, url_instance, "name_of_change")) # EDIT name of the change 
    print(check_for_open_change_with_number(sntoken, url_instance, "number_of_the_change")) # EDIT Number of the change 
    """

    all_list_change = list_all_current_change(sntoken, url_instance, '1', 'put_assignment_group_here') # EDIT group and state here as you want

    for list_change in all_list_change['result']:
        print(list_change['number'])
