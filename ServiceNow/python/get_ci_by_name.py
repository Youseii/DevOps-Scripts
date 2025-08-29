"""
Parameters need:
- the credetials file json
- the name of the CI
"""

import requests
import sys, json
import ServiceNowModule


def get_ci_info_by_name(token, url_instance, ci_name):
    """
    Get CI information with a search based on the name.
    Return a maximum of 1 entry
    @param token: ServiceNow API token
    @type token: basestring
    @param name: Name of the CI to look for
    @type name: basestring
    @return: CMDB_CI record
    @rtype: dict
    """

    url = f'https://{url_instance}/api/now/table/cmdb_ci?sysparm_query=GOTOnameLIKE{ci_name}&sysparm_limit=15'

    headers = {'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer ' + token}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Error getCiRecord")
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
        return 0

    responsejson = json.loads(response.text)

    return responsejson


if __name__ == '__main__':

    url_instance = '' # MODIFY THIS VALUE

    # token, specify the credential file in parameters of the script
    auth_sn = ServiceNowModule.auth_service_now(url_instance, sys.argv[1])
    sntoken = auth_sn['access_token']

    print(get_ci_info_by_name(sntoken, url_instance, sys.argv[2]))
