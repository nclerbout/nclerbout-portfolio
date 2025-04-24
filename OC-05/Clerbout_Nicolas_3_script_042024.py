# Version : 1.0
# Date : avril 2024
# Auteur : Nicolas Clerbout (a partir d'une base fournie par Albertine)
# Description : Automatisation de blocage de multiples adresses IP par un WAF.
# Le WAF attend des requêtes au format json -- donc on utilise json.dumps().
# Affichage du résultat de la requête.

# N.B. : le script a ete écrit et testé avec la version 2.31.0 du package requests

from json import dumps
import requests

liste_adresses_ips = ["52.158.209.219", "5.31.3.31", "54.24.3.85", "55.64.4.15", "118.71.95.25", "115.89.119.166",
                      "193.174.167.74", "7.227.7.145", "48.108.146.81", "87.129.91.47", "46.123.183.243",
                      "170.169.43.40", "77.159.91.107", "219.253.23.64", "204.8.93.157", "238.105.95.237",
                      "223.230.60.83", "102.66.3.221", "10.203.234.137", "95.84.125.255", "209.224.20.64",
                      "147.65.131.19", "113.191.0.101", "23.11.96.242", "191.203.101.233", "127.238.70.112",
                      "236.143.151.139", "43.235.240.197", "101.115.94.82", "200.154.55.33", "248.10.203.170",
                      "226.134.226.229", "174.181.123.25", "238.237.9.63"]
url = "https://learning-secwall.openclassrooms.workers.dev/api/firewall/rules/add"

print("******************************************")
print("Blocage d'adresses IPs sur le WAF")
print("******************************************")

for ip in liste_adresses_ips:
    print(f"Bloquer l'adresse IP {ip}")
    data = {"action": "block", "type": "ip", "value": ip}
    j_data = dumps(data)
    r = requests.post(url, data=j_data)
    if r.status_code < 400:
        print("Adresse bloquée avec succès")
    else:
        print("(", r.status_code, ") Erreur : l'adresse n'a pas pu être bloquée")
    print("---------------------------------------")
