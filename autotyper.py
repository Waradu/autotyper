from pynput.keyboard import Controller, Key, Listener
import time
import sys
import tkinter as tk
from tkinter import filedialog
from threading import Thread

keyboard = Controller()
content = ""
stop_flag = False


def press(char):
  keyboard.press(char)
  keyboard.release(char)


def start_typing():
  global content
  time.sleep(5)
  i = 0
  for char in content:
    if stop_flag:
      break
    if char == '\n':
      if i + 1 < len(content) and content[i + 1] != "}":
        press(Key.enter)
      continue
    if char == "}":
      press(Key.down)
      continue
    press(char)
    time.sleep(.01)
    i += 1


def select_file():
  global content
  filepath = filedialog.askopenfilename(
      filetypes=[("Java files", "*.java"), ("All files", "*.*")])
  if filepath:
    with open(filepath, 'r') as file:
      content = file.read()


def on_start():
  threading = Thread(target=start_typing)
  threading.start()


def on_press(key):
  global stop_flag
  if key == Key.esc:
    stop_flag = True
    return False


def on_release(key):
  pass


listener = Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

root = tk.Tk()
root.title("Auto Typer")

label = tk.Label(
    text="Achtung datei darf keinen indent haben\n(ctrl+a und dann so oft shift+tab drücken bis sich nichts mehr ändert)")
label.pack(pady=10)

file_button = tk.Button(root, text="Datei auswählen", command=select_file)
file_button.pack(pady=10)

label2 = tk.Label(
    text="1. File auswählen\n2. Start drücken\nZum editor wechseln (nach 5sek started es)")
label2.pack(pady=10)

start_button = tk.Button(root, text="Start", command=on_start)
start_button.pack(pady=10)

label3 = tk.Label(
    text="Escape drücken um zu stoppen")
label3.pack(pady=10)

root.geometry("450x300")

root.mainloop()
