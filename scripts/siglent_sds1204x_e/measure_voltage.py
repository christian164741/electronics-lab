# measure_voltage.py

import socket
from config import OSCILLOSCOPE_IP, OSCILLOSCOPE_PORT, TIMEOUT


def extract_value(answer):
    """
    Extrahiert den Zahlenwert aus der Antwort des Oszilloskops.
    Beispiel:
    C1:PAVA PKPK,3.160000E+00V  ->  3.16
    """

    value_part = answer.split(",")[1]       # alles nach dem Komma
    value_part = value_part.replace("V", "")
    value_part = value_part.strip()

    return float(value_part)


def measure_voltage(channel=1):
    command = f"C{channel}:PAVA? PKPK"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as osc:
        osc.settimeout(TIMEOUT)
        osc.connect((OSCILLOSCOPE_IP, OSCILLOSCOPE_PORT))

        osc.sendall((command + "\n").encode())

        answer = osc.recv(1024).decode().strip()

    return extract_value(answer)


if __name__ == "__main__":
    spannung = measure_voltage()
    print(f"Spannung: {spannung:.3f} Vpp")