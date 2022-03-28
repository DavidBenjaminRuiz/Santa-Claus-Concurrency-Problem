from tkinter import *
from tkinter import ttk
import tkinter
from PIL import ImageTk, Image

root = Tk()
root.geometry("900x900")
label = tkinter.Label(root, text=" TALLER DE SANTA ", font= ("Arial", 30))
label.pack()
MAX_REINDEERS = 7
MAX_ELVES = 3


def add_elf():

    print("elfo")

def add_reindeer():
    print("reindeer")

elf_button  = tkinter.Button(root, text=" Añadir duende", command= add_elf, width=20, height= 3)
santa_image = ImageTk.PhotoImage(Image.open('images/santa.jpg').resize((400, 400)))
santa_label = tkinter.Label(root, image=santa_image)
reindeer_button = tkinter.Button(root, text=" Añadir reno", command= add_reindeer, width=20, height= 3)


santa_label.pack()
elf_button.pack(side = LEFT, padx=100, pady=100)
reindeer_button.pack(side = RIGHT, padx=100, pady=100)

root.mainloop()