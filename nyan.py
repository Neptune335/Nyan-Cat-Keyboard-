import os

from  pynput import keyboard
import pygame
import time

pygame.mixer.init()
pygame.mixer.music.load("nyan.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0)

last_press_time = 0
active = False

def on_press(key):
    global last_press_time, active
    last_press_time = time.time()
    if not active:
        pygame.mixer.music.set_volume(1.0)
        active = True
        
def monitor():
    global active
    while True:
        if active and (time.time() - last_press_time > 0.25):
            for i in range(10, -1, -1):
                pygame.mixer.music.set_volume(i / 10)
                time.sleep(0.01)
            pygame.mixer.music.set_volume(0)
            active = False
        time.sleep(0.05)

def exit_program():
    print("Exiting program...")
    pygame.mixer.music.stop()
    os._exit(0)
    
hotkey_listener = keyboard.GlobalHotKeys({
    '<ctrl>+<alt>+q': exit_program
})


import threading
threading.Thread(target=monitor, daemon=True).start()

hotkey_listener.start()
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()