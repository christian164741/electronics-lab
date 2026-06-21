# auto_setup.py
# Run auto setup on Siglent SDS1204X-E via LAN/SCPI

import socket
import time

IP = "192.168.2.117"
PORT = 5025


def send_scpi(command, read_response=False):
    """Send one SCPI command to the oscilloscope. Optionally read response."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(5)
        sock.connect((IP, PORT))
        sock.sendall((command + "\n").encode())

        if read_response:
            response = sock.recv(4096).decode(errors="ignore").strip()
            return response

        return None


if __name__ == "__main__":
    print("Running auto setup on oscilloscope...")

    send_scpi("ASET")

    # Auto setup needs a moment
    time.sleep(3)

    print("Auto setup command sent.")