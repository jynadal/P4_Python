from tkinter import *
import tkinter as tk
from tkinter import ttk
import simplejson as json
from tinydb import TinyDB, Query
dbTournaR2 = TinyDB('dbTournRound2ClassTest.json')
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
    with open ('dbRound2_P_list.json','r') as mylist:
        data=mylist.read()

        R2_players = json.loads(data)
        #print(R2_players["_default"])
        #Players_data = R2_players["_default"]
    """ END Add json file for name ..."""


    PLAYERS_WIN = [ d for d in R2_players if d['points'] > 0 ]
    PLAYERS_LOSE = [ d for d in R2_players if d['points'] == 0 ]
    NBR_PLAYERS_WIN = len(PLAYERS_WIN)
    PLAYERS_SELECT = R2_players
    TOURNAMENT_NAME = objs["_default"][str(last_T)]["name"]
    BEGIN = str(objs["_default"][str(last_T)]["T_Begin"])
    END =  objs["_default"][str(last_T)]["T_End"]
    PLAYERS_DATA = R2_players
    variables = ["fname_var","lname_var","DBirth_var","gender_var","rang_No_var"]
    width = "1400"
    height = "200" 

    print(R2_players[0])

    # for index, player in enumerate(PLAYERS_DATA):
    #     #print("{} => {}".format([index],player))
    #     PLAYERS_DATA+[index] = player[index] ????????????


    # for player1 key, value in R2_players["_default"]['1']:
    #     print(player1)
    # #========================================== Code à factoriser avec une LOOP =========================================
    PLAYERS_DATA1 = R2_players[0]
    PLAYERS_DATA2 = R2_players[1]
    PLAYERS_DATA3 = R2_players[2]
    PLAYERS_DATA4 = R2_players[3]
    PLAYERS_DATA5 = R2_players[4]
    PLAYERS_DATA6 = R2_players[5]
    PLAYERS_DATA7 = R2_players[6]
    PLAYERS_DATA8 = R2_players[7]

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
        Outer_Frame = Frame(window,bd=4, bg=background_color2)
        Outer_Frame.place(x=10,y=70,width=1500,height=380)

        """ Match Frame """
        # Match_Frame = Frame(Outer_Frame,bd=4, bg="yellow")
        # Match_Frame.place(x=20,y=100,width=1500,height=305)

        """ Match_lable """
        lbl_fMatch = Label(Outer_Frame, text="First Match", bg=background_color2,fg=background_color,font=("lato",20,"bold"))
        lbl_fMatch.grid(row=0, column=0, pady=10, padx=170, sticky="N")
        lbl_sMatch = Label(Outer_Frame, text="Second Match", bg="blue",fg="white",font=("lato",20,"bold"))
        lbl_sMatch.grid(row=0, column=2, pady=10, padx=170, sticky="n")
        lbl_tMatch = Label(Outer_Frame, text="Third Match", bg="blue",fg="white",font=("lato",20,"bold"))
        lbl_tMatch.grid(row=0, column=4, pady=10, padx=170, sticky="N")

        # VS_Frame = Frame(Outer_Frame,bd=4, bg="green")
        # VS_Frame.place(x=0,y=50,width=300,height=350)

    #     """------------------------------ Controller things for players matchs -------------------------------------"""

        
    #     """ Diviser la liste en 2 groupes WIN et LOSE """
        if (self.NBR_PLAYERS_WIN % 2) != 0:
            self.NBR_PLAYERS_WIN += 1
        print(self.NBR_PLAYERS_WIN)

        PLAYERS_SELECT = self.R2_players[:self.NBR_PLAYERS_WIN]
        #PLAYERS_NONSELECT = list(self.R2_players.items())[self.NBR_PLAYERS_WIN:]

        print(PLAYERS_SELECT)

    #     """----------------------------- END Controller things for players matchs ----------------------------------"""

        for index, joueurN in enumerate(PLAYERS_SELECT):

            if (index%2 == 0):
                print(joueurN)

                VS_Frame = Frame(Outer_Frame, bg="green")
                VS_Frame.grid(row=0, column=(index), pady=40,padx=30)

                # VS_Frame.place(x=0,y=50,width=300,height=350)

                """ Afficher joueur1 des matches."""
                # for joueurA in round1_A:
                lbl_player1 = Label(VS_Frame, text=joueurN["fname"]+" "+joueurN["lname"], bg="black",fg="white",font=("lato",18,"bold"))
                lbl_player1.grid(row=0, column=(index), pady=5,padx=30,sticky="N" )

                combo_player1 = ttk.Combobox(VS_Frame,
                # textvariable=self.search_by, 
                font=("lato",13,"bold"),width=15, state='readonly')
                combo_player1['values'] = ('Win','Equals','Lose')
                combo_player1.grid(row=1, column=(index), pady=5, padx= 0)

                lbl_VS = Label(VS_Frame, text="VS", bg="blue",fg="black",font=("lato",25,"bold"))
                lbl_VS.grid(row=2, column=(index))

            else:

                VS_Frame = Frame(Outer_Frame, bg="purple")
                VS_Frame.grid(row=1, column=((index)-1), pady=0,padx=50, sticky="S")

                combo_player2 = ttk.Combobox(VS_Frame,
                # textvariable=self.search_by, 
                font=("lato",13,"bold"),width=15, justify="center", state='readonly')
                combo_player2['values'] = ('Win','Equals','Lose')
                combo_player2.grid(row=1, column=((index)-1), pady=10, padx= 0)

                lbl_player2 = Label(VS_Frame, text=joueurN["fname"]+" "+joueurN["lname"], bg="white",fg="black",font=("lato",18,"bold"))
                lbl_player2.grid(row=0, column=((index)-1), pady=5,padx=30)
        
        """ Btn First Frame"""
        BtnF_Frame = Frame(Outer_Frame,relief=RIDGE, bg=background_color2)
        BtnF_Frame.place(x=0,y=315,width=1500,height=50)

        validate_btn = Button(BtnF_Frame,text="Valider", width="20",pady=5).grid(row=0, column=9, padx=10,pady=10)
        reset_btn = Button(BtnF_Frame,text="Reset", width="15",pady=5).grid(row=0, column=0, padx=10,pady=10)

        lbl_obs = Label(BtnF_Frame, text="Votre observation : ",bg= background_color2,font=("lato",15)).grid(row=0 ,column=1)
        observation_box = Entry(BtnF_Frame, width="115",text="Ajouter votre observation", textvariable = "#observation")
        observation_box.grid(row=0 ,column=2, columnspan=5)



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
        Second_Frame = Frame(window,bd=4, bg=background_color3)
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
        
        # for index, playerR2 in enumerate(self.PLAYERS_DATA):   NE FONCTIONNE PAS MAIS J'Y ETAIS PRESQUE
        #     #print(playerR2, index)
        #     self.Players_table.insert(parent='', index=[index],iid=[index], text='', values=(
        #     (playerR2(index)['rang']),
        #     (playerR2+index['fname']),
        #     (playerR2+index['lname']),
        #     (playerR2+index['DBirth']),
        #     (playerR2+index['gender']),
        #     ))


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
            (self.PLAYERS_DATA1['points']),
        ))
        self.Players_table.insert(parent='', index=2,iid=2, text='', values=(
             (self.PLAYERS_DATA2['rang']),
            (self.PLAYERS_DATA2['fname']),
            (self.PLAYERS_DATA2['lname']),
            (self.PLAYERS_DATA2['DBirth']),
            (self.PLAYERS_DATA2['gender']),
            (self.PLAYERS_DATA2['points']),
            ))
        self.Players_table.insert(parent='', index=3,iid=3, text='', values=(
            (self.PLAYERS_DATA3['rang']),
            (self.PLAYERS_DATA3['fname']),
            (self.PLAYERS_DATA3['lname']),
            (self.PLAYERS_DATA3['DBirth']),
            (self.PLAYERS_DATA3['gender']),
            (self.PLAYERS_DATA3['points']),
        ))
        self.Players_table.insert(parent='', index=4,iid=4, text='', values=(
             (self.PLAYERS_DATA4['rang']),
            (self.PLAYERS_DATA4['fname']),
            (self.PLAYERS_DATA4['lname']),
            (self.PLAYERS_DATA4['DBirth']),
            (self.PLAYERS_DATA4['gender']),
            (self.PLAYERS_DATA4['points']),
            ))
        self.Players_table.insert(parent='', index=5,iid=5, text='', values=(
            (self.PLAYERS_DATA5['rang']),
            (self.PLAYERS_DATA5['fname']),
            (self.PLAYERS_DATA5['lname']),
            (self.PLAYERS_DATA5['DBirth']),
            (self.PLAYERS_DATA5['gender']),
            (self.PLAYERS_DATA5['points']),
        ))
        self.Players_table.insert(parent='', index=6,iid=6, text='', values=(
             (self.PLAYERS_DATA6['rang']),
            (self.PLAYERS_DATA6['fname']),
            (self.PLAYERS_DATA6['lname']),
            (self.PLAYERS_DATA6['DBirth']),
            (self.PLAYERS_DATA6['gender']),
            (self.PLAYERS_DATA6['points']),
            ))
        self.Players_table.insert(parent='', index=7,iid=7, text='', values=(
            (self.PLAYERS_DATA7['rang']),
            (self.PLAYERS_DATA7['fname']),
            (self.PLAYERS_DATA7['lname']),
            (self.PLAYERS_DATA7['DBirth']),
            (self.PLAYERS_DATA7['gender']),
            (self.PLAYERS_DATA7['points']),
        ))
        self.Players_table.insert(parent='', index=8,iid=8, text='', values=(
             (self.PLAYERS_DATA8['rang']),
            (self.PLAYERS_DATA8['fname']),
            (self.PLAYERS_DATA8['lname']),
            (self.PLAYERS_DATA8['DBirth']),
            (self.PLAYERS_DATA8['gender']),
            (self.PLAYERS_DATA8['points']),
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
    Initialisation = Big_window(window,"Round 2","1500x900+50+50","#2f435e","2éme Round ")
    #window.mainloop()

    """ Round Frame """
    #### Ne fonctionne pas ici
    # Round_Frame = Frame(window,bd=4,relief=RIDGE, bg="blue")
    # Round_Frame.place(x=20,y=100,width=570,height=485)

    # Round_Frame()


Initialisation() #(window,"Initialisation du tournoi","1500x900+50+50","#2f435e","1ere Round du Tournoi")