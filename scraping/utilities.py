import json
import datetime
import socket
import os



def read_json(filename):
    with open(filename, "r", encoding="utf-8") as json_file:
        return json.load(json_file)


def read_token():
    current_dir = get_script_directory(__file__)
    token_dir = os.path.join(current_dir, "token.txt")
    with open(token_dir) as file:
        return file.read()
    

def write_log(log):
    current_dir = get_script_directory(__file__)
    logs_dir = os.path.join(current_dir, "logs.txt")
    with open(logs_dir, "a", encoding="utf-8") as logs:

        date = datetime.datetime.now()
        year = str(date.year)
        month = str(date.month).zfill(2)
        day = str(date.day).zfill(2)
        hour = str(date.hour).zfill(2)
        minute = str(date.minute).zfill(2)
        second = str(date.second).zfill(2)
        formated_date = f"{day}-{month}-{year} {hour}:{minute}:{second}"

        logs.write(f"[{formated_date}] | {log}\n")

def get_ip():
    try:
        # Crear un socket de tipo AF_INET (IPv4) y SOCK_DGRAM (UDP)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Conectar el socket a un servidor (en este caso, el servidor de Google)
        s.connect(("8.8.8.8", 80))

        # Obtener la dirección IP asignada al socket
        ip_ipv4 = s.getsockname()[0]

        return ip_ipv4
    except Exception:
        return "IP no detectada"
    
def get_script_directory(file):
    return os.path.dirname(os.path.abspath(file))
