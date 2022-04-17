from curses import window
from tkinter import *
# cree fenetre
window = Tk()

#custom 
window.title("passgenerator")
window.geometry("300x300")
window.minsize(480, 360)
window.maxsize(300,300)
window.config(background='grey')
# cree frame
framee = Frame(window, bg='black', bd=1 )
framee.pack(expand=YES, side=TOP)

# ajout texte 
titre = Label(window, text="Bienvenu sur PassGenerator", font=("Courrier",20), bg='grey', foreground=('white'))
titre.pack(expand=YES,side=TOP)

# affiche 
window.mainloop()