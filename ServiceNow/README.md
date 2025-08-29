## 🔧 ServiceNow

Les scripts de cette section permettent d’interagir avec l’API ServiceNow afin de récupérer des métriques et informations utiles (par exemple, des CIs).  

### 📂 Configuration requise
Afin de pouvoir exécuter les scripts, il est nécessaire de disposer d’un fichier `credentials.json` contenant les informations d’authentification.  

Créez ce fichier dans votre environnement local avec le format suivant :  

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
