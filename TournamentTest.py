from tkinter import *
import tkinter as tk
from tkinter import ttk
import simplejson as json
from tinydb import TinyDB, Query
dbTournamentTest2 = TinyDB('dbTournamentTest2.json')
dbTournamentTest3 = TinyDB('dbTournamentTest3.json')
dbjoueurNTestA = TinyDB('dbjoueurNTestA.json')
dbjoueurNTestB = TinyDB('dbjoueurNTestB.json')


from tkinter import messagebox

background_color = "#2f435e"
background_color2 = "#44566c" 
font_color = '#ececec',
background_color3 ='#4b5e65' 
#Noir= #201b22

class Big_window(): #Register
    """ Add json file for name ..."""
    with open ('dbTournoisClassHardCode.json','r') as myfile:
        data=myfile.read()
        objs = json.loads(data)
        last_T=(len(objs["_default"])) # the last tournament

    """ END Add json file for name ..."""

    """ Add json file for players ..."""
    with open ('dbForWork.json','r') as mylist:
        data=mylist.read()

        R1_players = json.loads(data)
        #print(R1_players["_default"])
        Players_data = R1_players["_default"]
    """ END Add json file for name ..."""


    NBR_PLAYERS = objs["_default"][str(last_T)]["Nbr_players"]
    TOURNAMENT_NAME = objs["_default"][str(last_T)]["name"]
    BEGIN = str(objs["_default"][str(last_T)]["T_Begin"])
    END =  objs["_default"][str(last_T)]["T_End"]
    PLAYERS_DATA = R1_players["_default"]
    variables = ["fname_var","lname_var","DBirth_var","gender_var","rang_No_var"]
    width = "1400"
    height = "200" 


    # for i, player in range(PLAYERS_DATA):
    #     print("{} => {}".format([i],player))
        
    # for i, nbr_joueur in enumerate(PLAYERS_DATA):
    #     print("{} => {}".format([i],nbr_joueur))
    #     print(str(nbr_joueur))

    # for player1 key, value in R1_players["_default"]['1']:
    #     print(player1)
    #========================================== Code à factoriser avec une LOOP =========================================
    PLAYERS_DATA1 = R1_players["_default"]['1']
    PLAYERS_DATA2 = R1_players["_default"]['2']
    PLAYERS_DATA3 = R1_players["_default"]['3']
    PLAYERS_DATA4 = R1_players["_default"]['4']
    PLAYERS_DATA5 = R1_players["_default"]['5']
    PLAYERS_DATA6 = R1_players["_default"]['6']
    PLAYERS_DATA7 = R1_players["_default"]['7']
    PLAYERS_DATA8 = R1_players["_default"]['8']

    #========================================== FIN Code à factoriser avec une LOOP =====================================

    def __init__(self, window,title, geometry, bg_color, message):
       # personnaliser la fenêtre
        self.window = window
        self.window.title(title+self.TOURNAMENT_NAME)
        self.window.geometry(geometry)
        self.window.minsize(580, 360)
        #self.window.iconbitmap("images/logo.ico")
        self.window.config(background=bg_color)
        #  #2f435e, #44566c, Blanc= #ececec, #4b5e65, Noir= #201b22.
        Label(self.window,text=(message+self.TOURNAMENT_NAME), font=("Arial", 40), bg="#2f435e", fg="#ececec").pack()

        """ Outer Frame """
        Outer_Frame = Frame(self.window,bd=4, bg=background_color2)
        Outer_Frame.place(x=10,y=70,width=1500,height=380)

        """ Match Frame """
        # Match_Frame = Frame(Outer_Frame,bd=4, bg="yellow")
        # Match_Frame.place(x=20,y=100,width=1500,height=305)

        """ Match_lable """
        lbl_fMatch = Label(Outer_Frame, text="First Match", bg=background_color2,fg=background_color,font=("lato",20,"bold"))
        lbl_fMatch.grid(row=0, column=0, pady=10, padx=70, sticky="N")
        lbl_sMatch = Label(Outer_Frame, text="Second Match", bg="blue",fg="white",font=("lato",20,"bold"))
        lbl_sMatch.grid(row=0, column=1, pady=10, padx=70, sticky="n")
        lbl_tMatch = Label(Outer_Frame, text="Third Match", bg="blue",fg="white",font=("lato",20,"bold"))
        lbl_tMatch.grid(row=0, column=2, pady=10, padx=70, sticky="N")
        lbl_foMatch = Label(Outer_Frame, text="Fourth Match", bg="blue",fg="white",font=("lato",20,"bold"))
        lbl_foMatch.grid(row=0, column=3, pady=10, padx=70, sticky="N")

        # VS_Frame = Frame(Outer_Frame,bd=4, bg="green")
        # VS_Frame.place(x=0,y=50,width=300,height=350)

        """------------------------------ Controller things for players matchs -------------------------------------"""

        
        """ Diviser la liste en 2 groupe."""
        # dico1 = dict(players.items()[len(players)//2:])
        # dico2 = dict(players.items()[:len(players)//2])

        # # Code initial
        # middle_index = (len(players.items())//2)
        # round1_A = list(players.items())[:middle_index]
        # round1_B = list(players.items())[middle_index:]

        middle_index = ((self.NBR_PLAYERS)//2)
        players= self.PLAYERS_DATA
        round1_A = list(players.items())[:middle_index]
        round1_B = list(players.items())[middle_index:]
            
        """ Classement des joueurs par leur classement."""
        # round1_ready = sorted(players.items(), key=lambda p: p[0][1])
            
        # print(round1_ready)

        # """ Diviser la liste en 2 groupe."""
        # middle_index = (len(round1_ready)//2)
        # round1_A = round1_ready[:middle_index]
        # round1_B = round1_ready[middle_index:]


        #============================== Loop sur joueurs du round1_A / round1_B =====================

        joueur1= round1_A[0][1]
        joueur2= round1_A[1][1]
        joueur3= round1_A[2][1]
        joueur4= round1_A[3][1]

        round1_A= [joueur1,joueur2, joueur3,joueur4]

        joueur5= round1_B[0][1]
        joueur6= round1_B[1][1]
        joueur7= round1_B[2][1]
        joueur8= round1_B[3][1]

        round1_B= [joueur5,joueur6, joueur7,joueur8]

        print(round1_A)
        print(round1_B)

        #joueur1=round1_A[0][1]
        #print(joueur4)
        # print(joueur1["lname"])
        # for index in enumerate(round1_A):
    
        #print(joueur3["lname"])
        
        #============================Fin Loop sur joueurs du round1_A / round1_B =====================

        """ Afficher les matches."""
       # print("For the {0} Tournament. It begin {1} to {2} in the afternoon. With {3} players.\n And the match are: ".format(T_name, T_begin, T_end, T_contender))
        # for indice_objet, valeur_objet in enumerate(round1_A):
        #     print(valeur_objet[0][1])
        #     print(indice_objet)
        #     pass
            #print("Le match opposera {} N°{} au classement VS {} N°{} au classement"
            #.format(valeur_objet[0][1].fname, valeur_objet[0][1].rang,round1_B[indice_objet][0][1].fname, round1_B[indice_objet][0][1].rang))
        """Fin Round 1 """


        """----------------------------- END Controller things for players matchs ----------------------------------"""
        validateA = [StringVar() for _ in range(4)]
        validateB = [StringVar() for _ in range(4)]

        match_result = ('Win','Equals','Lose') # List of result of the match

        for index, joueurN in enumerate(round1_A):

            dbjoueurNTestA.insert({(index+1):joueurN})

            print(joueurN)

            VS_Frame = Frame(Outer_Frame, bg="green")
            VS_Frame.grid(row=0, column=(index), pady=40,padx=30)

            # VS_Frame.place(x=0,y=50,width=300,height=350)

            """ Afficher joueur1 des matches."""
            # for joueurA in round1_A:
            lbl_player1 = Label(VS_Frame, text=joueurN["fname"]+" "+joueurN["lname"], bg="black",fg="white",font=("lato",18,"bold"))
            lbl_player1.grid(row=0, column=(index), pady=5,padx=30,sticky="N" )

            combo_player1 = ttk.Combobox(VS_Frame,
            textvariable=validateA[index],
            font=("lato",13,"bold"),width=15, state='normal')
            combo_player1['values'] = match_result
            combo_player1.grid(row=1, column=(index), pady=5, padx= 0)

            lbl_VS = Label(VS_Frame, text="VS", bg="blue",fg="black",font=("lato",25,"bold"))
            lbl_VS.grid(row=2, column=(index))

        for index, joueurN in enumerate(round1_B):

            dbjoueurNTestB.insert({(index+1): joueurN})

            VS_Frame = Frame(Outer_Frame, bg="purple")
            VS_Frame.grid(row=1, column=(index), pady=0,padx=50, sticky="S")

            combo_player2 = ttk.Combobox(VS_Frame,
            textvariable=validateB[index], 
            font=("lato",13,"bold"),width=15, justify="center", state='normal')
            combo_player2['values'] = match_result
            combo_player2.grid(row=1, column=(index), pady=10, padx= 0)

            lbl_player2 = Label(VS_Frame, text=joueurN["fname"]+" "+joueurN["lname"], bg="white",fg="black",font=("lato",18,"bold"))
            lbl_player2.grid(row=0, column=(index), pady=5,padx=30)

            print(validateA)
        
        # if validateA['values']=='Win':
        #     validateB['values'] == 'Lose'
        # elif validateA['values']=='Equal':
        #     validateB['values'] == 'Equal'
        # elif validateA['values']=='Lose':
        #     validateB['values'] == 'Win'

       
   


        
        # combo_player1.bind('<<ComboboxSelected>>', validate_combo)
        # combo_player2.bind('<<ComboboxSelected>>', validate_combo)
        
        """ Btn First Frame"""
        BtnF_Frame = Frame(Outer_Frame,relief=RIDGE, bg=background_color2)
        BtnF_Frame.place(x=0,y=315,width=1500,height=50)

        validate_btn = Button(BtnF_Frame,text="Valider", width="20",command=self.validate_combo,pady=5).grid(row=0, column=9, padx=10,pady=10)
        reset_btn = Button(BtnF_Frame,text="Reset", width="15",pady=5).grid(row=0, column=0, padx=10,pady=10)

        lbl_obs = Label(BtnF_Frame, text="Votre observation : ",bg= background_color2,font=("lato",15)).grid(row=0 ,column=1)
        observation_box = Entry(BtnF_Frame, width="115",text="Ajouter votre observation", textvariable = "#observation")
        observation_box.grid(row=0 ,column=2, columnspan=5)
        
        #def validate_combo(self):
            #print("OKKKKKK")
    def validate_combo(self):

        #dbTournamentTest3.insert({'equipe_A':round1_A})
        print("Fonction OK")

        # for i in range(4):

        #     if validateA.get()== "Jan":
        #         dbTournamentTest3.insert({'point ': 1 })
        #     elif validateA.get() == "Feb":
        #         dbTournamentTest3.insert({'point ': .5 })
        #     elif validateA.get() == "Lose":
        #         dbTournamentTest3.insert({'point': 0 })

            #dbTournamentTest.insert({'point :':(validateA.get())})

            # result=validateA.get()
            # if result=='Win':
            #     point= 1
            # elif result=='Equal':
            #     point = 0.5
            # elif result=='Lose':
            #     point = 0

        #dbTournamentTest2.insert({"equipe_B:":round1_B})
        # for i in range(4):

        #     if validateB.get()== "Jan":
        #         dbTournamentTest3.insert({'point ': 1 })
        #     elif validateB.get() == "Feb":
        #         dbTournamentTest3.insert({'point ': .5 })
        #     elif validateB.get() == "Lose":
        #         dbTournamentTest3.insert({'point': 0 })
            
        #messagebox.showinfo("success","Vos infos ont été enregistrés avec SUCCESS")

        ''' -------------------------------------- Second Frame ------------------------------------  '''
        """ Btn Second Frame"""
        BtnS_Frame = Frame(self.window,bd=4,relief=RIDGE, bg=background_color3)
        BtnS_Frame.place(x=10,y=450,width=1500,height=70)

        lbl_rang = Label(BtnS_Frame, text="Liste par :", bg="black",fg="white",font=("lato",20,"bold"))
        lbl_rang.grid(row=0, column=0, pady=10,padx=20,sticky="w")

        combo_rang = ttk.Combobox(BtnS_Frame,textvariable="self.sort_by", font=("lato",13,"bold"),width=10, state='readonly')
        combo_rang['values'] = ('Classement','Nom','Prénom')
        combo_rang.grid(row=0, column=1, pady=10, padx= 20)

        txt_search = Entry(BtnS_Frame,textvariable="self.set_by",font=("lato",10,"bold"),width=20,bd=5,relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx= 20, sticky="w")

        sort_btn = Button(BtnS_Frame,text="Classer", width="15",pady=5).grid(row=0, column=3, padx=10,pady=10)
        setAll_btn = Button(BtnS_Frame,text="Modifier", width="15",pady=5).grid(row=0, column=4, padx=10,pady=10)
       
        """ Second Frame """
        Second_Frame = Frame(self.window,bd=4, bg=background_color3)
        Second_Frame.place(x=10,y=510,width=1500,height=300)

        """ Scroll Bar """
        scroll_x = Scrollbar(Second_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Second_Frame,orient=VERTICAL)

        self.Players_table = ttk.Treeview(Second_Frame,column=("rang","fname", "lname","DBirth", "gender","points"), xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Players_table.xview)
        scroll_y.config(command=self.Players_table.yview)

        self.Players_table.heading("fname", text="Prénom")
        self.Players_table.heading("lname", text="Nom")
        self.Players_table.heading("DBirth", text="D Naissancé")
        self.Players_table.heading("gender", text="Genre")
        self.Players_table.heading("points", text="Points")
        self.Players_table.heading("rang", text="Classement")

        self.Players_table['show']='headings'
        self.Players_table.column("fname", width=100)
        self.Players_table.column("lname", width=100)
        self.Players_table.column("DBirth", width=100)
        self.Players_table.column("gender", width=100)
        self.Players_table.column("points", width=100)
        self.Players_table.column("rang", width=100)

        self.Players_table.pack(fill=BOTH, expand=1)

       # print(self.PLAYERS_DATA1['fname'])
        #========================================== Code à factoriser avec une LOOP =========================================
        ##    "self" + variable qui ne le conserne pas ne font pas bon menage.
        #self.Players_table.insert(parent='', index=0,iid=0, text='', values=((self.PLAYERS_DATA1['fname']),(self.PLAYERS_DATA1['lname']), (self.PLAYERS_DATA1['DBirth']), (self.PLAYERS_DATA1['gender']), (self.PLAYERS_DATA1['rang'])))
         # values=('1','Vineet','Alpha', '2001','male','2'))
        #PlayersDataList=['PLAYERS_DATA1','PLAYERS_DATA2','PLAYERS_DATA3','PLAYERS_DATA4','PLAYERS_DATA5','PLAYERS_DATA6','PLAYERS_DATA7','PLAYERS_DATA8']
        
        # for i,p in enumerate(self.NBR_PLAYERS):
        #     print(p)
            # self.Players_table.insert(parent='', index=[i],iid=[i], text='', values=(
            # (self.PLAYERS_DATA1['rang']),
            # (self.PLAYERS_DATA1['fname']),
            # (self.PLAYERS_DATA2['lname']),
            # (self.PLAYERS_DATA2['DBirth']),
            # (self.PLAYERS_DATA1['gender']),
            # ))
        self.Players_table.insert(parent='', index=1,iid=1, text='', values=(
            (self.PLAYERS_DATA1['rang']),
            (self.PLAYERS_DATA1['fname']),
            (self.PLAYERS_DATA1['lname']),
            (self.PLAYERS_DATA1['DBirth']),
            (self.PLAYERS_DATA1['gender']),
        ))
        self.Players_table.insert(parent='', index=2,iid=2, text='', values=(
            (self.PLAYERS_DATA2['rang']),
            (self.PLAYERS_DATA2['fname']),
            (self.PLAYERS_DATA2['lname']),
            (self.PLAYERS_DATA2['DBirth']),
            (self.PLAYERS_DATA2['gender']),
            ))
        self.Players_table.insert(parent='', index=3,iid=3, text='', values=(
            (self.PLAYERS_DATA3['rang']),
            (self.PLAYERS_DATA3['fname']),
            (self.PLAYERS_DATA3['lname']),
            (self.PLAYERS_DATA3['DBirth']),
            (self.PLAYERS_DATA3['gender']),
        ))
        self.Players_table.insert(parent='', index=4,iid=4, text='', values=(
             (self.PLAYERS_DATA4['rang']),
            (self.PLAYERS_DATA4['fname']),
            (self.PLAYERS_DATA4['lname']),
            (self.PLAYERS_DATA4['DBirth']),
            (self.PLAYERS_DATA4['gender']),
            ))
        self.Players_table.insert(parent='', index=5,iid=5, text='', values=(
            (self.PLAYERS_DATA5['rang']),
            (self.PLAYERS_DATA5['fname']),
            (self.PLAYERS_DATA5['lname']),
            (self.PLAYERS_DATA5['DBirth']),
            (self.PLAYERS_DATA5['gender']),
        ))
        self.Players_table.insert(parent='', index=6,iid=6, text='', values=(
             (self.PLAYERS_DATA6['rang']),
            (self.PLAYERS_DATA6['fname']),
            (self.PLAYERS_DATA6['lname']),
            (self.PLAYERS_DATA6['DBirth']),
            (self.PLAYERS_DATA6['gender']),
            ))
        self.Players_table.insert(parent='', index=7,iid=7, text='', values=(
            (self.PLAYERS_DATA7['rang']),
            (self.PLAYERS_DATA7['fname']),
            (self.PLAYERS_DATA7['lname']),
            (self.PLAYERS_DATA7['DBirth']),
            (self.PLAYERS_DATA7['gender']),
        ))
        self.Players_table.insert(parent='', index=8,iid=8, text='', values=(
             (self.PLAYERS_DATA8['rang']),
            (self.PLAYERS_DATA8['fname']),
            (self.PLAYERS_DATA8['lname']),
            (self.PLAYERS_DATA8['DBirth']),
            (self.PLAYERS_DATA8['gender']),
            ))
        # self.Players_table.insert(parent='', index=3,iid=3, text='', values=('4','Vimal','Delta', '2001','male','2'))
        # self.Players_table.insert(parent='', index=4,iid=4, text='', values=('1','Vineet','Alpha', '2001','male','2'))
        # self.Players_table.insert(parent='', index=5,iid=5, text='', values=('2','Anil','Bravo', '2001','male','2'))
        # self.Players_table.insert(parent='', index=6,iid=6, text='', values=('3','Vinod','Charlie', '2001','male','2'))
        # self.Players_table.insert(parent='', index=7,iid=7, text='', values=('4','Vimal','Delta', '2001','male','2'))

        self.Players_table.pack()


        #self.Players_table.bind(self.get_players)


    #def get_players(self, PLAYERS_DATA):
        # for index, item in enumerate(PLAYERS_DATA):
        #print(self.PLAYERS_DATA)
            #self.Players_table.insert(parent='', index=0,iid=0, text='', values=('1','Vineet','Alpha', '2001','male','2'))
        # # curosor_row = self.Players_table.focus()
        # # contents = self.Players_data.set_children(curosor_row)
        # # row = contents['values']
        # # self.fname_var.set(row[0])
        # # self.lname_var.set(row[1])
        # # self.DBirth_var.set(row[2])
        # # self.gender_var.set(row[3])
        # # self.rang_No_var.set(row[4])



        self.window.mainloop()
        pass


def Initialisation():
    window = Tk()
    Initialisation = Big_window(window,"Round 1 ","1500x900+50+50","#2f435e","1ere Round ")
    #window.mainloop()

    """ Round Frame """
    #### Ne fonctionne pas ici
    # Round_Frame = Frame(window,bd=4,relief=RIDGE, bg="blue")
    # Round_Frame.place(x=20,y=100,width=570,height=485)

    # Round_Frame()


Initialisation() #(window,"Initialisation du tournoi","1500x900+50+50","#2f435e","1ere Round du Tournoi")