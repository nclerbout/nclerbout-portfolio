import random
import json
from datetime import datetime, timedelta

# version Mai 2025, créée avec l'aide d'un chatbox IA de type ChatGPT
# === Paramètres généraux ===
now = datetime.now() - timedelta(days=30)     #(pour vérifier le bon fonctionnement de l'alerte Splunk, on enlève le delta de 30 jours et on génère un autre fichier avec la date du jour)
start_time = datetime(now.year, now.month, now.day, 0, 0, 0)
end_time = start_time + timedelta(hours=24)

attacker_ip = "45.227.254.36"
legit_ips = [f"198.51.100.{i}" for i in range(1, 30)]
users = ["admin", "root", "ubuntu", "user1", "developer"]
processes = ["sshd", "login", "systemd-logind", "cron"]
pids = list(range(1000, 9999))
target_hosts = ["192.168.1.5", "192.168.1.8", "192.168.1.22"]

log_entries = []

def generate_event(timestamp, host, process, pid, user, src_ip, port, status, message):
    return {
        "timestamp": timestamp.strftime("%Y-%m-%dT%H:%M:%S"),
        "host": host,
        "process": process,
        "pid": pid,
        "user": user,
        "src_ip": src_ip,
        "port": port,
        "status": status,
        "event": message
    }

# === Génération d'événements légitimes (toutes les 5 à 30 secondes) ===
current_time = start_time
while current_time < end_time:
    host = random.choice(target_hosts)
    ip = random.choice(legit_ips)
    user = random.choice(users)
    port = random.randint(1024, 65535)
    pid = random.choice(pids)
    proc = random.choice(processes)

    if proc == "sshd":
        if random.random() < 0.8:
            status = "Accepted"
        else:
            status = "Failed"
        msg = f"{status} password for {user} from {ip} port {port} ssh2"
        log_entries.append(generate_event(current_time, host, proc, pid, user, ip, port, status, msg))

    elif proc == "login":
        msg = f"pam_unix(login:session): session opened for user {user} by (uid=0)"
        log_entries.append(generate_event(current_time, host, proc, pid, user, None, None, "session_open", msg))

    elif proc == "cron":
        msg = f"pam_unix(cron:session): session closed for user {user}"
        log_entries.append(generate_event(current_time, host, proc, pid, user, None, None, "session_close", msg))

    else:
        msg = f"New session c{random.randint(100,999)} of user {user}."
        log_entries.append(generate_event(current_time, host, proc, pid, user, None, None, "session_start", msg))

    current_time += timedelta(seconds=random.randint(5, 30))

# === Insertion de l'attaque bruteforce entre 14h00 et 14h05 ===
attack_start = start_time + timedelta(hours=14)
attack_attempts = 15 * 5
failed_before_success = 13
interval = timedelta(seconds=2)

current_time = attack_start
for i in range(attack_attempts):
    user = users[i % 2]  # admin, root
    port = random.randint(1024, 65535)
    pid = random.choice(pids)
    status = "Failed" if i < failed_before_success or user != "admin" else "Accepted"
    msg = f"{status} password for {user} from {attacker_ip} port {port} ssh2"
    log_entries.append(generate_event(current_time, "192.168.1.5", "sshd", pid, user, attacker_ip, port, status, msg))
    current_time += interval

# === Tri final des logs ===
log_entries.sort(key=lambda x: x["timestamp"])

# === Écriture dans un fichier JSON (1 log par ligne) ===
with open("ssh_logs.json", "w") as f:
    for entry in log_entries:
        f.write(json.dumps(entry) + "\n")

print("Fichier ssh_logs.json généré.")
