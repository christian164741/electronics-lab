# oscilloscope/screenshot.py

import socket
from configs.oscilloscope_config import OSCILLOSCOPE_IP, OSCILLOSCOPE_PORT, TIMEOUT


def save_screenshot(filename="oscilloscope_screenshot.bmp"):
    """
    Holt einen Screenshot vom Siglent-Oszilloskop
    und speichert ihn als Datei.
    """

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(TIMEOUT)
        s.connect((OSCILLOSCOPE_IP, OSCILLOSCOPE_PORT))

        s.sendall(b"SCDP\n")

        data = b""

        while True:
            try:
                chunk = s.recv(4096)
                if not chunk:
                    break
                data += chunk
            except socket.timeout:
                break

    with open(filename, "wb") as f:
        f.write(data)

    print(f"Screenshot gespeichert: {filename}")