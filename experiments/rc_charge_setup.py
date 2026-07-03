# experiments/rc_charge_setup.py
from oscilloscope.select_channel import select_channel
from oscilloscope.set_timebase import (
    set_time_division,
    set_display_delay,
    reset_trigger_delay,
)

from oscilloscope.set_trigger_level import (
    set_trigger_level,
    get_trigger_level,
)

from oscilloscope.set_trigger_slope import (
    set_trigger_slope,
    get_trigger_slope,
)

from oscilloscope.set_vertical import (
    set_voltage_division,
    set_vertical_offset,
    get_voltage_division,
    get_vertical_offset,
)


def setup_rc_charge(
    channel=1,
    supply_voltage="5V",
    trigger_level="3.16V",
    time_division="100MS",
    display_delay="374MS",
    voltage_division="1V",
    vertical_offset="-2V",
):
    """
    Stellt das Oszilloskop für eine RC-Aufladung ein.

    Standard:
    - Kanal 1
    - 5 V Aufladung
    - Trigger bei 2.5 V
    - steigende Flanke
    - 100 ms/div
    - 374 ms Display-Delay
    - 1 V/div
    - 2 V Offset

    Wichtig:
    CH1, Edge-Trigger und Single-Modus können vorher manuell am Oszilloskop eingestellt werden.
    """

    print("RC-Aufladung: Oszilloskop wird eingestellt")
    print("------------------------------------------")
    # Channel einstellen
    select_channel(channel)

    
    # Vertikal einstellen
    set_voltage_division(channel, voltage_division)
    set_vertical_offset(channel, vertical_offset)

    # Horizontal einstellen
    set_time_division(time_division)
    set_display_delay(display_delay)

    # Trigger einstellen
    set_trigger_slope(channel, "POS")
    set_trigger_level(channel, trigger_level)

    print()
    print("Einstellungen gesetzt:")
    print(f"Kanal:              CH{channel}")
    print(f"Versorgung:         {supply_voltage}")
    print(f"Volt/Div:           {get_voltage_division(channel)}")
    print(f"Vertikal-Offset:    {get_vertical_offset(channel)}")
    print(f"Zeitbasis:          {time_division}")
    print(f"Display-Delay:      {display_delay}")
    print(f"Trigger-Flanke:     {get_trigger_slope(channel)}")
    print(f"Trigger-Level:      {get_trigger_level(channel)}")

    print()
    print("Jetzt am Oszilloskop:")
    print("1. Kondensator entladen")
    print("2. Trigger auf Single stellen")
    print("3. Aufladung starten")
    print("4. Kurve aufnehmen")
   
    

if __name__ == "__main__":
    setup_rc_charge()