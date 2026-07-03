# testprogramme/test_trigger_level.py

from oscilloscope.set_trigger_level import (
    set_trigger_level,
    get_trigger_level,
    get_error,
)


set_trigger_level(1, "2.5V")

print("Trigger-Level CH1:", get_trigger_level(1))
print("Fehler:", get_error())