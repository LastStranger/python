import tkinter
from pygame import mixer

from tkinter.filedialog import askopenfilename


def browse():
    global in_file
    in_file = askopenfilename()


def kml_function():
    with open(in_file, 'w') as file:
        file.write("万鹏萌萌哒")


root = tkinter.Tk()
root.title("FUCK")
label = tkinter.Label(root, text="打开一个txt文件")
label.pack()
browse_button = tkinter.Button(root, text="Browse", command=browse)
browse_button.pack()
kml_button = tkinter.Button(root, text="world", command=kml_function)
kml_button.pack()

mixer.init()
mixer.music.load("Funky Stars.mp3")
mixer.music.play()

root.mainloop()

