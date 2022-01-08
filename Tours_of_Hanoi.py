from turtle import *
from copy import deepcopy
from time import *
import datetime

#-----------------------------------------------------------------
#                            Partie A
#-----------------------------------------------------------------
def init(n):
    """reçoit le nombre de disques souhaités par l'utilisateur, puis créer et
    renvoie le plateau dans sa configuration initiale
    Le plateau est une liste contenant les 3 tours, chaque tours est aussi
    une liste"""
    plateau=[[],[],[]]
    for i in range (n):
        plateau[0].append(n-i)
    return plateau

def nombre_disques(plateau,numtour):
    """reçoit le plateau et un numero de tour, puis détérmine et renvoie le
    nombre de disques sur cette tour"""
    return len(plateau[numtour])

def disque_superieur(plateau,numtour):
    """reçoit le plateau et un numero de tour, puis détérmine et renvoie le
    numero du disque supérieur de cette tour (ou -1 si la tour est vide)"""
    if len(plateau[numtour])!=0:
        return plateau[numtour][len(plateau[numtour])-1]
    return -1

def position_disque(plateau,numdisque):
    """reçoit le plateau et un numero de disque, puis trouve la tour sur la
    quelle il est et renvoie le numero de la tour"""
    for i in range (3):
        for j in range (len(plateau[i])):
            if plateau[i][j]==numdisque:
                return i

def verifier_deplacement(plateau,nt1,nt2):
    """reçoit la plateau et deux tours nt1 et nt2 puis indique si on peut
    déplacer le disque supérieur de la tour nt1 vers la tour nt2"""
    if len(plateau[nt1])>0:
        if len(plateau[nt2])==0 or disque_superieur(plateau,nt1)<disque_superieur(plateau,nt2):
            return True
        return False
    return False

def verifier_victoire(plateau,n):
    """Vérifie si le joueur a résolu le problème.
    Il reçoit le plateau et le nombre total de disque, puis créer un nouveau
    plateau correspondant à la position finale en cas de victoire. Il compare
    ensuite les deux plateau et renvoie True s'ils correspondent"""
    final=[[],[],[]]
    for i in range (n):
        final[2].append(n-i)
    if plateau==final:
        return True
    return False

#-----------------------------------------------------------------
#                            Partie B
#-----------------------------------------------------------------
def dessine_plateau(n):
    """reçoit le nombre total de disque et dessine le plateau en adaptant sa
    taille au nombre de disques"""
    bgcolor("black")
    color("orange")
    ht()
    speed(0)
    disque_max=40+(n-1)*30
    tour_tour=disque_max+20
    tour_bord=(disque_max/2)+20
    moitié=(tour_bord+6+tour_tour+6+tour_tour+6+tour_bord)/2
    goto(-moitié,0)
    for j in range (2):
        forward(moitié*2)
        left(90)
        forward(20)
        left(90)
    right(90)
    for i in range (3):
        up()
        goto((-moitié+tour_bord+6)+(i*(tour_tour+6)),20)
        down()
        left(180)
        forward(n*20+30)
        left(90)
        forward(6)
        left(90)
        forward(n*20+30)
        up()
        goto((-moitié+tour_bord+1)+(i*(tour_tour+6)),2)
        down()
        write(i)
        

def dessine_disque(nd,plateau,n):
    """reçoit un numéro de disque, le plateau et le nombre total de disques.
    Il détermine ensuite les coordonnées du disque, sa taille et sa position
    sur le plateau, après quoi il le dessine au bon endroit"""
    disque_max=40+(n-1)*30
    tour_bord=(disque_max/2)+20
    tour_tour=disque_max+20
    moitié=(tour_bord+6+tour_tour+6+tour_tour+6+tour_bord)/2
    numero_tour=position_disque(plateau,nd)
    for i in range (3):
        for j in range (len(plateau[i])):
            if plateau[i][j]==nd:
                numero_etage=j
    diametre_disque=40+(nd-1)*30
    up()
    goto(-moitié+tour_bord+3+(numero_tour*(tour_tour+6)),20+numero_etage*20)
    down()
    left(90)
    forward(diametre_disque/2)
    left(90)
    forward(20)
    left(90)
    forward(diametre_disque)
    left(90)
    forward(20)
    left(90)
    forward((diametre_disque/2)+3)
    left(90)
    forward(1)
    color("black")
    forward(18)
    left(90)
    forward(6)
    left(90)
    forward(19)
    color("orange")
    
def efface_disque(nd,plateau,n):
    """reçoit un numéro de disque, le plateau et le nombre total de disques.
    Il redessine ensuite le disque dans la même couleur que celle de l'arrière
    plan sans toucher au reste pour donner l'impression de l'effacer"""
    color("black")
    disque_max=40+(n-1)*30
    tour_bord=(disque_max/2)+20
    tour_tour=disque_max+20
    moitié=(tour_bord+6+tour_tour+6+tour_tour+6+tour_bord)/2
    numero_tour=position_disque(plateau,nd)
    for i in range (3):
        for j in range (len(plateau[i])):
            if plateau[i][j]==nd:
                numero_etage=j
    diametre_disque=40+(nd-1)*30
    up()
    goto(-moitié+tour_bord+3+(numero_tour*(tour_tour+6)),20+numero_etage*20)
    down()
    left(90)
    up()
    forward(diametre_disque/2)
    left(90)
    forward(1)
    down()
    forward(19)
    left(90)
    forward(diametre_disque)
    left(90)
    forward(20)
    left(90)
    up()
    forward((diametre_disque/2)+3)
    down()
    left(90)
    color("orange")
    forward(21)
    left(90)
    up()
    forward(6)
    down()
    left(90)
    forward(22)

def dessine_config(plateau,n):
    """reçoit le plateau et le nombre total de disques, puis dessine chaque
    disque au bon endroit"""
    for i in range (n):
        dessine_disque(i+1,plateau,n)

def efface_tout(plateau,n):
    """reçoit le plateau et le nombre total de disques, puis efface chaque
    disques sans toucher au plateau"""
    for i in range (n):
        efface_disque(i+1,plateau,n)

#-----------------------------------------------------------------
#                            Partie C
#-----------------------------------------------------------------
def lire_coords(plateau):
    """reçoit le plateau et demande à l'utilisateur de saisir les numéros
    d'une tour de départ et d'une tour d'arrivée, redemande à l'utilisateur
    s'il s'est trompé jusqu'à ce qu'il rentre des valeurs cohérentes"""
    tour_depart=int(input("entrez la tour de départ (0 à 2): "))
    while tour_depart < 0 or tour_depart > 2:
        print("hors de l'intervalle [0,2]")
        tour_depart=int(input("entrez la tour de départ (0 à 2): "))
    while nombre_disques(plateau,tour_depart) == 0:
        print("la tour",tour_depart,"est vide")
        tour_depart=int(input("entrez la tour de départ (0 à 2): "))

    tour_arrivee=int(input("entre la tour d'arrivée (0 à 2): "))
    while tour_arrivee < 0 or tour_arrivee > 2:
        print("hors de l'intervalle [0,2]")
        tour_arrivee=int(input("entrez la tour de d'arrivée (0 à 2): "))
    while verifier_deplacement(plateau,tour_depart,tour_arrivee)==False:
        print("le disque supérieur de la tour",tour_depart,"est plus grand")
        print("que le disque supérieur de la tour",tour_arrivee)
        tour_depart=int(input("entrez la tour de départ (0 à 2): "))

        while tour_depart < 0 or tour_depart > 2:
            print("hors de l'intervalle [0,2]")
            tour_depart=int(input("entrez la tour de départ (0 à 2): "))

        while nombre_disques(plateau,tour_depart) == 0:
            print("la tour",tour_depart,"est vide")
            tour_depart=int(input("entrez la tour de départ (0 à 2): "))
        tour_arrivee=int(input("entrez la tour de d'arrivée(0 à 2): ")) 

    return tour_depart , tour_arrivee

def jouer_un_coup(plateau,n):
    """reçoit le plateau et le nombre total de disques, détermine le
    déplacement que le joueur souhaite faire et réalise effectivement le
    déplacement en mettant à jour le plateau et l'affichage vu par le joueur"""
    a,b = lire_coords(plateau)
    efface_disque(min(plateau[a]),plateau,n)
    plateau[b].append(min(plateau[a]))
    plateau[a].remove(min(plateau[a]))
    print("Plateau : ",plateau)
    dessine_disque(min(plateau[b]), plateau,n)
    
def boucle_jeu(plateau,n):
    """reçoit le plateau, le nombre total de disque et fait faire des
    déplacements au joueur jusqu'à ce qu'il résoud le problème
    + affiche le nombre minimal de coups possibles
    + affiche et met à jour le compteur de coups
    + sauvegarde les coups / les différentes configurations du plateau dans
    un dictionnaire dico_doups
    + demande entre chaque coups à l'utilisateur s'il veut annuler le coup
    et réalise l'annulation de coups le cas échéant
    + affiche un message de victoire avec le nombre de coups joués et le
    nombre minimal de coups possible"""
    print("nombre minimal de coups possible :",2**n-1)
    compteur=0                      #----------
    up()                            #affiche "coup n°"
    goto(-20,-20)
    down()
    color("orange")
    write("coup n°")
    up()
    goto(20,-20)
    down()
    write(compteur)                 #----------
    plateau_init=init(n)
    dico_coups={0:plateau_init}
    t1=time()
    while verifier_victoire(plateau,n)== False:
        print("Coups numero ",compteur,"\n")
        jouer_un_coup(plateau,n)
        color("black")              #----------
        up()                        #affiche "coup n°"
        goto(20,-20)
        down()
        write(compteur)
        compteur = compteur + 1
        color("orange")
        up()
        goto(20,-20)
        down()
        write(compteur)             #----------
        dico_coups[compteur]=deepcopy(plateau)
        annuler=input("voulez vous annuler ? (o/n): ")
        if annuler == "o":
            annuler_dernier_coup(dico_coups,compteur,plateau,n)
            compteur-=1
            plateau=dico_coups[compteur]
    t2=time()
    temps_de_jeu = t2 - t1
    print("Tu as gagné en" ,compteur, "coups")
    print("nombre minimal de coups possible :",2**n-1)
    pseudo=input("Saisis ton nom : ")
    Date=datetime.datetime.now()
    enregistrer_score(pseudo,n,compteur,temps_de_jeu,Date)
    affiche_score()

#-----------------------------------------------------------------
#                            Partie D
#-----------------------------------------------------------------
def dernier_coup(coups,numero):
    """reçoit un dictionnaire contenant l'ensemble des coups / configuration du
    plateau ainsi que le numero du dernier coup. Puis détermine en renvoie la
    tour de départ et la tour d'arrivée que le joueur a saisi lors du dernier
    coup"""
    dernier=coups[numero]
    avant_dernier=coups[numero-1]
    if avant_dernier[0]==dernier[0]:
        if disque_superieur(avant_dernier,1)==disque_superieur(dernier,2):
            a=1
            b=2
        elif disque_superieur(avant_dernier,2)==disque_superieur(dernier,1):
            a=2
            b=1   
    elif avant_dernier[1]==dernier[1]:
        if disque_superieur(avant_dernier,0)==disque_superieur(dernier,2):
            a=0
            b=2
        elif disque_superieur(avant_dernier,2)==disque_superieur(dernier,0):
            a=2
            b=0        
    elif avant_dernier[2]==dernier[2]:
        if disque_superieur(avant_dernier,0)==disque_superieur(dernier,1):
            a=0
            b=1
        elif disque_superieur(avant_dernier,1)==disque_superieur(dernier,0):
            a=1
            b=0 
    return a,b

def annuler_dernier_coup(coups,numero,plateau,n):
    """reçoit le dictionnaire contenant l'ensemble des coups, le numero du
    dernier coup, le plateau et le nombre total de disques.
    Il détermnie ensuite le dernier déplacement fait par le joueur et réalise
    le même déplacement à l'envers en mettant à jour le plateau, l'affichage
    vu par le joueur le compteur de coups"""
    a,b=dernier_coup(coups,numero)
    efface_disque(min(plateau[b]),plateau,n)
    coups[numero][a].append(min(coups[numero][b]))
    coups[numero][b].remove(min(coups[numero][b]))
    dessine_disque(min(coups[numero][a]),coups[numero],n)
    del coups[numero]
    
#-----------------------------------------------------------------
#                            Partie E
#-----------------------------------------------------------------        
def enregistrer_score(nom, n , nb_coups,temps,date):
    """reçoit le pseudo du joueur, le nombre total de disques, le nombre de
    coups et le temps de la partie puis détermine la date et l'heure de la
    partie avant sauvegarder le tout dans un ficher .txt"""
    score = "     "+str(n)+"         "+str(nb_coups)+"       "+str(temps)+"  "+nom+"       "+str(date)+"\n"
    fichier_score = open("tableau scores Tours de Hanoï.txt" , "a")
    fichier_score.write(score)
    fichier_score.close()

def affiche_score():
    fichier_score = open("tableau scores Tours de Hanoï.txt")
    texte=fichier_score.read()
    print()
    print("nombre de |  nombre  | temps en secondes | joueur | date")
    print(" disques  | de coups |")
    print(texte)

def trie_score():
    fichier_score = open("tableau scores Tours de Hanoï.txt")
    lignes_fichier_score = fichier_score.readlines()    
    fichier_score.close()
    for i in range (len(lignes_fichier_score)):
        print(lignes_fichier_score[i])
    lignes_fichier_score.sort
    for j in range (len(lignes_fichier_score)):
        print(lignes_fichier_score[j])

#-----------------------------------------------------------------
#                     Programme principal
#-----------------------------------------------------------------
nombre=int(input("entrez un entier : "))
Plateau=init(nombre)
print("Plateau : ",Plateau)
dessine_plateau(nombre)
dessine_config(Plateau,nombre)
boucle_jeu(Plateau,nombre)

#-----------------------------------------------------------------
#                     Test de fonctions
#-----------------------------------------------------------------
