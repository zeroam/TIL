import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        print(f"{event.event_type} {event.src_path}")

    def on_created(self, event):
        print(f"on_created {event.src_path}")

    def on_deleted(self, event):
        print(f"on_deleted {event.src_path}")

    def on_modified(self, event):
        print(f"on_modified {event.src_path}")

    def on_moved(self, event):
        print(f"on_moved {event.src_path}")


if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    observer.schedule(event_handler, path, recursive=True)
    observer.start()  # 스레드 실행

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
