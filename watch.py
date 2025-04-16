import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import os

class DocsHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(('.md', '.rst')):
            print(f"Change detected in {event.src_path}")
            self.rebuild_docs()

    def on_created(self, event):
        if event.src_path.endswith(('.md', '.rst')):
            print(f"New file detected: {event.src_path}")
            self.rebuild_docs()

    def on_deleted(self, event):
        if event.src_path.endswith(('.md', '.rst')):
            print(f"File deleted: {event.src_path}")
            self.rebuild_docs()

    def rebuild_docs(self):
        try:
            subprocess.run(['sphinx-build', '-b', 'html', '.', '_build/html'], check=True)
            print("Documentation rebuilt successfully!")
        except subprocess.CalledProcessError as e:
            print(f"Error rebuilding documentation: {e}")

if __name__ == "__main__":
    event_handler = DocsHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=True)
    observer.start()

    print("Watching for changes in documentation files...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join() 