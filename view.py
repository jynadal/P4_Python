from tkinter import *
import tkinter as tk
from tkinter import messagebox

from tinydb import TinyDB, Query
db = TinyDB('dbTestTournois.json')

import os

""" Prémiere fenetre de tournoi """
window = Tk()

# personnaliser la fenêtre
window.title("Initialisation du tournoi")
window.geometry("1400x800+50+50")
window.minsize(580, 360)
#window.iconbitmap('images/logo.ico')
window.config(background="#2f435e")
#  #2f435e, #44566c, Blanc= #ececec, #4b5e65, Noir= #201b22.

# ajouter un premier texte
label_title = Label(window, text="Bienvenue à l'inscription d'un Tournoi", font=("Arial", 40), bg="#2f435e", fg="#ececec")
label_title.place(x=200, y=100,width=1200)

# creer la frame principale
frame = Frame(window, bg="#2f435e")

# création d'image
width= 400
height = 500
image = PhotoImage(file="images/chess.png").zoom(70).subsample(52)
canvas = Canvas(frame, width = width, height= height, bg="#2f435e", bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)

# creer une sous boite de la frame
right_frame = Frame(frame, bg="#2f435e")

""" All variable"""
varTournament = tk.StringVar()
varBegin = tk.StringVar()
varEnd = tk.StringVar()
varNbrPlayers = tk.IntVar()

# creer une sous boite de la frame pour boutton
btn_frame = Frame(frame, bg="#2f435e")

def add_tournament():
    if varTournament.get()=="" or varBegin.get()=="" or varEnd.get()=="" or varNbrPlayers.get()=="":
        messagebox.showerror("warning","Veuillez remplir tout les champs!")
    else:
        db.insert({'name': (varTournament.get()), 'T_Begin' : (varBegin.get()), 'T_End':(varEnd.get()), 'Nbr_players': (varNbrPlayers.get())})


""" btn frame """
btn_frame = Frame(window,bd=3,relief=RIDGE, bg="#44566c")
btn_frame.place(x=550,y= 625,width=530)

Add_btn = Button(btn_frame,text="Add", width=10, cursor="hand2",command= add_tournament).grid(row=0, column=0,padx=10, pady=10) #command=self.add_students
Update_btn = Button(btn_frame,text="Modifier", width=10).grid(row=0, column=1,padx=10, pady=10)
Delete_btn = Button(btn_frame,text="Supprimer", width=10).grid(row=0, column=2,padx=10, pady=10)
clear_btn = Button(btn_frame,text="Reset", width=10).grid(row=0, column=3,padx=10, pady=10)

# creer un sub titre
label_tournament = Label(right_frame, text="Inscrivez le nom du Tournoi", font=("Arial", 20), bg="#2f435e", fg="#ececec")
label_tournament.pack()

# creer un champs/entrée/input pour le Tournoi
tournament_name_entry = Entry(right_frame, textvariable=varTournament, font=("Arial", 20), bg="#2f435e", fg="#ececec")
tournament_name_entry.pack()

# creer un sub titre
label_date_begin = Label(right_frame, text="Debute le :", font=("Arial", 20), bg="#2f435e", fg="#ececec")
label_date_begin.pack()

# creer un champs/entrée/input pour le Tournoi
date_begin_entry = Entry(right_frame, textvariable=varBegin, font=("Arial", 20), bg="#2f435e", fg="#ececec")
date_begin_entry.pack()

# creer un sub titre
label_date_end = Label(right_frame, text="Jusqu'à :", font=("Arial", 20), bg="#2f435e", fg="#ececec")
label_date_end.pack()

# creer un champs/entrée/input pour le Tournoi
date_end_entry = Entry(right_frame,textvariable=varEnd, font=("Arial", 20), bg="#2f435e", fg="#ececec")
date_end_entry.pack()

# creer un sub titre
label_nbr_players = Label(right_frame, text="Nombre de participant :", font=("Arial", 20), bg="#2f435e", fg="#ececec")
label_nbr_players.pack()

# creer un champs/entrée/input pour le Tournoi
nbr_players_entry = Entry(right_frame, textvariable=varNbrPlayers, font=("Arial", 20), bg="#2f435e", fg="#ececec")
nbr_players_entry.pack()

# creer un bouton le Tournoi
btn_tournament = Button(btn_frame,text="Envoyer", command=add_tournament, font=("Arial", 20), bg="#2f435e", fg="#ececec")
btn_tournament.place(x=110,y= 285,width=150)


# on place la sous boite à droite de la frame pricipale
right_frame.grid(row=0, column=1, sticky=W)

# # on place la sous boite à droite de la frame pricipale
# btn_frame.grid(row=1, column=0, sticky=N)

# afficher la frame
frame.pack(expand=YES)

# afficher
window.mainloop()

#  https://www.meerodrop.com/fr/drop/b3bfc282-e483-4f4c-81bb-5eed3ecb6c41/media/013c4f23-da6b-4fcc-8345-a4d0bcc7c4e6