# testprogramme/test_vertical.py

from oscilloscope.set_vertical import (
    set_voltage_division,
    get_voltage_division,
    set_vertical_offset,
    get_vertical_offset,
    reset_vertical_offset,
    get_error,
)


# Kanal 1: 1 V pro Kästchen
set_voltage_division(1, "1V")
print("Volt/Div CH1:", get_voltage_division(1))

# Offset auf 0 V
reset_vertical_offset(1)
print("Offset CH1:", get_vertical_offset(1))

# Kurve verschieben
set_vertical_offset(1, "1V")
print("Offset CH1:", get_vertical_offset(1))

print("Fehler:", get_error())