# The script will check if a job is present multiple times in a project
import json
import sys
import requests
from collections import Counter
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# Instance of Rundeck ( Can be Rundeck maintenance, Rundeck Prod and Rundeck SAAS )
rdk_instance = "" # To edit


def rundeck_get_api_call(instance, url, data=""):
    headers = {"Content-Type": "application/json",
               "Accept": "application/json",
               "X-Rundeck-Auth-Token": sys.argv[1]}

    r = requests.get(instance+url, headers=headers, params=data)
    content = r.content.decode('utf8')
    data = json.loads(content)
    return data


# List every project in Rundeck
projects = rundeck_get_api_call(rdk_instance, f"/api/45/projects")

# List who contained every jobs' name
l_name = []

for project in projects:
    print(f"\n -------- PROJECT: {project['name']} ------ \n")
    l_name.clear()

    # List every Job in a Rundeck Project
    jobs = rundeck_get_api_call(rdk_instance, f"/api/45/project/{project['name']}/jobs")
    for job in jobs:
        l_name.append(job['name'])

    # Count how many times a name's job is in the list
    occ = Counter(l_name)
    # If the count is superior to 1, then we add it into a list who take only the Jobs who are named multiple times
    multiple_jobs = {nom: count for nom, count in occ.items() if count > 1}

    # Print the Jobs who are named multiple times in a Project
    for nom, count in multiple_jobs.items():
        print(f"Job {nom} are named {count} times in the Project {project['name']}")
