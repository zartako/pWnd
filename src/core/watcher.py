import time
import pyautogui
import keyboard
import threading
import sys
from config import PREPARATION_TIME

def wait_for_mouse_move(trigger):
    print(f"[*] Esperando {PREPARATION_TIME} segundos antes de iniciar...")

    for i in range(PREPARATION_TIME, 0, -1):
        print(f"[*] Solo quedan {i}...")
        time.sleep(1)

    print("[*] Observando quien toca mi computadora...")

    stop_event = threading.Event()

    # Hilo para detectar ESC
    def esc_listener():
        while not stop_event.is_set():
            if keyboard.is_pressed('esc'):
                print("[✋] Se ha pulsado ESC. Saliendo del programa...")
                stop_event.set()
                sys.exit(0)  # Finaliza el programa inmediatamente

    esc_thread = threading.Thread(target=esc_listener, daemon=True)
    esc_thread.start()

    last_pos = pyautogui.position()
    while not stop_event.is_set():
        time.sleep(0.5)
        current_pos = pyautogui.position()
        if current_pos != last_pos:
            print("[+] Movimiento detectado.")
            stop_event.set()
            trigger()
            break