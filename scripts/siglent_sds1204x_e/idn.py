# idn.py
# Simple connection test for Siglent SDS1204X-E via LAN/SCPI

import socket

IP = "192.168.2.117"
PORT = 5025

def send_scpi(command: str) -> str:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(3)
        sock.connect((IP, PORT))
        sock.sendall((command + "\n").encode())
        response = sock.recv(4096).decode().strip()
        return response

if __name__ == "__main__":
    response = send_scpi("*IDN?")
    print("Device response:")
    print(response)