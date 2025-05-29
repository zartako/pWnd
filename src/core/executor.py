import threading
import time
from services.vlc import play_video, kill_vlc
from services.pranks import creepy_notes
from services.lock import lock_system
from services.reverse_mouse import ReverseMouse
from services.block_keyboard import BlockKeyboard
from config import TROLL_MODE, VIDEO_TIME, LOCK_TIME

def handle_trigger():
    print("[🎬] Lanzando acción principal...")
    play_video()

    reverse_mouse = ReverseMouse()
    reverse_mouse.start()

    keyboard_block = BlockKeyboard()
    keyboard_block.start()

    def actions():
        time.sleep(VIDEO_TIME)
        kill_vlc()
        reverse_mouse.stop()
        keyboard_block.stop()

        if TROLL_MODE:
            creepy_notes()

        time.sleep(LOCK_TIME)
        lock_system()

    thread = threading.Thread(target=actions)
    thread.start()
    thread.join()
