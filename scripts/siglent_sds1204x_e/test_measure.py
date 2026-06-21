# test_measure.py

from measure_frequenz import measure_frequency
from measure_voltage import measure_voltage


def main():
    print("Messung am Siglent SDS1204X-E")
    print("-----------------------------")

    try:
        frequenz = measure_frequency()
        spannung = measure_voltage()

        print(f"Frequenz: {frequenz:.2f} Hz")
        print(f"Spannung: {spannung:.3f} Vpp")

    except Exception as e:
        print("Fehler bei der Messung:")
        print(e)


if __name__ == "__main__":
    main()