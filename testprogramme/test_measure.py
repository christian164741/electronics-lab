# test_measure.py

from oscilloscope.measure_frequenz import measure_frequency
from oscilloscope.measure_voltage import measure_voltage
from oscilloscope.select_channel import select_channel

def main():
    print("Messung am Siglent SDS1204X-E")
    print("-----------------------------")

    try:
        frequenz = measure_frequency(channel=2)
        channel = 2

        frequenz = measure_frequency(channel=channel)
        print(f"Kanal {channel}: Frequenz = {frequenz:.2f} Hz")
        
        spannung = measure_voltage(channel=2)
        channe = 2
        
        print(f"Kanal {channel}: Spannung= {spannung:.3f} Vpp")
     
        select_channel(channel=3)  
        print(f"Kanal {channel} wurde eingeschalten.")
        
    except Exception as e:
        print("Fehler bei der Messung:")
        print(e)

     
    
if __name__ == "__main__":
    main()