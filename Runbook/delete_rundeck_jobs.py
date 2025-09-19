# The script is used to delete rundeck job in every project, it will detect jobs that has been detected having a reference about the arguments we put.
import json
import sys, ssl
import requests
import urllib3.poolmanager
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

instance_name = "" # TO EDIT


class CustomHttpAdapter(requests.adapters.HTTPAdapter):
    def __init__(self, ssl_context=None, **kwargs):
        self.ssl_context = ssl_context
        super().__init__(**kwargs)

    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = urllib3.poolmanager.PoolManager(num_pools=connections, maxsize=maxsize, block=block, ssl_context=self.ssl_context)


def get_legacy_session():
    ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    ctx.options |= ssl.PROTOCOL_TLSv1_2
    session = requests.session()
    session.mount('https://', CustomHttpAdapter(ctx))

    return session


def get_api_call(instance, url, data=""):
    headers = {"Content-Type": "application/json",
               "Accept": "application/json",
               "X-Rundeck-Auth-Token": sys.argv[1]}

    r = get_legacy_session().get(instance+url, headers=headers, params=data, verify=False)
    content = r.content.decode('utf8')
    data = json.loads(content)
    return data


def delete_api_call(instance, url, data=""):
    headers = {"Content-Type": "application/json",
               "Accept": "application/json",
               "X-Rundeck-Auth-Token": sys.argv[1]}

    r = get_legacy_session().delete(instance+url, headers=headers, params=data, verify=False)
    return r

# List every project in Rundeck
projects = get_api_call(instance_name, f"/api/45/projects")

for project in projects:
    print(f"\n -------- PROJECT: {project['name']} ------ \n")

    # List the complete definition of every job
    jobs = get_api_call(instance_name, f"/api/45/project/{project['name']}/jobs/export")
    for job in jobs:
        s = []
        for key, value in job.items():
            if sys.argv[2] in str(value):
                s.append(key)
            else:
                pass

        if not s:
            pass
        else:
            for opt in s:
                if opt == 'options':
                    pass
                else:
                    print(f"{sys.argv[2]} has been detected in {s} for the job {job['name']}")
                    # Delete jobs
                    #delete_api_call(instance_name, f"/api/45/job/{job['id']}")
                    #print(f"----> {job['name']} has been deleted\n")
