import subprocess
import psutil
from config import VLC_PATH, VIDEO_PATH

def play_video():
    print("[🎬] Reproduciendo video...")
    subprocess.Popen([
        VLC_PATH,
        "--fullscreen",
        "--no-video-title-show",
        "--qt-start-minimized",
        "--play-and-exit",
        VIDEO_PATH
    ])

def kill_vlc():
    print("[✖️] Cerrando VLC si está en ejecución...")
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] and 'vlc' in proc.info['name'].lower():
            proc.kill()
