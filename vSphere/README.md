## 🖥️ VMware vSphere

Scripts in this section are using the VMware API to get metrics and data usefull for are automation project. ( for example, start/stop, Backup, ..)

### 📂 Configuration requise

For the python environment, I'm using `python3.12` using mostly `requests`, `sys`, `json` packages.

To execute these scripts, you will necessary need the `credentials.json` file that contains sensitive information ( password, username, client_secret, ..), it is mandatory to have it a specify it it in arguments of the script's call. 

Create this file in your local environment using this format:

```json
{
  "credentials": {
    "vsphere": {
      "login": "",
      "password": ""
    }
  }
}
```
Example of how to execute a script:

    python3 start_vm.py credentials.json [name_of_VM]

