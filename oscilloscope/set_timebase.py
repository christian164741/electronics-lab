# oscilloscope/set_timebase.py

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

    #print("Befehl gesendet")


def ask(command):
    """
    Sendet eine SCPI-Abfrage und gibt die Antwort zurück.
    """

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(TIMEOUT)
        s.connect((OSCILLOSCOPE_IP, OSCILLOSCOPE_PORT))
        s.sendall((command + "\n").encode())
        answer = s.recv(1024).decode().strip()

    return answer


def set_time_division(value):
    """
    Setzt die horizontale Zeitbasis.

    Beispiele:
    set_time_division("1MS")      # 1 ms/div
    set_time_division("100US")    # 100 µs/div
    set_time_division("500MS")    # 500 ms/div
    set_time_division("1S")       # 1 s/div
    """

    value = value.upper()
    send_command(f"TDIV {value}")


def get_time_division():
    """
    Fragt die aktuelle Zeitbasis ab.
    """

    return ask("TDIV?")

def set_display_delay(value):

    """

    Setzt den Delay so, wie er am Oszilloskop angezeigt werden soll.

    Das Vorzeichen wird intern umgedreht.

    """

    value = value.upper()

    if value.startswith("-"):

        scpi_value = value[1:]

    elif value.startswith("0"):

        scpi_value = value

    else:

        scpi_value = "-" + value

    send_command(f"TRDL {scpi_value}")
def set_trigger_delay(value):
    """
    Setzt den horizontalen Trigger-Delay.

    Beispiele:
    set_trigger_delay("0S")        # Trigger in Bildschirmmitte
    set_trigger_delay("-200MS")    # Ereignis weiter links/rechts je nach Gerätedarstellung
    set_trigger_delay("100MS")
    """

    value = value.upper()
    send_command(f"TRDL {value}")


def get_trigger_delay():
    """
    Fragt den aktuellen Trigger-Delay ab.
    """

    return ask("TRDL?")

def get_display_delay():
    """
    Fragt den Trigger-Delay ab und dreht das Vorzeichen so,
    dass der Wert zur Anzeige am Oszilloskop passt.
    """

    answer = ask("TRDL?")
    value = answer.replace("TRDL", "").strip()

    if value.startswith("-"):
        display_value = value[1:]
    elif value.startswith("0"):
        display_value = value
    else:
        display_value = "-" + value

    return display_value
def reset_trigger_delay():
    """
    Setzt den Trigger-Delay auf 0 Sekunden.
    """

    set_trigger_delay("0S")