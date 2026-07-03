# oscilloscope/set_trigger_slope.py

import socket
from configs.oscilloscope_config import OSCILLOSCOPE_IP, OSCILLOSCOPE_PORT, TIMEOUT


def send_command(command):
    """
    Sendet einen SCPI-Befehl an das Oszilloskop.
    """

    #print(f"Sende: {command}")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(TIMEOUT)
        s.connect((OSCILLOSCOPE_IP, OSCILLOSCOPE_PORT))
        s.sendall((command + "\n").encode())


def ask(command):
    """
    Sendet eine SCPI-Abfrage und gibt die Antwort zurück.
    """

   # print(f"Frage: {command}")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(TIMEOUT)
        s.connect((OSCILLOSCOPE_IP, OSCILLOSCOPE_PORT))
        s.sendall((command + "\n").encode())
        answer = s.recv(1024).decode(errors="ignore").strip()

    return answer


def set_trigger_slope(channel=1, slope="POS"):
    """
    Setzt die Trigger-Flanke.

    channel: Kanalnummer 1 bis 4

    slope:
        "POS"  = aufsteigende Flanke
        "NEG"  = absteigende Flanke

    Beispiele:
        set_trigger_slope(1, "POS")   # CH1 aufsteigend
        set_trigger_slope(1, "NEG")   # CH1 absteigend
    """

    if channel not in [1, 2, 3, 4]:
        raise ValueError("Kanal muss 1, 2, 3 oder 4 sein.")

    slope = slope.upper()

    if slope not in ["POS", "NEG"]:
        raise ValueError("Slope muss POS oder NEG sein.")

    send_command(f"C{channel}:TRSL {slope}")


def get_trigger_slope(channel=1):
    """
    Fragt die aktuelle Trigger-Flanke ab.
    """

    if channel not in [1, 2, 3, 4]:
        raise ValueError("Kanal muss 1, 2, 3 oder 4 sein.")

    return ask(f"C{channel}:TRSL?")


def get_error():
    """
    Fragt die Fehlerliste des Oszilloskops ab.
    """

    return ask("SYST:ERR?")