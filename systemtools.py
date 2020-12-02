import os
from telnetlib import Telnet
import socket
from dns import resolver


def check_ping(host, num_of_packets: int):
    response = os.system(f'ping {host} -n {num_of_packets}')
    if response == 0:
        return True
    else:
        return False


def check_port_status(dst, port: int):
    try :
        Telnet(dst, port)
        return "Open"
    except:
        return "Blocked"


def get_machine_ip(host):
    try:
        ip = socket.gethostbyname(host)
        return ip
    except:
        return "NotFound"


