from tkinter import *
from tkinter import ttk
from tinydb import TinyDB, Query
db = TinyDB('dbTest2.json')
from tkinter import messagebox

class Student():
    def __init__(self,root):
        self.root = root
        self.root.title("Test Tournois TK Inter")
        self.root.geometry("1470x700+0+0")

        title = Label(self.root, text="Test Tournois Echec",bd=9,relief=GROOVE, font=("times new roman",50,"bold"),bg="light grey",fg='blue')
        title.pack(side=TOP,fill=X)

        """ All variable"""
        self.fname_var = StringVar()
        self.lname_var = StringVar()
        self.DBirth_var = StringVar()
        self.gender_var = StringVar()
        self.rang_No_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()        



        """ ManageFrame"""
        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE, bg="blue")
        Manage_Frame.place(x=20,y=100,width=570,height=485)

        m_title = Label(Manage_Frame, text="Inscriptions", bg="white",fg="black",font=("times new roman",40,"bold"))
        m_title.grid(row=0, columnspan=2, pady=10)

        lbl_roll = Label(Manage_Frame, text="Roll No", bg="blue",fg="white",font=("lato",20,"bold"))
        lbl_roll.grid(row=1, column=0, pady=10, padx= 20, sticky="w")
        txt_roll = Entry(Manage_Frame,font=("lato",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=1, column=1, pady=10, padx= 20, sticky="w")

        lbl_fname = Label(Manage_Frame, text="First Name", bg="blue",fg="white",font=("lato",20,"bold"))
        lbl_fname.grid(row=2, column=0, pady=10, padx= 20, sticky="w")
        txt_fname = Entry(Manage_Frame, textvariable=self.fname_var, font=("lato",15,"bold"),bd=5,relief=GROOVE)
        txt_fname.grid(row=2, column=1, pady=10, padx= 20, sticky="w")

        lbl_lname = Label(Manage_Frame, text="Last Name", bg="blue",fg="white",font=("lato",20,"bold"))
        lbl_lname.grid(row=3, column=0, pady=10, padx= 20, sticky="w")
        txt_lname = Entry(Manage_Frame,textvariable=self.lname_var,font=("lato",15,"bold"),bd=5,relief=GROOVE)
        txt_lname.grid(row=3, column=1, pady=10, padx= 20, sticky="w")

        """ dBirth """
        lbl_dBirth = Label(Manage_Frame, text="Date of Birth", bg="blue",fg="white",font=("lato",20,"bold"))
        lbl_dBirth.grid(row=4, column=0, pady=10, padx= 20, sticky="w")
        txt_dBirth = Entry(Manage_Frame,textvariable=self.DBirth_var,font=("lato",15,"bold"),bd=5,relief=GROOVE)
        txt_dBirth.grid(row=4, column=1, pady=10, padx= 20, sticky="w")

        """ Combobox Gender """
        lbl_Gender = Label(Manage_Frame, text="Sexe", bg="blue",fg="white",font=("lato",20,"bold"))
        lbl_Gender.grid(row=5, column=0, pady=10, padx= 20, sticky="w")
        
        combo_gender = ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("lato",13,"bold"),state='readonly')
        combo_gender['values'] = ('male','female','other')
        combo_gender.grid(row=5, column=1, pady=10, padx= 20)

        """ btn frame """
        btn_frame = Frame(Manage_Frame,bd=3,relief=RIDGE, bg="black")
        btn_frame.place(x=10,y= 405,width=530)

        Add_btn = Button(btn_frame,text="Add", width=10, command=self.add_students).grid(row=0, column=0,padx=10, pady=10)
        Update_btn = Button(btn_frame,text="Modifier", width=10).grid(row=0, column=1,padx=10, pady=10)
        Delete_btn = Button(btn_frame,text="Supprimer", width=10).grid(row=0, column=2,padx=10, pady=10)
        clear_btn = Button(btn_frame,text="Reset", width=10).grid(row=0, column=3,padx=10, pady=10)

        """ Details Frame"""
        Details_Frame = Frame(self.root,bd=4,relief=RIDGE, bg="green")
        Details_Frame.place(x=650,y=100,width=880,height=585)

        lbl_search = Label(Details_Frame, text="Recherche", bg="black",fg="white",font=("lato",20,"bold"))
        lbl_search.grid(row=0, column=0, pady=10,padx=20,sticky="w")

        combo_search = ttk.Combobox(Details_Frame,textvariable=self.search_by, font=("lato",13,"bold"),width=10, state='readonly')
        combo_search['values'] = ('Nom','Prenom','Classement')
        combo_search.grid(row=0, column=1, pady=10, padx= 20)

        txt_search = Entry(Details_Frame,textvariable=self.search_txt,font=("lato",10,"bold"),width=20,bd=5,relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx= 20, sticky="w")

        search_btn = Button(Details_Frame,text="Rechercher", width="10",pady=5).grid(row=0, column=3, padx=10,pady=10)
        showAll_btn = Button(Details_Frame,text="Show All", width="10",pady=5).grid(row=0, column=4, padx=10,pady=10)

        """ Table Frame """
        Table_Frame = Frame(Details_Frame,bd=4,relief=RIDGE, bg="crimson")
        Table_Frame.place(x=40,y=70,width=780,height=500)

        scroll_x = Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame,orient=VERTICAL)

        self.Student_table = ttk.Treeview(Table_Frame,column=("fname", "lname","DBirth", "gender","points", "rang"), xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("fname", text="fname")
        self.Student_table.heading("lname", text="lname")
        self.Student_table.heading("DBirth", text="DBirth")
        self.Student_table.heading("gender", text="Gender")
        self.Student_table.heading("points", text="Points")
        self.Student_table.heading("rang", text="Classement")

        self.Student_table['show']='headings'
        self.Student_table.column("fname", width=100)
        self.Student_table.column("lname", width=100)
        self.Student_table.column("DBirth", width=100)
        self.Student_table.column("gender", width=100)
        self.Student_table.column("points", width=100)
        self.Student_table.column("rang", width=100)

        self.Student_table.pack(fill=BOTH, expand=1)

        self.Student_table.insert(parent='', index=0,iid=0, text='', values=('1','Vineet','Alpha', '2001','male','2'))
        self.Student_table.insert(parent='', index=1,iid=1, text='', values=('2','Anil','Bravo', '2001','male','2'))
        self.Student_table.insert(parent='', index=2,iid=2, text='', values=('3','Vinod','Charlie', '2001','male','2'))
        self.Student_table.insert(parent='', index=3,iid=3, text='', values=('4','Vimal','Delta', '2001','male','2'))
        self.Student_table.pack()

        #self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)

    def add_students(self):
        if self.lname_var.get()=="" or self.fname_var.get()=="" or self.DBirth_var.get()=="":
            messagebox.showerror("Error","all fields are required to fill")
        else:
         db.insert({'fname': (self.fname_var.get()), 'lname' : (self.lname_var.get()), 'DBirth':(self.DBirth_var.get()), 'gender': (self.gender_var.get()), 'rang' : (self.rang_No_var.get())
         })

    # def get_cursor(self):
    #     curosor_row = self.Student_table.focus()
    #     contents = self.Student_table.item(curosor_row)
    #     row = contents['values']
    #     self.fname_var.set(row[0])
    #     self.lname_var.set(row[1])
    #     self.DBirth_var.set(row[2])
    #     self.gender_var.set(row[3])
    #     self.rang_No_var.set(row[4])

   

  
    def reset_students(self):
        pass


class Student():
    pass
    root= Tk()
    obj= Student(root)
    root.mainloop()