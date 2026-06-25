# test_single_trigger.py

from oscilloscope.set_trigger import single_trigger,set_trigger_mode, get_trigger_mode


single_trigger()
# mode = set_trigger_mode("AUTO")
mode = get_trigger_mode()
print(f"Aktueller Trigger-Modus: {mode}")