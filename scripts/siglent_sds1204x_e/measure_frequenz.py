# measure_frequenz.py
# Read frequency from Siglent SDS1204X-E channel 1 via LAN/SCPI

import socket
import re

IP = "192.168.2.117"
PORT = 5025

CHANNEL = "C1"


def send_scpi(command):
    """Send one SCPI command to the oscilloscope and return the response."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(3)
        sock.connect((IP, PORT))
        sock.sendall((command + "\n").encode())
        response = sock.recv(4096).decode(errors="ignore").strip()
        return response


def extract_frequency(response):
    """
    Extract frequency value from Siglent response.

    Typical response:
    C1:PAVA FREQ,1.000000E+03Hz
    """
    match = re.search(r"([-+]?\d+\.?\d*(?:E[-+]?\d+)?)\s*Hz", response, re.IGNORECASE)

    if match:
        return float(match.group(1))

    return None


if __name__ == "__main__":
    print("Reading frequency from oscilloscope...")
    print(f"Device IP: {IP}")
    print(f"Channel: {CHANNEL}")
    print()

    response = send_scpi(f"{CHANNEL}:PAVA? FREQ")

    print("Raw response:")
    print(response)
    print()

    frequency = extract_frequency(response)

    if frequency is not None:
        print(f"Frequency: {frequency:.3f} Hz")
        print(f"Frequency: {frequency / 1000:.6f} kHz")
    else:
        print("No valid frequency value found.")
        print("Check:")
        print("- Is the signal connected to CH1?")
        print("- Is CH1 switched on?")
        print("- Is the trigger stable?")
        print("- Is the signal periodic?")