# oscilloscope/set_vertical.py

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

    #print(f"Frage: {command}")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(TIMEOUT)
        s.connect((OSCILLOSCOPE_IP, OSCILLOSCOPE_PORT))
        s.sendall((command + "\n").encode())
        answer = s.recv(1024).decode(errors="ignore").strip()

    return answer


def check_channel(channel):
    """
    Prüft, ob der Kanal gültig ist.
    """

    if channel not in [1, 2, 3, 4]:
        raise ValueError("Kanal muss 1, 2, 3 oder 4 sein.")


def set_voltage_division(channel=1, value="1V"):
    """
    Setzt die vertikale Skalierung in Volt pro Division.

    Beispiele:
        set_voltage_division(1, "1V")       # 1 V/div
        set_voltage_division(1, "500MV")    # 500 mV/div
        set_voltage_division(2, "2V")       # Kanal 2, 2 V/div
    """

    check_channel(channel)

    value = value.upper().replace(" ", "")

    send_command(f"C{channel}:VDIV {value}")


def get_voltage_division(channel=1):
    """
    Fragt die aktuelle vertikale Skalierung ab.
    """

    check_channel(channel)

    return ask(f"C{channel}:VDIV?")


def set_vertical_offset(channel=1, value="0V"):
    """
    Setzt den vertikalen Offset des Kanals.

    Beispiele:
        set_vertical_offset(1, "0V")       # Offset auf 0 V
        set_vertical_offset(1, "1V")       # Kurve verschieben
        set_vertical_offset(1, "-1V")      # Kurve in Gegenrichtung verschieben
    """

    check_channel(channel)

    value = value.upper().replace(" ", "")

    send_command(f"C{channel}:OFST {value}")


def get_vertical_offset(channel=1):
    """
    Fragt den aktuellen vertikalen Offset ab.
    """

    check_channel(channel)

    return ask(f"C{channel}:OFST?")


def reset_vertical_offset(channel=1):
    """
    Setzt den vertikalen Offset auf 0 V.
    """

    set_vertical_offset(channel, "0V")


def get_error():
    """
    Fragt die Fehlerliste des Oszilloskops ab.
    """

    return ask("SYST:ERR?")