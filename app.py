from flask import Flask, json, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    n = 0

    #il faudrait définir une variable type ID=50 pour le mettre dans chaque url


    headers = {
        'Authorization': "SH_dxvkwNWQIkHGzr9oO1nCNka4tATMlDQ-YDEcPl4ECKOquSNiTsA",
        'Accept': "application/json",
        'API-VERSION': "v1",
    }
    #nombre d'erreur
    url = 'https://wifi-supervision.gotocloud.io/nb_alerts/open_alerts_at_intervals.json?agent_id=50'
    r = requests.get(url, headers=headers)
    response = r.json()
    nbreErreur = response[n]["counts"]
    #nbreErreur = response[n]["counts"]["1"]
    #return str(nbreErreur)

    #nom de l'agent
    url2 = 'https://wifi-supervision.gotocloud.io/agents/names.json'
    r2 = requests.get(url2, headers=headers)
    response2 = r2.json()
    ssid = response2['50']  #ajouter ici la variable type ID


    # current alerte
    url3 = 'https://wifi-supervision.gotocloud.io/nb_alerts/current_alerts.json?agent_id=50'
    r3 = requests.get(url3, headers=headers)
    response3 = r3.json()
    current = response3['current_alerts']  # ajouter ici la variable type ID



    #test
    url30 = 'https://wifi-supervision.gotocloud.io/nb_alerts/open_alerts_at_intervals.json?agent_id=55'
    r30 = requests.get(url30, headers=headers)
    response30 = r30.json()
    nbreErreur30 = response30[n]["timestamp"]
    #y = 161
    #if nbreErreur3 < y:
    #    nbreErreur3= y

    #else:
    #    nbreErreur3= nbreErreur3 + 10000000000000000


    return render_template('index.html', nbreErreur=nbreErreur, ssid=ssid , current=current, nbreErreur30=nbreErreur30)

if __name__ == '__main__':
    app.run(debug=True)

