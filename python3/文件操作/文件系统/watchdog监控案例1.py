from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f"{event.src_path} has been modified")

observer = Observer()
event_handler = MyHandler()
observer.schedule(event_handler, path='/path/to/folder', recursive=True)
observer.start()

# 这个无限循环可以保证程序一直运行监控文件夹
try:
    while True:
        pass
except KeyboardInterrupt:
    observer.stop()

observer.join()
