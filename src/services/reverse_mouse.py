import threading
import time
from pynput.mouse import Controller, Listener, Button

class ReverseMouse:
    def __init__(self):
        self.stop_flag = threading.Event()
        self.mouse_controller = Controller()
        self.motion_thread = None
        self.mouse_listener = None

    def _invert_motion(self):
        last_pos = self.mouse_controller.position
        while not self.stop_flag.is_set():
            time.sleep(0.01)
            current_pos = self.mouse_controller.position
            dx = current_pos[0] - last_pos[0]
            dy = current_pos[1] - last_pos[1]

            if dx != 0 or dy != 0:
                new_x = current_pos[0] - dx
                new_y = current_pos[1] - dy
                self.mouse_controller.position = (new_x, new_y)

            last_pos = self.mouse_controller.position

    def _on_click(self, x, y, button, pressed):
        if not pressed or self.stop_flag.is_set():
            return False
        if button == Button.left:
            self.mouse_controller.click(Button.right)
        elif button == Button.right:
            self.mouse_controller.click(Button.left)
        return False

    def start(self):
        print("[🌀] Invirtiendo el ratón...")
        self.motion_thread = threading.Thread(target=self._invert_motion, daemon=True)
        self.motion_thread.start()

        self.mouse_listener = Listener(on_click=self._on_click)
        self.mouse_listener.start()

    def stop(self):
        print("[🛑] Deteniendo inversión del ratón...")
        self.stop_flag.set()
        if self.mouse_listener:
            self.mouse_listener.stop()
        if self.motion_thread:
            self.motion_thread.join()
