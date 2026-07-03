# testprogramme/test_trigger_slope.py

from oscilloscope.set_trigger_slope import (
    set_trigger_slope,
    get_trigger_slope,
    get_error,
)


set_trigger_slope(1, "NEG")

print("Trigger-Flanke CH1:", get_trigger_slope(1))
print("Fehler:", get_error())


set_trigger_slope(1, "POS")

print("Trigger-Flanke CH1:", get_trigger_slope(1))
print("Fehler:", get_error())