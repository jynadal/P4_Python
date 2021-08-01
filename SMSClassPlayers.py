from os import closerange
from tkinter import *
from tkinter import ttk
from tinydb import TinyDB, Query
dbIn = TinyDB('dbAddPlayers.json')
from tkinter import messagebox
import simplejson as json

background_color = "#2f435e"
background_color2 = "#44566c" 
font_color = '#ececec',
background_color3 ='#4b5e65' 
#Noir= #201b22

class Players():

    variables = ["fname_var","lname_var","DBirth_var","gender_var","rang_No_var"]

    """ Add json file for name ..."""
    with open ('dbTournoisClassHardCode.json','r') as myfile:
        data=myfile.read()

        objs = json.loads(data)
        last_T=(len(objs["_default"])) # the last tournament
        print(objs["_default"][str(last_T)]["name"])
    """ END Add json file for name ..."""


    NBR_PLAYERS = objs["_default"][str(last_T)]["Nbr_players"]
    TOURNAMENT_NAME = objs["_default"][str(last_T)]["name"]
    BEGIN = str(objs["_default"][str(last_T)]["T_Begin"])
    END =  objs["_default"][str(last_T)]["T_End"]
    """ END Add json file for name ..."""


    def __init__(self,root):
        self.root = root
        self.root.title("Inscription "+self.TOURNAMENT_NAME)
        self.root.geometry("1500x900+50+50")

        title = Label(self.root, text="Inscriptions joueurs - "+self.TOURNAMENT_NAME,bd=9,relief=GROOVE, font=("times new roman",50,"bold"),bg=background_color,fg=font_color)
        title.pack(side=TOP,fill=X)

        """ All variable"""
        self.fname_var =[StringVar() for _ in range(8)]
        self.lname_var =  [StringVar() for _ in range(8)]
        self.DBirth_var =[StringVar() for _ in range(8)]
        self.gender_var =[StringVar() for _ in range(8)]
        self.rang_No_var =[StringVar() for _ in range(8)]
        self.search_by =[StringVar() for _ in range(8)]
        self.search_txt =[StringVar() for _ in range(8)]

        # labels = ["fname_var","lname_var","DBirth_var","gender_var","rang_No_var"]

        """ ManageFrame"""
        Manage_Frame = Frame(self.root,bd=4, bg=background_color)
        Manage_Frame.place(x=20,y=100,width=1500,height=800)

        # m_title = Label(Manage_Frame, text="Inscriptions", bg="white",fg="black",font=("times new roman",35))
        # m_title.grid(row=0, columnspan=2, pady=10)

        lbl_rang = Label(Manage_Frame, text="Rang No", bg="blue",fg="white",font=("lato",20))
        lbl_rang.grid(row=0, column=0, pady=5, padx= 5, sticky="w")
       

        lbl_fname = Label(Manage_Frame, text="First Name", bg="blue",fg="white",font=("lato",20,"bold"))
        lbl_fname.grid(row=0, column=1, pady=10, padx= 50, sticky="w")
        lbl_lname = Label(Manage_Frame, text="Last Name", bg="blue",fg="white",font=("lato",20,"bold"))
        lbl_lname.grid(row=0, column=2, pady=10, padx= 50, sticky="w")
        lbl_Gender = Label(Manage_Frame, text="Sexe", bg="blue",fg="white",font=("lato",20,"bold"))
        lbl_Gender.grid(row=0, column=4, pady=10, padx= 50, sticky="w")
        lbl_dBirth = Label(Manage_Frame, text="Date of Birth", bg="blue",fg="white",font=("lato",20,"bold"))
        lbl_dBirth.grid(row=0, column=3, pady=10, padx= 50, sticky="w")

        for i in range(self.NBR_PLAYERS):

            rang = i + int(1)

            txt_rang = Label(Manage_Frame,text=(rang), bg="blue",fg="white",font=("lato",20))
            txt_rang.grid(row=(rang), column=0, pady=5, padx= 10, sticky="w")

            """ First name """
            self.fname_var =[StringVar() for _ in range(8)]
            txt_fname = Entry(Manage_Frame, textvariable=self.fname_var[i], font=("lato",15),bd=5,relief=GROOVE)
            txt_fname.grid(row=(rang), column=1, pady=10, padx=30, sticky="w")

            """ Last name """
            txt_lname = Entry(Manage_Frame,textvariable=self.lname_var[i],font=("lato",15),bd=5,relief=GROOVE)
            txt_lname.grid(row=(rang), column=2, pady=10, padx=30, sticky="w")

            """ dBirth """
            txt_dBirth = Entry(Manage_Frame,textvariable=self.DBirth_var[i],font=("lato",15),bd=5,relief=GROOVE)
            txt_dBirth.grid(row=(rang), column=3, pady=10, padx=30, sticky="w")

            """ Combobox Gender """
            combo_gender = ttk.Combobox(Manage_Frame,textvariable=self.gender_var[i],font=("lato",15,"bold"),state='normal')
            combo_gender['values'] = ('male','female','other')
            combo_gender.grid(row=(rang), column=4, pady=10, padx=30)

        """ btn frame """
        btn_frame = Frame(Manage_Frame,bd=3,relief=RIDGE, bg=background_color2)
        btn_frame.place(x=20,y= 615,width=1430)

        Add_btn = Button(btn_frame,text="Add", width=10, command=self.add_players).grid(row=0, column=0,padx=10, pady=10)
        clear_btn = Button(btn_frame,text="Reset", width=10, command=self.reset_players).grid(row=0, column=3,padx=10, pady=10)


    def add_players(self):
        for i in range(self.NBR_PLAYERS):
            dbIn.insert({'fname': (self.fname_var[i].get()), 'lname' : (self.lname_var[i].get()), 'DBirth':(self.DBirth_var[i].get()), 'gender': (self.gender_var[i].get()), 'rang' : (self.rang_No_var[i].get())
            })
        messagebox.showinfo("success","Vos joueurs ont été enregistrés avec SUCCESS")
    
    def reset_players(self):
        #self.fname_var.set("")
        #self.lname_var.set("")
        # DBirth_var.set =[StringVar() for _ in range(8)]
        # gender_var.set =[StringVar() for _ in range(8)]
        # rang_No_var =[StringVar() for _ in range(8)]
        # search_by =[StringVar() for _ in range(8)]
        # search_txt =[StringVar() for _ in range(8)]
        pass


class Student():
    pass
    root= Tk()
    obj= Players(root)
    root.mainloop()