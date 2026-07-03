# experiments/rc_discharge_setup.py

from oscilloscope.select_channel import select_channel

from oscilloscope.set_timebase import (
    set_time_division,
    set_display_delay,
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


def setup_rc_discharge(
    channel=2,
    trigger_level="2.5V",
    time_division="100MS",
    display_delay="374MS",
    voltage_division="1V",
    vertical_offset="-2V",
):
    """
    Stellt das Oszilloskop für eine RC-Entladung ein.

    Standard:
    - Kondensator vorher auf 5 V geladen
    - Entladung von 5 V nach 0 V
    - Trigger bei 2.5 V
    - fallende Flanke
    """

    print("RC-Entladung: Oszilloskop wird eingestellt")
    print("------------------------------------------")

    select_channel(channel)

    set_voltage_division(channel, voltage_division)
    set_vertical_offset(channel, vertical_offset)

    set_time_division(time_division)
    set_display_delay(display_delay)

    set_trigger_slope(channel, "NEG")
    set_trigger_level(channel, trigger_level)

    print()
    print("Einstellungen gesetzt:")
    print(f"Kanal:            CH{channel}")
    print(f"Volt/Div:         {get_voltage_division(channel)}")
    print(f"Offset:           {get_vertical_offset(channel)}")
    print(f"Zeitbasis:        {time_division}")
    print(f"Display-Delay:    {display_delay}")
    print(f"Trigger-Flanke:   {get_trigger_slope(channel)}")
    print(f"Trigger-Level:    {get_trigger_level(channel)}")

    print()
    print("Jetzt am Oszilloskop:")
    print("1. Kondensator auf 5 V aufladen")
    print("2. Trigger auf Single stellen")
    print("3. Entladung starten")
    print("4. Kurve aufnehmen")


if __name__ == "__main__":
    setup_rc_discharge()