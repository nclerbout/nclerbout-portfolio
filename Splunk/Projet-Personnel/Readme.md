
## Objectifs
1. Utilisation d'un Lab virtuel pour pratiquer l'analyse de logs : 2 VMs sous Linux (VM 1 : Kali Linux ; VM 2 : Ubuntu)
2. Installation de Splunk (sur VM 1) : Utilisation de l'interface web (sur http://localhost:8000), indexation de /var/log
3. Création d'un script Python pour générer un fichier de log basé sur un scénario d'attaque bruteforce sur SSH
   Création d'une règle de détection basique pour repérer les attaques similaires
5. Installation du forwarder universel de Splunk (sur VM 2)
6. Configuration de la collecte des logs de VM 2 sur VM 1


## Compétences :
- **SIEM** : *installation* de Splunk ; collecte de logs ; analyse de logs ; création de règles de détection
- **Scripting** : script Python pour générer des logs ensuite indexés pour requêtes sur le SIEM
  -- N.B. : le script Python a été créé avec l'aide d'un assistant IA ("Le chat" par Mistral)


## Remarques :
Le premier objectif était d'installer de bout en bout Splunk (et le forwarder sur une autre machine) au lieu de simplement utiliser un lab virtuel pré-configuré comme cela avait pu être le cas lors de la formation.
Un autre objectif était de me familiariser avec l'outil Splunk dans ses fonctions basiques (collecte et indexation de logs, recherches, création de règles de détection) puisque mon expérience avec cet outil particulier était limitée à la création d'un dashboard simple jusqu'ici.

Pour l'installation de Splunk et du forwarder universel, voir :
- [https://iritt.medium.com/setting-up-splunk-for-log-management-on-kali-linux-for-your-cybersecurity-home-lab-039fdcff60dd](https://iritt.medium.com/setting-up-splunk-for-log-management-on-kali-linux-for-your-cybersecurity-home-lab-039fdcff60dd)
- [https://iritt.medium.com/setting-up-the-splunk-universal-forwarder-on-kali-linux-for-your-cybersecurity-home-lab-c153d19215dc](https://iritt.medium.com/setting-up-the-splunk-universal-forwarder-on-kali-linux-for-your-cybersecurity-home-lab-c153d19215dc)


## Captures d'écran :

- Lancement du service Splunk sur la VM 1, utilisation de l'interface web et indexaction de /var/log
![lancement service Splunk](/Splunk/Projet-Personnel/img/P11_01.png)
![interface web Splunk](/Splunk/Projet-Personnel/img/P11_02.png)
![indexation /var/log](/Splunk/Projet-Personnel/img/P11_03.png)

- Chargement et indexation d'un fichier de logs (json) simulant une attaque bruteforce sur SSH
- - Création du fichier via script Python + indexation dans Splunk
    ![creation_fichier](/Splunk/Projet-Personnel/img/P11_04.png)
    ![indexation fichier](/Splunk/Projet-Personnel/img/P11_05.png)
  - Recherche dans Splunk pour détecter la tentative de bruteforce
    ![recherche_bruteforce](/Splunk/Projet-Personnel/img/P11_06.png)
  - Création d'une alerte à partir de la requête
    ![creation_alerte](/Splunk/Projet-Personnel/img/P11_07.png)
  - Nouvelle simulation d'attaque et vérification du déclenchement de l'alerte
    ![declenchement_alerte](/Splunk/Projet-Personnel/img/P11_08.png)

(à venir)
