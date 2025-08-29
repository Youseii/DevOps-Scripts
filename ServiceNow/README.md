In the ServiceNow part, you will obviously need credentials access that we are going to put in a json file named 'credentials.json'. It is necessary to have the credentials.json due to the access needed for the API to get metrics of what ServiceNow can offer us. In every scripts, we will have to specify the credentials.json in the arguments.

Create it in your local env using this format:

    {
        "credentials": {
          "Oauth" : {
            "client_id": "",
            "client_secret": "",
            "grant_type": "password",
            "username": "",
            "password": ""  
            }
         }
    }

Example script execution:

    python3 get_ci_by_name.py credentials.json [name_of_CI]
