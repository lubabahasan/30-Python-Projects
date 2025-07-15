import time
import subprocess
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

WATCHED_FILE = "Clock_Widget.py"
PROGRAM_COMMAND = ["python", WATCHED_FILE]

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self):
        self.process = None

    def on_modified(self, event):
        if event.src_path.endswith(WATCHED_FILE):
            print(f"{WATCHED_FILE} was modified.")

            # Kill previous process if it's still running
            if self.process and self.process.poll() is None:
                print("Terminating previous instance...")
                self.process.terminate()
                try:
                    self.process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    print("Force killing unresponsive process...")
                    self.process.kill()

            # Start new process
            print("Starting new instance...")
            self.process = subprocess.Popen(PROGRAM_COMMAND)

if __name__ == "__main__":
    path = "."
    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path, recursive=False)
    
    print(f"Watching for changes to {WATCHED_FILE}...")
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping observer...")
        observer.stop()
        # Terminate the last process if running
        if event_handler.process and event_handler.process.poll() is None:
            event_handler.process.terminate()
    
    observer.join()
