import os

def lock_system():
    print("[🔒] Bloqueando el sistema...")
    os.system("rundll32.exe user32.dll,LockWorkStation")
