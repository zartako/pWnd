import threading
import keyboard

class BlockKeyboard:
    def __init__(self):
        self.stop_flag = threading.Event()
        self.hook = None

    def _block_event(self, event):
        if self.stop_flag.is_set():
            return False  # Detiene el hook
        return False  # Bloquea el evento

    def start(self):
        print("[⌨️] Bloqueando teclado con hook global...")
        self.hook = keyboard.hook(self._block_event, suppress=True)

    def stop(self):
        print("[🛑] Desbloqueando teclado...")
        self.stop_flag.set()
        if self.hook:
            keyboard.unhook(self.hook)
