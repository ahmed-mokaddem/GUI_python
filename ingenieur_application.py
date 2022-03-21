from cProfile import label
from logging.config import valid_ident

from pydoc import text
from random import shuffle
from select import select
from sre_parse import CATEGORIES
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from turtle import color, left, onclick, right
import connection





class Application(Tk):
    def __init__(self):
        super().__init__()
        self.create_widget()

    def  affiche1(self,event):
        messagebox.showinfo("le code",self.cat.get())

    def affiche(self):
        print(self.c_ing_val.get())
        messagebox.showinfo("le code",self.c_ing_val.get())
        print(self.lb.curselection())
        print(self.lb.get(3))
 



    def create_ing(self):
        
        self.ajout=Toplevel(app)
        self.ajout.geometry("600x400")
        self.c_ing=Label(self.ajout,text="code de l'ingénieur")  
        self.c_ing_val=Entry(self.ajout,show="*")          
        self.nom_ing=Label(self.ajout,text="Nom de l'ingénieur") 
        self.nom_val=Entry(self.ajout)           
        self.prenom_ing=Label(self.ajout,text="prenom de l'ingénieur") 
        self.prenom_val=Entry(self.ajout)       
        self.specialite=Label(self.ajout,text="choisir specilaité")
        self.spec_val=Entry(self.ajout)          
        self.salaire=Label(self.ajout,text="Ajouter salaire")
        self.salair=Spinbox(self.ajout, from_=50.00, to=200.00)      
        self.catégorie=Label(self.ajout,text="choisir categorie")
        self.cat_val=Entry(self.ajout)
        # listebox  
        self.lb=Listbox(self.ajout, selectmode=MULTIPLE)
        self.lb.insert(1,"ingénieur")
        self.lb.insert(1,"architecte")
        self.lb.insert(2,"analyste")
        print(self.lb.curselection())
        self.lb.pack()
        # combobox
        self.cat=Combobox(self.ajout,values=["ingénieur","architecte","analyste"])
        self.cat.current(0) # la valeur à afficher au début 
        # afficher la valeur sélectioné 
        self.cat.bind("<<ComboboxSelected>>", self.affiche1)
            

            
        self.add=Button(self.ajout,text="Ajouter",command=self.affiche)
        self.annuler=Button(self.ajout,text="Annuler")
        self.c_ing.place(x=5, y=5, width=160, height=25)
        self.c_ing_val.place(x=150, y=5, width=160, height=25)

        self.nom_ing.place(x=5, y=55, width=160, height=25)
        self.nom_val.place(x=150, y=55, width=160, height=25)

        self.prenom_ing.place(x=5, y=110, width=160, height=25)
        self.prenom_val.place(x=150, y=110, width=160, height=25)

        self.specialite.place(x=5, y=160, width=160, height=25)
        self.spec_val.place(x=150, y=160, width=160, height=25)

        self.salaire.place(x=5, y=200, width=160, height=25)
        self.salair.place(x=150, y=200)#, width=160, height=25)

        self.catégorie.place(x=5, y=250, width=160, height=25)
        self.cat.place(x=150, y=250)

        self.add.place(x=300,y=350, width=100, height=25)
        self.annuler.place(x=400,y=350, width=100, height=25)
        
        self.ajout.mainloop()


    def create_widget(self):
        self.mon_menu=Menu(self)
        # Menu Ingenieur
        self.ing=Menu(self.mon_menu,tearoff=0)
        self.ing.add_command(label="Ajout_ingenieur",command=self.create_ing)
        self.ing.add_command(label="recherche_ingenieur")
        self.ing.add_command(label="Ajout Compétences")
        self.ing.add_command(label="Quitter")
        #menu Foromation
        self.format=Menu(self.mon_menu,tearoff=0)
        self.format.add_command(label="Ajout_format" )
        self.format.add_command(label="recherche_format")
        self.config(menu=self.mon_menu)
        # Attacher les menus 
        self.mon_menu.add_cascade(label="Ingenieur",menu=self.ing)
        self.mon_menu.add_cascade(label="Formation",menu=self.format)

     


    
   


# Fenêtre 
app=Application()
app.title("Société")
app.geometry('600x400')
app.iconbitmap()
app.configure(bg="#5361ad")


app.mainloop()
