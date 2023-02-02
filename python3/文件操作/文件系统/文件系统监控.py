# coding:utf8

import time

from watchdog.events import *
from watchdog.observers import Observer


class FileEventHandler(FileSystemEventHandler):
    oldStr = ""

    def __init__(self):

        FileSystemEventHandler.__init__(self)

    def on_moved(self, event):
        if event.is_directory:
            # pass
            print("directory moved from {0} to {1}".format(event.src_path, event.dest_path))
        else:
            # pass
            print("file moved from {0} to {1}".format(event.src_path, event.dest_path))

    def on_created(self, event):
        if event.is_directory:
            # pass
            print("directory created:{0}".format(event.src_path))
        else:
            # pass
            print("file created:{0}".format(event.src_path))

    def on_deleted(self, event):
        if event.is_directory:
            # pass
            print("directory deleted:{0}".format(event.src_path))
        else:
            # pass
            print("file deleted:{0}".format(event.src_path))

    def on_modified(self, event):
        if event.is_directory:
            # pass
            print("directory modified:{0}".format(event.src_path))
        else:
            # 这里加的if是为了避免同一个事件多次发生
            # 注意，这里操作的变量极有可能出现多线程问题，最好加锁
            if event.src_path != self.oldStr:
                # -------------------------------------------------
                # 在这里加上要执行的事情
                print("file modified:{0}".format(event.src_path))
                # -------------------------------------------------
                self.oldStr = event.src_path


if __name__ == "__main__":
    observer = Observer()
    event_handler = FileEventHandler()
    observer.schedule(event_handler, "c:/", True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
