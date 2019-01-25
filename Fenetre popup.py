from tkinter import *
from tkinter import ttk

def popup():
    fInfos = Toplevel()
    fInfos.title('Règles')
    Label(fInfos, text="La bataille navale est un jeu de société qui se joue à 2\n où le joueur doit placer des navires sur une grille qui n'est pas visible par l'adversiare.\n Chaque tour, le joueur doit essayer de toucher les navires de l'adversaire.\n Le gagant est celui qui a coulé tous les bateaux de l'adversaire").pack(padx=10,pady=10)
    Button(fInfos, text="J'ai compris", command=fInfos.destroy).pack(side="bottom")
    fInfos.transient(jeu) 
    fInfos.grab_set()
    jeu.wait_window(fInfos)

jeu = Tk()					  
jeu.title('Bataille navale')
jeu.geometry('300x100')
Button(jeu, text='Règles', command=popup).pack(padx=10, pady=10)

jeu.mainloop()