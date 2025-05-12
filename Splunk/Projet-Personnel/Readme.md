
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


## Captures d'écran :

