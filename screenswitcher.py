
import tkinter as tk
import subprocess

def duoScreen():
    subprocess.call(['displayswitch.exe', '/extend'])
    
    
    
def singleScreen():
    subprocess.call(['displayswitch.exe', '/external'])
    

root = tk.Tk()
root.title("Screen Switcher")

panel = tk.Canvas(root, width = 300, height = 200)
panel.pack()

exitButton = tk.Button(root, text = 'Exit Application',
                       command = root.destroy)
panel.create_window(85,150, window = exitButton)


duoButton = tk.Button(root, text = 'Duo Screen',
                      command = duoScreen)
panel.create_window(85,50, window = duoButton)

singleButton = tk.Button(root, text = 'Single Screen',
                         command = singleScreen)
panel.create_window(85,100, window = singleButton)

