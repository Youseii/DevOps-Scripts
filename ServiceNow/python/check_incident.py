"""
Parameters need:
- the credetials file json
"""
import requests
import sys, json
import ServiceNowModule


def check_for_open_incident(token, url_instance, title):

    url = f'https://{url_instance}/api/now/table/incident?sysparm_query=GOTOshort_descriptionLIKE{title}^incident_state!=7^incident_state!=6'

    headers = {'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer ' + token}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("error check of open incident using the title")
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
        exit()
    response = response.json()

    return response


def get_incident_by_number(token, url_instance, incident_number):

    url = f'https://{url_instance}/api/now/table/incident?sysparm_query=number%3D{incident_number}&sysparm_limit=1'

    headers = {'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer ' + token}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("error check of open incident using the title")
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
        exit()
    response = response.json()

    return response


def open_incident(token, url_instance, support_group_name, service, ci, title, kb="", description=''):

    print("Openning an incident on ServiceNow Gateway")

    url = f'https://{url_instance}/api/now/table/u_monitoring_event'

    headers = {'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer ' + token}

    request_data = {
        'u_action': '',
        'u_comment': str(description)+'\nPlease refer to attached KB article and take actions',
        'u_description': title,
        'u_instruction': kb, # Knowledge base if you have some
        'u_origin': ci, # Configuration Item
        'u_recipient': support_group_name, # Example: INFRA_TEAM
        'u_service': service, # ServiceNow bse
        'u_source': "scripts_api",
    }
    d = json.dumps(request_data)

    response = requests.post(url, headers=headers, data=d)
    response = response.json()

    return response['result']


if __name__ == '__main__':

    url_instance = '' # MODIFY THIS VALUE

    # token, specify the credential file in parameters of the script
    auth_sn = ServiceNowModule.auth_service_now(url_instance, sys.argv[1])
    sntoken = auth_sn['access_token']

    print("========", check_for_open_incident(sntoken, url_instance, "incident_name_title"))
    print("-------------", get_incident_by_number(sntoken, url_instance, "incident_number"))
    
    # Opening an personalize incident
    """open_incident(sntoken, url_instance, "IT_TEAM", "ServiceNow_service", "Linux_VM_1", "Linux_VM_1 is not starting",
                  kb="", description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')"""
