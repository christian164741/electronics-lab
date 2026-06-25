# testprogramme/test_timebase.py

from oscilloscope.set_timebase import (
    set_time_division,
    get_time_division,
    set_trigger_delay,
    set_display_delay,
    get_trigger_delay,
    get_display_delay,
    reset_trigger_delay,
)


set_time_division("100MS")

#set_time_division("100MS")   # langsam, RC-Aufladung
#set_time_division("1MS")     # 1 kHz gut sichtbar
#set_time_division("10US")    # schnelle Flanken
#set_time_division("10NS")    # sehr schnelle Details

set_display_delay("466MS")
# set_trigger_delay() erzeug bei -466 erzeugt amm Oszilloskoe +466
# set_display_delay korrigiert es im Modul: set_timebase.py

timebase = get_time_division()

delay = get_display_delay()
print(f"Zeitbasis: {timebase}")
print(f"Trigger-Delay: {delay}")