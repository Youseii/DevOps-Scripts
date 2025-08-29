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


def auth_service_now(url_instance, credential_file):
    """
    Authentication to serviceNow
    @return: Authentication token
    @rtype: basestring
    """

    print("Beginning the auth to ServiceNow")
    url = f'https://{url_instance}/oauth_token.do'
    auth = credentials(credential_file)

    x = requests.post(url, data=auth['credentials']["Oauth"])
    data = x.json()
    return data
