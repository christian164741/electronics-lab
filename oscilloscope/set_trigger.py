#set_trigger.py

import socket
from configs.oscilloscope_config import OSCILLOSCOPE_IP, OSCILLOSCOPE_PORT, TIMEOUT


def send_command(command):
    """
    Sendet einen SCPI-Befehl an das Oszilloskop.
    """

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(TIMEOUT)
        s.connect((OSCILLOSCOPE_IP, OSCILLOSCOPE_PORT))
        s.sendall((command + "\n").encode())


def ask(command):
    """
    Sendet eine SCPI-Abfrage an das Oszilloskop
    und gibt die Antwort zurück.
    """

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(TIMEOUT)
        s.connect((OSCILLOSCOPE_IP, OSCILLOSCOPE_PORT))
        s.sendall((command + "\n").encode())
        answer = s.recv(1024).decode().strip()

    return answer


def set_trigger_mode(mode="SINGLE"):
    """
    Setzt den Trigger-Modus des Oszilloskops.

    Mögliche Modi:
    AUTO
    NORM
    SINGLE
    STOP
    """

    mode = mode.upper()

    allowed_modes = ["AUTO", "NORM", "SINGLE", "STOP"]

    if mode not in allowed_modes:
        raise ValueError(f"Ungültiger Trigger-Modus: {mode}")

    send_command(f"TRMD {mode}")


def single_trigger():
    """
    Schaltet das Oszilloskop in den Single-Trigger-Modus.
    """

    set_trigger_mode("SINGLE")


def stop_trigger():
    """
    Stoppt die Aufnahme.
    """

    set_trigger_mode("STOP")


def auto_trigger():
    """
    Schaltet zurück auf Auto-Trigger.
    """

    set_trigger_mode("AUTO")


def normal_trigger():
    """
    Schaltet auf normalen Trigger-Modus.
    """

    set_trigger_mode("NORM")


def get_trigger_mode():
    """
    Fragt den aktuellen Trigger-Modus ab.
    """

    return ask("TRMD?")