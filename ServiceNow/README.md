## 🔧 ServiceNow

Scripts in this section are using the ServiceNow API to get metrics and data usefull for are automation project. ( for example, CIs, Incidents, Changes, ..).

### 📂 Configuration requise

To execute these scripts, you will necessary need a `credentials.json` file that contains sensitive information ( password, username, client_secret, ..)

Create this file in your local environment using this format:

```json
{
  "credentials": {
    "Oauth": {
      "client_id": "",
      "client_secret": "",
      "grant_type": "password",
      "username": "",
      "password": ""
    }
  }
}
```
Example of how to execute a scripts:

    python3 get_ci_by_name.py credentials.json [name_of_CI]
