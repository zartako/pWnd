from core.watcher import wait_for_mouse_move
from core.executor import handle_trigger

def main():
    wait_for_mouse_move(trigger=handle_trigger)

if __name__ == "__main__":
    main()
