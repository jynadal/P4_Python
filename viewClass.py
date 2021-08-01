from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

from tinydb import TinyDB, Query
db = TinyDB('dbTournoisClass.json')
import os

def main():
    window = Tk()
    Initialisation = Register(window,"Initialisation du tournoi","1500x900+50+50","#2f435e","Bienvenue à l'inscription d'un Tournoi")
    # return None

""" Window class"""
class Register:

    def __init__(self, window, title, geometry, bg_color, message):
       # personnaliser la fenêtre
        self.window = window
        self.window.title(title)
        self.window.geometry(geometry)
        self.window.minsize(580, 360)
        #self.window.iconbitmap("images/logo.ico")
        self.window.config(background=bg_color)
        #  #2f435e, #44566c, Blanc= #ececec, #4b5e65, Noir= #201b22.
        Label(self.window,text=(message), font=("Arial", 40), bg="#2f435e", fg="#ececec").pack()

        # creation d'image
        self.chessImage = ImageTk.PhotoImage(file="images/chess.png")
        chessImage  = Label(self.window, image=self.chessImage,bg="#2f435e").place(x= 150, y=200, width=500, height=600)

        # image = PhotoImage(file="images/chess.png").zoom(70).subsample(32)
        # Canvas(self.window, width=300, height=300,bg="#44566c", bd=0, highlightthickness=0).create_image(300/2, 300/2, image=image)#.pack()

        """ All variable"""
        varTournament = tk.StringVar()
        varBegin = tk.StringVar()
        varEnd = tk.StringVar()
        varNbrPlayers = tk.IntVar()

        """ TournamentFrame"""
        Tourn_Frame = Frame(self.window,bd=4,relief=RIDGE, bg="#44566c")
        Tourn_Frame.place(x=650,y=200,width=700,height=600)

        # creer un sub titre
        label_tournament = Label(Tourn_Frame, text="Nouveau du Tournoi", font=("Arial", 20), bg="#2f435e", fg="#ececec")
        label_tournament.pack(pady=10, padx= 20)

        # creer un champs/entrée/input pour le Tournoi
        tournament_name_entry = Entry(Tourn_Frame, textvariable=varTournament, justify="right", font=("Arial", 20), bg="#2f435e", fg="#ececec")
        tournament_name_entry.pack(pady=15, padx= 20)

        # creer un sub titre
        label_date_begin = Label(Tourn_Frame, text="Debute le :", font=("Arial", 20), bg="#2f435e", fg="#ececec")
        label_date_begin.pack(pady=10, padx= 20)

        # creer un champs/entrée/input pour le Tournoi
        date_begin_entry = Entry(Tourn_Frame, textvariable=varBegin, justify="right", font=("Arial", 20), bg="#2f435e", fg="#ececec")
        date_begin_entry.pack(pady=15, padx= 20)

        # creer un sub titre
        label_date_end = Label(Tourn_Frame, text="Jusqu'à :", font=("Arial", 20), bg="#2f435e", fg="#ececec")
        label_date_end.pack(pady=10, padx= 20)

        # creer un champs/entrée/input pour le Tournoi
        date_end_entry = Entry(Tourn_Frame,textvariable=varEnd, justify="right", font=("Arial", 20), bg="#2f435e", fg="#ececec")
        date_end_entry.pack(pady=15, padx= 20)

        # creer un sub titre
        label_nbr_players = Label(Tourn_Frame, text="Nombre de participant :", font=("Arial", 20), bg="#2f435e", fg="#ececec")
        label_nbr_players.pack(pady=10, padx= 20)

        # creer un champs/entrée/input pour le Tournoi
        nbr_players_entry = Entry(Tourn_Frame, textvariable=varNbrPlayers, justify="right", font=("Arial", 20), bg="#2f435e", fg="#ececec")
        nbr_players_entry.pack( pady=15, padx= 20)

        # creer une sous boite de la frame pour boutton
        #btn_frame = Frame(Tourn_Frame, bg="#2f435e")

        def add_tournament():
            if varTournament.get()=="" or varBegin.get()=="" or varEnd.get()=="" or varNbrPlayers.get()=="":
                messagebox.showerror("warning","Veuillez remplir tout les champs!")
            else:
                db.insert({'name': (varTournament.get()), 'T_Begin' : (varBegin.get()), 'T_End':(varEnd.get()), 'Nbr_players': (varNbrPlayers.get())})
                messagebox.showinfo("success","Les infos du tournois ont été enregistrés avec SUCCESS")

        def reset_tournament():
            varTournament.set("")
            varBegin.set("")
            varEnd.set("")
            varNbrPlayers.set("")
           
        def set_tournament():
            pass

        def del_tournament():
            pass



        """ btn frame """
        btn_frame = Frame(window,bd=3,relief=RIDGE, bg="#2f435e")
        btn_frame.place(x=700,y= 725,width=600)

        Add_btn = Button(btn_frame,text="Ajouter", width=10, cursor="hand2",command= add_tournament).grid(row=0, column=0,padx=10, pady=10) #command=self.add_students
        clear_btn = Button(btn_frame,text="Reset", width=10, cursor="hand1",command= reset_tournament).grid(row=0, column=2,padx=10, pady=10)
        Update_btn = Button(btn_frame,text="Modifier précédent", width=15, cursor="hand2",command= set_tournament).grid(row=0, column=3,padx=10, pady=10)
        Delete_btn = Button(btn_frame,text="Supprimer précédent", width=15, cursor="hand1",command= del_tournament).grid(row=0, column=4,padx=10, pady=10)

        # creer un bouton le Tournoi
        btn_tournament = Button(btn_frame,text="Envoyer", command=add_tournament, font=("Arial", 20), bg="#2f435e", fg="#ececec")
        btn_tournament.place(x=110,y= 285,width=150)




        self.window.mainloop()
        pass
    pass



main()


# """ Prémiere fenetre de tournoi """



# # ajouter un premier texte
# label_title = Label(window, text="Bienvenue à l'inscription d'un Tournoi", font=("Arial", 40), bg="#2f435e", fg="#ececec")
# label_title.pack(side=TOP,fill=X)

# # le frame


# # afficher
# window.mainloop()