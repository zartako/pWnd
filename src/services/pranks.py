import subprocess
from config import NOTE_PATH

def creepy_notes():
    with open(NOTE_PATH, "w", encoding="utf-8") as f:
        f.write("\n" * 10)
        f.write("👁️  ¿Creías que nadie te vigilaba?\n\n")
        f.write("💻  Este equipo está protegido.\n")
        f.write("🚫  No deberías estar tocándolo.\n\n")
        f.write("😈  Atentamente, el dueño.\n")

    subprocess.Popen(f'start /MAX notepad "{NOTE_PATH}"', shell=True)
