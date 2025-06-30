import os
import shutil
import time
import tkinter as tk
import winsound
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import getpass
from termcolor import colored
import datetime

# os.system("title", "DownloadWatcher")
# ctypes.windll.kernel32.SetConsoleTitleA("DownloadWatcher")
print(colored("[~] Überwachung der Downloads wurde gestartet!", "light_cyan"))

username  = getpass.getuser()

# log_file = open("C:\download_txt", "w")

src_dir = f"C:/Users/{username}/Downloads"
doc_dir = f"C:/Users/{username}/Downloads/Documents"
exe_dir = f"C:/Users/{username}/Downloads/Executables"
img_dir = f"C:/Users/{username}/Downloads/Images"
iso_dir = f"C:/Users/{username}/Downloads/ISO"
pdf_dir = f"C:/Users/{username}/Downloads/PDF"
rox_dir = f"C:/Users/{username}/Downloads/Roxtra"
xls_dir = f"C:/Users/{username}/Downloads/Excel"
zip_dir = f"C:/Users/{username}/Downloads/Archives"

file_doc = (".docx", ".doc", ".dotx", ".dot", ".docm")
file_exe = (".exe", ".msi", ".bat", ".cmd", ".app", ".sh", ".run", ".bin", ".jar", ".cgi", ".pl", ".py", ".wsf", ".ps1", ".vbs")
file_img = (".jpeg", ".jpg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".svg", ".heif", ".ico", ".raw", ".indd", ".ai", ".eps", ".jfif")
file_xls = (".xlsx", ".xls", ".xlsm", ".xltx", ".xlt")
file_zip = (".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".arj", ".lzh", ".cab", ".ace", ".uue", ".z", ".pak", ".rpm")


def MoveFile(entry, destination):
    file_path = destination + "/" + entry.name
    if os.path.exists(file_path):
        winsound.PlaySound("*", winsound.SND_ALIAS)
        print(colored(f"[!] Die Datei {entry.name} existiert bereits.", "yellow"))
        print(colored(f"[!] Bitte speichern Sie die Datei unter einem anderen Namen!","yellow"))
        print(colored(f"[!] {src_dir}/{entry.name} wurde gelöscht","red"))
        os.remove(src_dir + "/" + entry.name)
    else:
        now_time = datetime.datetime.now()
        shutil.move(entry, destination)
        print(colored(f"{now_time} -- [!] {entry.name} wurde in den Ordner {destination} verschoben", "light_green"))


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with os.scandir(src_dir) as entries:
            for entry in entries:
                name = entry.name
                if name.endswith(file_doc):
                    destination = doc_dir
                    MoveFile(entry, destination)
                elif name.endswith(file_exe):
                    destination = exe_dir
                    MoveFile(entry, destination)
                elif name.endswith(file_img):
                    destination = img_dir
                    MoveFile(entry, destination)
                elif name.endswith(".iso"):
                    destination = iso_dir
                    MoveFile(entry, destination)
                elif name.endswith(".pdf"):
                    destination = pdf_dir
                    MoveFile(entry, destination)
                elif name.endswith(".rox"):
                    destination = rox_dir
                    MoveFile(entry, destination)
                elif name.endswith(".xls"):
                    destination = xls_dir
                    MoveFile(entry, destination)
                elif name.endswith(".zip"):
                    destination = zip_dir
                    MoveFile(entry, destination)

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, src_dir, recursive=True)
observer.start()

root = tk.Tk()
root.withdraw()
root.mainloop()

try:
    while True:
        time.sleep(20)
except KeyboardInterrupt:
    observer.stop()
observer.join()