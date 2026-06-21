# measure_voltage.py
# Read voltage values from Siglent SDS1204X-E channel 1 via LAN/SCPI

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


def extract_voltage(response):
    """
    Extract voltage value from Siglent response.

    Typical response:
    C1:PAVA PKPK,3.120000E+00V
    """
    match = re.search(r"([-+]?\d+\.?\d*(?:E[-+]?\d+)?)\s*V", response, re.IGNORECASE)

    if match:
        return float(match.group(1))

    return None


if __name__ == "__main__":
    print("Reading voltage from oscilloscope...")
    print(f"Device IP: {IP}")
    print(f"Channel: {CHANNEL}")
    print()

    # Peak-to-peak voltage
    response_vpp = send_scpi(f"{CHANNEL}:PAVA? PKPK")

    print("Raw response Vpp:")
    print(response_vpp)
    print()

    vpp = extract_voltage(response_vpp)

    if vpp is not None:
        print(f"Voltage peak-to-peak: {vpp:.6f} V")
    else:
        print("No valid Vpp value found.")

    print()

    # Amplitude
    response_amp = send_scpi(f"{CHANNEL}:PAVA? AMPL")

    print("Raw response amplitude:")
    print(response_amp)
    print()

    amplitude = extract_voltage(response_amp)

    if amplitude is not None:
        print(f"Amplitude: {amplitude:.6f} V")
    else:
        print("No valid amplitude value found.")

    print()

    print("Check if needed:")
    print("- Signal connected to CH1")
    print("- CH1 switched on")
    print("- Trigger stable")
    print("- Vertical scale suitable")