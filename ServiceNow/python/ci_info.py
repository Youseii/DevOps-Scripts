"""
Parameters need:
- the credetials file json
- the ID of the CI
"""

import requests
import sys
import ServiceNowModule


def get_ci_info_by_id(token, url_instance, instance_id):
    """
   Get CI information from its ID
   @param token: ServiceNow API token
   @type token: basestring
   @param instance_id: ID of the CI to retrieve information
   @type instance_id: basestring
   @return: CMDB_CI record
   @rtype: dict
    """
    url = f'https://{url_instance}/api/now/cmdb/instance/cmdb_ci/{instance_id}'
    headers = {'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer ' + token}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("error getInstanceInfo")
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
        exit()
    data = response.json()

    return data['result']['attributes']


if __name__ == '__main__':

    url_instance = '' # MODIFY THIS VALUE by the url of your instance

    # token, specify the credential file in parameters of the script
    auth_sn = ServiceNowModule.auth_service_now(url_instance, sys.argv[1])
    sntoken = auth_sn['access_token']

    print(get_ci_info_by_id(sntoken, url_instance, sys.argv[2]))
