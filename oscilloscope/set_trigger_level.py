# oscilloscope/set_trigger_level.py

import socket
from configs.oscilloscope_config import OSCILLOSCOPE_IP, OSCILLOSCOPE_PORT, TIMEOUT


def send_command(command):
    """
    Sendet einen SCPI-Befehl an das Oszilloskop.
    """

    print(f"Sende: {command}")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(TIMEOUT)
        s.connect((OSCILLOSCOPE_IP, OSCILLOSCOPE_PORT))
        s.sendall((command + "\n").encode())


def ask(command):
    """
    Sendet eine SCPI-Abfrage und gibt die Antwort zurück.
    """

    #print(f"Frage: {command}")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(TIMEOUT)
        s.connect((OSCILLOSCOPE_IP, OSCILLOSCOPE_PORT))
        s.sendall((command + "\n").encode())
        answer = s.recv(1024).decode(errors="ignore").strip()

    return answer


def set_trigger_level(channel=1, level="1V"):
    """
    Setzt den Trigger-Level L für den angegebenen Kanal.

    Beispiele:
    set_trigger_level(1, "2.5V")
    set_trigger_level(1, "500MV")
    set_trigger_level(1, "-200MV")
    """

    if channel not in [1, 2, 3, 4]:
        raise ValueError("Kanal muss 1, 2, 3 oder 4 sein.")

    level = level.upper().replace(" ", "")

    send_command(f"C{channel}:TRLV {level}")


def get_trigger_level(channel=1):
    """
    Fragt den Trigger-Level L des angegebenen Kanals ab.
    """

    if channel not in [1, 2, 3, 4]:
        raise ValueError("Kanal muss 1, 2, 3 oder 4 sein.")

    return ask(f"C{channel}:TRLV?")


def get_error():
    """
    Fragt die Fehlerliste des Oszilloskops ab.
    Sehr wichtig zum Testen von SCPI-Befehlen.
    """

    return ask("SYST:ERR?")