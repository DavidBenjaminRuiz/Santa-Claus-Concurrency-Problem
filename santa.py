from re import A
import tkinter
import threading
from PIL import ImageTk, Image
from time import sleep

MAX_ELFS = 3
MAX_REINDEERS = 7
elfs = 0
reindeers = 0
elfs_sem = threading.Semaphore()
reindeer_sem = threading.Semaphore(MAX_REINDEERS)
mutex = threading.Semaphore()
santa_sem = threading.Semaphore()
elfs_mutex = threading.Semaphore()

App = tkinter.Tk()
App.title("Navidad de Santa")
App.geometry("1200x900")

# Load images show them in the window
elf_image = ImageTk.PhotoImage(Image.open('images/duende.jpeg').resize((400, 400)))
santa_image = ImageTk.PhotoImage(Image.open('images/santa.jpg').resize((400, 400)))
reindeer_image = ImageTk.PhotoImage(Image.open('images/reno.jpeg').resize((400, 400)))

elf_gui = tkinter.Label(App, image = elf_image)
elf_gui.grid(row = 0, column = 0)

santa_gui = tkinter.Label(App, image= santa_image)
santa_gui.grid(row= 0, column= 1)

reindeer_gui = tkinter.Label(App, image= reindeer_image)
reindeer_gui.grid(row= 0, column= 2)

# Etiquetas de conteo
elfs_cont = tkinter.StringVar()
reindeer_cont = tkinter.StringVar()
elf_help_cont = tkinter.StringVar()
reindeer_sled_cont = tkinter.StringVar()

elf_lb = tkinter.Label(App, textvariable = elfs_cont).grid(row = 1, column = 0)
reindeer_label = tkinter.Label(App, textvariable = reindeer_cont).grid(row = 1, column = 2)

# -------------------- Funciones para modificar la interfaz grafica. -------------------- #

# Función de solicitud de ayuda de los duendes.
def elfs_get_help():
    elf_help_label = tkinter.Label(App, textvariable= elf_help_cont).grid(row= 3, column=1)
    sleep(1)


# Función para atender a los procesos renos.
def prepare_sled():
    reindeer_sled_label = tkinter.Label(App, textvariable= reindeer_sled_cont).grid(row= 3, column=1)
    sleep(1)


# Función para definir que los regalos se repartieron.
def gifts():
    pass

# Función para domir a santa.
def back_to_sleep():
    santa_gui.configure(image = santa_image)
    # reindeer_gui.configure(image = reindeer_gui)


# Función para el proceso de santa claus. #
def santa_process():
    global reindeers, MAX_REINDEERS, elfs, MAX_ELFS
    print("El santa se anda échando una jeta...")
    while True:
        santa_sem.acquire()
        mutex.acquire()
        if reindeers == MAX_REINDEERS:
            reindeer_sled_cont.set("Amonos a repartir la mota")
            prepare_sled()
            print("Preparando trineo...")
            reindeer_sled_cont.set(" --- ")
            # Liberación de los procesos de los renos.
            while reindeers:
                reindeers -= 1
                reindeer_sem.release()
            sleep(3)
        elif elfs == MAX_ELFS:
            print("Santa ayuda a los duendes...")
            elf_help_cont.set("Ayudando a los duendes alv")
            elfs_get_help()
            elf_help_cont.set(" --- ")
            # Liberación de los duendes.
            while elfs:
                elfs -= 1
                sleep(1)
            sleep(3)
        mutex.release()
        back_to_sleep()

# Función para el proceso de los duendes. #
def elf_process():
    global elfs, MAX_ELFS
    while True:
        elfs_mutex.acquire()
        mutex.acquire()
        elfs += 1
        if elfs == MAX_ELFS:
            santa_sem.release()
        else:
            elfs_mutex.release()
        mutex.release()
        elfs_cont.set(f"{elfs} Duendes trabajando")
        sleep(1)
        mutex.acquire()
        if not elfs:
            elfs_mutex.release()
        mutex.release()


# Función para realizar el proceso de los renos. #
def reindeer_process():
    global reindeers, MAX_REINDEERS
    while True:
        mutex.acquire()
        reindeers += 1
        if reindeers == MAX_REINDEERS:
            santa_sem.release()
        mutex.release()
        reindeer_cont.set(f"{reindeers} Renos chambeando")
        print('total de renos:', reindeers)
        reindeer_sem.acquire()
        sleep(1)

# Ejecución principal del programa.
if __name__ == "__main__":
    santa_thread = threading.Thread(target = santa_process)
    elf_threads = threading.Thread(target = elf_process)
    reindeer_threads = threading.Thread(target = reindeer_process)

    santa_thread.start()
    elf_threads.start()
    reindeer_threads.start()

    App.mainloop()