import socket

from configs.oscilloscope_config import (
    OSCILLOSCOPE_IP,
    OSCILLOSCOPE_PORT,
    TIMEOUT
)


def send_command(command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(TIMEOUT)
        s.connect((OSCILLOSCOPE_IP, OSCILLOSCOPE_PORT))
        s.sendall((command + "\n").encode())


def select_channel(channel=1):
    """
    Schaltet einen Oszilloskop-Kanal sichtbar ein.
    Beispiel:
    select_channel(channel=3)
    """

    if channel not in [1, 2, 3, 4]:
        raise ValueError("Kanal muss 1, 2, 3 oder 4 sein.")

    command = f"C{channel}:TRA ON"
    send_command(command)