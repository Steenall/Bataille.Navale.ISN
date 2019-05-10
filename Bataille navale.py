#coding:utf-8
from tkinter import *
from math import *
from random import *
casejoueur = []
casejoueur2 = []
caseia = []
torpille = []
torpilleia = []
liste_ordi=[]
plancement = 0
bateau = 1
tempvar = 0
base_torpilleur = 0
base_sous_marin = 0
name = ""
base_contre_torpilleur = 0
base_croiseur = 0
fullscreenvar = 0
base_porte_avions = 0
touche = 0
toucheia = 0
liste_rectangle= []
ernord = 0
ersud = 0
erest = 0
erouest = 0
lbat = 0
lancement = 0
direction = 2
#liste
def fullscreen():
    global fullscreenvar
    if fullscreenvar ==0:
        jeu.attributes("-fullscreen", 1)
        fullscreenvar = 1
    elif fullscreenvar == 1:
        jeu.attributes("-fullscreen", 0)
        fullscreenvar = 0
        
def nord():
    global direction
    global casex
    global casey
    global placement_1
    global lbat
    global placement_2
    global placement_3
    global placement_4
    global placement_5
    global tempvar
    global base_torpilleur
    global base_sous_marin
    global liste_rectangle
    global base_contre_torpilleur
    global base_croiseur
    global base_porte_avions
    global ernord
    if bateau == 1:
        if placement_1 == 1:
            for i in range(lbat):
                if base_torpilleur-10*i in casejoueur:
                    print("erreur nord")
                    ernord = 1
            lbat = 2
            name="torpilleur"
            casey= floor(((base_torpilleur+10)/10)+1)
            casex= floor((base_torpilleur+10)-(casey-1)*10)
    if bateau == 2:
        if placement_2 == 1:
            for i in range(lbat):
                if base_sous_marin-10*i in casejoueur:
                    print("erreur nord")
                    ernord = 1
            lbat = 3
            name="sous_marin"
            casey= floor(((base_sous_marin+10)/10)+1)
            casex= floor((base_sous_marin+10)-(casey-1)*10)
    if bateau == 3:
        if placement_3 == 1:
            for i in range(lbat):
                if base_contre_torpilleur-10*i in casejoueur:
                    print("erreur nord")
                    ernord = 1
            lbat = 3
            name="contre_torpilleur"
            casey= floor(((base_contre_torpilleur+10)/10)+1)
            casex= floor((base_contre_torpilleur+10)-(casey-1)*10)
    if bateau == 4:
        if placement_4 == 1:
            for i in range(lbat):
                if base_croiseur-10*i in casejoueur:
                    print("erreur nord")
                    ernord = 1
            lbat = 4
            name = "croiseur"
            casey= floor(((base_croiseur+10)/10)+1)
            casex= floor((base_croiseur+10)-(casey-1)*10)
    if bateau == 5:
        if placement_5 == 1:
            for i in range(lbat):
                if base_porte_avions-10*i in casejoueur:
                    print("erreur nord")
                    ernord = 1
            lbat = 5
            name="porte_avions"
            casey= floor(((base_porte_avions+10)/10)+1)
            casex= floor((base_porte_avions+10)-(casey-1)*10)
    if casex == 0:
        casex = 10
    if ernord == 1 or casey <= 1*lbat-1:
        txt.insert(END, "Le bateau ne peut pas être orienté vers le nord")
    else:
        if direction == 2:
            for i in range(lbat):
                c1.delete(name)
                if bateau == 1:
                    casejoueur.remove(base_torpilleur+10-i)
                if bateau == 2:
                    casejoueur.remove(base_sous_marin+10-i)
                if bateau == 3:
                    casejoueur.remove(base_contre_torpilleur+10-i)
                if bateau == 4:
                    casejoueur.remove(base_croiseur+10-i)
                if bateau == 5:
                    casejoueur.remove(base_porte_avions+10-i)
        if direction == 3:
            for i in range(lbat):
                c1.delete(name)
                if bateau == 1:
                    casejoueur.remove(base_torpilleur+10+i)
                if bateau == 2:
                    casejoueur.remove(base_sous_marin+10+i)
                if bateau == 3:
                    casejoueur.remove(base_contre_torpilleur+10+i)
                if bateau == 4:
                    casejoueur.remove(base_croiseur+10+i)
                if bateau == 5:
                    casejoueur.remove(base_porte_avions+10+i)
        if direction == 0:
            for i in range(lbat):
                c1.delete(name)
                if bateau == 1:
                    casejoueur.remove(base_torpilleur+10-10*i)
                if bateau == 2:
                    casejoueur.remove(base_sous_marin+10-10*i)
                if bateau == 3:
                    casejoueur.remove(base_contre_torpilleur+10-10*i)
                if bateau == 4:
                    casejoueur.remove(base_croiseur+10-10*i)
                if bateau == 5:
                    casejoueur.remove(base_porte_avions+10-10*i)
        if direction == 1:
            for i in range(lbat):
                c1.delete(name)
                if bateau == 1:
                    casejoueur.remove(base_torpilleur+10+10*i)
                if bateau == 2:
                    casejoueur.remove(base_sous_marin+10+10*i)
                if bateau == 3:
                    casejoueur.remove(base_contre_torpilleur+10+10*i)
                if bateau == 4:
                    casejoueur.remove(base_croiseur+10+10*i)
                if bateau == 5:
                    casejoueur.remove(base_porte_avions+10+10*i)
        for i in range(lbat):
            casejoueur.append(casex + 10*casey+10*i-10)
            c1.create_rectangle((casex)*30+1,(casey-i)*30+1,(casex)*30+29,(casey-i)*30+29,fill='yellow',outline="yellow")
        direction = 0
        
        
def sud():
    global placement
    if placement == 1:
        print("cc")
    direction = 1
def est():
    global placement
    if placement == 1:
        print("cc")
    direction = 2
def ouest():
    global placement
    if placement == 1:
        print("cc")
    direction = 3

def start():
    global lancement
    txt.delete('0.0',END)
    global liste_ordi
    for i in range(17):
        X = randint(10,109)
        liste_ordi.append(X)
        casey = floor(X/10)
        casex = (X-(casey*10-10))
    if len(casejoueur) == 17:
        txt.insert(END, "La partie peut commencer")
        lancement=1
    if len(casejoueur) < 17:
        txt.insert(END, "Vous n'avez pas sélectionné suffisament de cases")
def test():
    print("coucou")
            
def placementbateau(event) :
    global lancement
    global casex
    global liste_rectangle
    global casey
    txt.delete('0.0',END)# on efface l'écriture précédente
    x=float(event.x)/30
    y=float(event.y)/30
    if 24 >= x >=14 or 11 >= x >=1:
         if 11 >= y >= 1:
            casex = floor(x)
            casey = floor(y)
            if casex == 24:
                casex = 23
            if casey == 11:
                casey = 10
            #Affiche la case sélectionné avec un clique en jaune 
            if 24 >= x >= 14:
                if lancement == 1:
                    global touche
                    global toucheia
                    casex2 = casex-13
                    torpille.append(casex2 + 10*casey-10)
                    if (casex2+9)+(casey*10-10) in liste_ordi:
                        c1.create_rectangle(casex*30+1,casey*30+1,casex*30+29,casey*30+29,fill='red',outline="red")
                        touche = touche +1
                    else:
                        c1.create_rectangle(casex*30+1,casey*30+1,casex*30+29,casey*30+29,fill='blue',outline="blue")
                    X = randint(10,109)
                    while X-10 in torpilleia:
                        X = randint(10,109)
                    torpilleia.append(X-10)
                    casey = floor(X/10)
                    casex = (X-(casey*10-10))
                    if (casex+1)+((casey*10)-20) in casejoueur:
                        c1.create_rectangle(casex*30-270+1,casey*30+1,casex*30+29-270,casey*30+29,fill='red',outline="red")
                        toucheia = toucheia + 1
                    else:
                        c1.create_rectangle(casex*30-270+1,casey*30+1,casex*30+29-270,casey*30+29,fill='blue',outline="blue")
            if 11 >= x >= 1:
                global bateau
                global erouest
                global erest
                global ernord
                global ersud
                global lbat
                global placement_1
                global placement_2
                global direction
                global placement_3
                global placement_4
                global placement_5
                global base_torpilleur
                global base_sous_marin
                global base_contre_torpilleur
                global base_croiseur
                global base_porte_avions
                if lancement == 0:
                    if (casex + 10*casey-10) in casejoueur:
                        txt.insert(END, "Erreur, le bateau chevauche un autre bateau. ")
                    else:
                        if bateau == 1:
                            lbat = 2
                            base_torpilleur = casex + 10*casey-10 -10
                            name = "torpilleur"
                        if bateau == 2:
                            lbat = 3
                            base_sous_marin = casex + 10*casey-10 -10
                            name = "sous_marin"
                        if bateau == 3:
                            lbat = 3
                            base_contre_torpilleur = casex + 10*casey-10 -10
                            name = "contre torpilleur"
                        if bateau == 4:
                            lbat = 4
                            base_croiseur = casex + 10*casey-10 -10
                            name = "croiseur"
                        if bateau == 5:
                            lbat= 5
                            base_porte_avions = casex + 10*casey-10 -10
                            name = "porte_avions"
                        erouest = 0
                        erest = 0
                        ernord = 0
                        ersud = 0
                        for i in range(lbat):
                            if casex +10*casey-10-i in casejoueur:
                                print("erreur ouest")
                                erouest = 1
                            if casex +10*casey-10+i in casejoueur:
                                print("erreur est")
                                erest = 1
                            if casex +10*casey-10-10*i in casejoueur:
                                print("erreur nord")
                                ernord = 1
                            if casex +10*casey-10+10*i in casejoueur:
                                print("erreur sud")
                                ersud = 1
                        if (casex + 10*casey-10) in casejoueur:
                            txt.insert(END, "Erreur, le bateau ne peut être positionné  ")
                        elif erouest == 1 or (casex) <= (lbat-1):
                            if erest == 1 or (10-casex) <= (lbat-1):
                                if ernord == 1 or casey-(lbat-1) <= 0:
                                    if ersud == 1 or casey + (lbat-1) >= 10:
                                        txt.insert(END, "Erreur, le bateau chevauche un autre bateau dans chaque orientation ")
                                    else:
                                        direction = 1
                                        for i in range(lbat):
                                            casejoueur.append(casex + 10*casey-10+10*i)
                                            c1.create_rectangle(casex*30+1,(casey+i)*30+1,casex*30+29,(casey+i)*30+29,fill='yellow',outline="yellow", tags=name)
                                        if bateau == 1:
                                            placement_1 = 1
                                        if bateau == 2:
                                            placement_2 = 1
                                        if bateau == 3:
                                            placement_3 = 1
                                        if bateau == 4:
                                            placement_4 = 1
                                        if bateau == 5:
                                            placement_5 = 1
                                else:
                                    direction = 0
                                    for i in range(lbat):
                                        casejoueur.append(casex + 10*casey-10-10*i)
                                        c1.create_rectangle((casex)*30+1,(casey-i)*30+1,(casex)*30+29,(casey-i)*30+29,fill='yellow',outline="yellow", tags=name)
                                    if bateau == 1:
                                        placement_1 = 1
                                    if bateau == 2:
                                        placement_2 = 1
                                    if bateau == 3:
                                        placement_3 = 1
                                    if bateau == 4:
                                        placement_4 = 1
                                    if bateau == 5:
                                        placement_5 = 1
                            else:
                                direction = 3
                                for i in range(lbat):
                                    casejoueur.append(casex + 10*casey-10 +i)
                                    c1.create_rectangle((casex+i)*30+1,casey*30+1,(casex+i)*30+29,casey*30+29,fill='yellow',outline="yellow", tags=name)
                                if bateau == 1:
                                    placement_1 = 1
                                if bateau == 2:
                                    placement_2 = 1
                                if bateau == 3:
                                    placement_3 = 1
                                if bateau == 4:
                                    placement_4 = 1
                                if bateau == 5:
                                    placement_5 = 1
                        else:
                            direction = 2
                            for i in range(lbat):
                                casejoueur.append(casex + 10*casey-10 -i)
                                c1.create_rectangle((casex-i)*30+1,casey*30+1,(casex-i)*30+29,casey*30+29,fill='yellow',outline="yellow", tags=name)
                            if bateau == 1:
                                placement_1 = 1
                            if bateau == 2:
                                placement_2 = 1
                            if bateau == 3:
                                placement_3 = 1
                            if bateau == 4:
                                placement_4 = 1
                            if bateau == 5:
                                placement_5 = 1
         else:
            txt.insert(END, "Erreur, sélection incorrecte")
    else:
        txt.insert(END, "Erreur, sélection incorrecte")
    for i in range(len(torpille)):
            if touche==17:
                txt.insert(END,"Ce n'est pas très folichon")
                fend = Toplevel()
                fend.title('Règles')
                Label(fend, text="Ce n'est pas très folichon").pack(padx=10,pady=10)
                Button(fend, text="Mettre fin à la partie", command=jeu.destroy).pack(side="bottom")
                fend.transient(jeu) 
                fend.grab_set()
                jeu.wait_window(fend)
            elif toucheia == 17:
                txt.insert(END,"Peut mieux faire")
                fend = Toplevel()
                fend.title('Règles')
                Label(fend, text="Peut mieux faire").pack(padx=10,pady=10)
                Button(fend, text="Mettre fin à la partie", command=jeu.destroy).pack(side="bottom")
                fend.transient(jeu) 
                fend.grab_set()
                jeu.wait_window(fInfos)
        

    #Popup Affiche les règles de la bataille navale dans une une autre fenètre quand on clique dessus + restreint l'utilisation de la fenètre principale


def popup():
    fInfos = Toplevel()
    fInfos.title('Règles')
    Label(fInfos, text="La bataille navale est un jeu de société qui se joue à 2\n où le joueur doit placer des navires sur une grille qui n'est pas visible par l'adversiare.\n Chaque tour, le joueur doit essayer de toucher les navires de l'adversaire.\n Le gagant est celui qui a coulé tous les bateaux de l'adversaire").pack(padx=10,pady=10)
    Button(fInfos, text="J'ai compris", command=fInfos.destroy).pack(side="bottom")
        
        #Après le clique sur le bouton ferme la popup et revient sur la fenètre principale 
        
    fInfos.transient(jeu) 
    fInfos.grab_set()
    jeu.wait_window(fInfos)

def loop_bateau():
    global bateau
    bateau = var.get()
    
    
jeu = Tk()					  
jeu.title('Bataille navale')
jeu.geometry('760x650')
#jeu.attributes("-fullscreen", 1)
c1=Canvas(jeu, height=360, width=900, bg="light blue")
c1.bind('<Button-1>',placementbateau)
#Exécute une commande au clic

#Quadrillage 1

#Quadrillage horizontal
b = 30
for i in range(12):
    c1.create_line(30,b*i,330,b*i,fill='black')
    
#Quadrillage vertical
for i in range(12):
    c1.create_line(b*i,30,b*i,330,fill='black')
    
#Quadrillage 2

#Quadrillage horizontal

for i in range(12):
    c1.create_line(420,b*i,720,b*i,fill='black')
    
#Quadrillage vertical
for i in range(11):
    c1.create_line(420+b*i,30,420+b*i,330,fill='black')

#Texte
for i in range(10):
    c1.create_text(45+30*i, 15, text=1*i+1)
    c1.create_text(45+390+30*i, 15, text=1*i+1)
for i in range(2):
    c1.create_text(15+390*i, 45, text="A")
    c1.create_text(15+390*i, 75, text="B")
    c1.create_text(15+390*i, 105, text="C")
    c1.create_text(15+390*i, 135, text="D")
    c1.create_text(15+390*i, 165, text="E")
    c1.create_text(15+390*i, 195, text="F")
    c1.create_text(15+390*i, 225, text="G")
    c1.create_text(15+390*i, 255, text="H")
    c1.create_text(15+390*i, 285, text="I")
    c1.create_text(15+390*i, 315, text="J")
    
c1.pack()
txt=Text (jeu,height=1,bg='light gray')
txt.pack()

#Frame Placement du bateau
Settings = Frame(jeu, borderwidth=2, relief=GROOVE)
Settings.pack(side=LEFT)
Label(Settings, text="Placement du bateau").pack(padx=15)


#Frame 1
Frame1 = Frame(jeu, borderwidth=2, relief=GROOVE)
Frame1.pack(side=RIGHT)
Label(Frame1, text="Menu").pack(padx=5)

regles=Button(Frame1, text='Règles', command=popup).pack(padx=5 ,pady=3) #Affichage de la case "Règles"
launch=Button(Frame1, text='Start', command=start).pack(padx=5 ,pady=3) #Lancer la partie
b=Button(Frame1,text='Plein écran',command=fullscreen).pack(pady=5)
b=Button(Frame1,text='Quitter',command=jeu.destroy).pack(pady=5)  #Quitte le jeu au clique du bouton "Quitter" 


#Frame Orientation
Orientation = Frame(Settings, borderwidth=2, relief=GROOVE)
Orientation.pack(padx=10, side=LEFT)
Label(Orientation, text="Orientation").pack(padx=5)

bn=Button(Orientation,text='Nord',command=nord).pack(ipadx=3, side=TOP)
bs=Button(Orientation,text='Sud',command=sud).pack(pady=2, ipadx=6, side=BOTTOM)
be=Button(Orientation,text='Est',command=est).pack(padx=2, ipadx=6, side=RIGHT)
bw=Button(Orientation,text='Ouest',command=ouest).pack(padx=2, side=LEFT)


#Frame Sélection du bateau
BateauSel= Frame(Settings, borderwidth=2, relief=GROOVE)
BateauSel.pack(padx=50, side=LEFT)
Label(BateauSel, text="Sélection du bateau à placer").pack(padx=15)

var = IntVar()
var.set(1)

R1 = Radiobutton(BateauSel, text="Torpilleur (2 cases)", command=loop_bateau, variable=var, value=1)
R1.pack( anchor = W )
R2 = Radiobutton(BateauSel, text="Sous-marin (3 cases)", command=loop_bateau, variable=var, value=2)
R2.pack( anchor = W )
R3 = Radiobutton(BateauSel, text="Contre-torpilleur (3 cases)", command=loop_bateau, variable=var, value=3)
R3.pack( anchor = W)
R4 = Radiobutton(BateauSel, text="Croiseur (4 cases)", command=loop_bateau, variable=var, value=4)
R4.pack( anchor = W)
R5 = Radiobutton(BateauSel, text="Porte-avions (5 cases)", command=loop_bateau, variable=var, value=5)
R5.pack( anchor = W)

jeu.mainloop()