import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return

        src_path = os.path.join(event.src_path, "main.txt")
        dest_path = os.path.join("DestinationFolder", "main.txt")

        # Use os.rename() to move the file
        os.rename(src_path, dest_path)

        print(f"File moved from {src_path} to {dest_path}")

if __name__ == "__main__":
    # Set up the watch dog observer
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=".", recursive=False)

    # Start the observer
    observer.start()

    try:
        print("Watching for file system events. Press Ctrl+C to stop.")
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()

    # Wait until the observer thread is done
    observer.join()