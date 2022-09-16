from audioop import reverse
from ctypes.wintypes import LPSC_HANDLE
from operator import truediv
from random import random
import re
import random 

#exo 1---------------------------------------------------------------------------------------------------------------
def full_name(str_arg:str):
    nom,prenom = str_arg.split(" ", 1)
    prenom = prenom.replace(prenom[0],prenom[0].upper())
    return nom.upper() + " " + prenom

print(full_name("garau thomas"))

def is_mail_regex(str: str) ->bool:
    regex = '^(?!.*[.]{2})([^.][\w\d\-_.]+)([\w\d][@])([\w\d\-_]*)([.])([\w\d\-_]*)'
    match = False
    result = re.match(regex, str)
    if result is not None:
        match = True
    else:
        match = False
    return match 

#true
print(is_mail_regex("thomas.garau8@gmail.com"))
print(is_mail_regex("thom.as.ga.rau8@gmail.com"))
print(is_mail_regex("thom.as.ga_rau8@gma-il.com"))
#false
print(is_mail_regex("thomas..garau8@gmail.com"))
print(is_mail_regex("thomas.garau8.@gmail.com"))
print(is_mail_regex("thomas.gara@u8@gmail.com"))
print(is_mail_regex("thomas.gara@u8@gmail.a.c"))

#retourne true si la liste contient deux . consecutif 
def is_consecutif(LIST: list[str]) ->bool:
    consecutif = False
    i = 0
    while consecutif is False and i < len(LIST) -1:
        if LIST[i] == "." and LIST[i+1] == ".":
            consecutif = True
        i+=1
    return consecutif

#prend en parametre un maile et retourne un code representant ca validite
def is_mail(str: str) ->bool:
    code = "(0,0)"
    i = 0
    LIST = str.split('@', 1)
    print(LIST)
    if "@" not in LIST :
        #si debute ou fini par .
        if LIST[0][0] == "." or LIST[0][len(LIST[0])-1] == "." or "@" in LIST[0] :
            code = "(0,1)"
        elif is_consecutif(LIST[0]):
             code = "(0,2)"
        elif is_consecutif(LIST[1]):
            code = "(0,2)"
        elif LIST[1][0] == "." or LIST[1][len(LIST[1])-1] == "." or "@" in LIST[1] :
            code = "(0,3)"
        elif "." not in LIST[1]:
            code = "(0,4)"   
    else: 
        code = "(0,2)"

    return code

#non regex 
#valide
print(is_mail("thomas.garau8@gmail.com"), "00")
print(is_mail("thom.as.ga.rau8@gmail.com"), "00")
print(is_mail("thom.as.ga_rau8@gma-il.com")," 00")
#invalide
print(is_mail("thomas..garau8@gmail.com"), "01")
print(is_mail("thomas.garau8.@gmail.com"), "01")
print(is_mail("thomas.garau8@gma@il.com"), "01")
print(is_mail("thomas.garau8@gmail..c"), "03")
print(is_mail("thomas.garau8@gmail.c."), "03")
print(is_mail("thomas.garau8@gmailzee"), "04")


# exo 2------------------------------------------------------------------------------------------------------------------
#1

lst_mot=["jouer","bonjour", "punir", "jour", "aurevoir", "revoir", "pouvoir", "cour", "abajour", 
"finir", "aimer"]
lst_mot_suffixe = ["iel", "opiniatre","activiste", "pessimiste", "royaliste"]
lst_mot_suffixe_attendu = ["activiste", "pessimiste", "royaliste"]
lst_mot_prefixe = ["incontournable", "incessant", "interminable", "amphitéatre", "amphibie", "ambivalent"]
lst_mot_prefixe_attendu = ["incontournable", "incessant", "interminable"]
lst_mot_prefixe_et_suffixe = ["inprevisible", "interpretable", "impartial", "inacessible"]
lst_mot_prefixe_et_suffixe_attendu = ["inacessible"]

#prend en entrer une liste est un entier, retourne une liste contenant l'ensemble des mots d'une taille n de la première liste
def mots_Nlettres(lst_str, n: int) ->list:
    list_return = []
    for e in lst_str:
        if len(e) == n:
            list_return.append(e)
    return list_return

#prend en entrer un mot et un prefixe, retourne true si le mot est formé à partir du préfixe
def commence_par(mot: str, prefixe:str) ->bool:
    return (mot[:len(prefixe)] == prefixe)

#prend en entrer un mot et un suffixe, retourne true si le mot est formé à partir du suffixe
def finit_par(mot, suffixe):
    return mot[len(mot) - len(suffixe):len(mot)] == suffixe

#prend en parametre une liste est un suffixe, retourne une nouvelle liste de tous les mots formé à partir du suffixe
def finissent_par(lst_str: list[str], suffixe:str) -> list:
    list_return = []
    for e in lst_str:
        if finit_par(e, suffixe):
            list_return.append(e)
    return list_return

#prend en parametre une liste est un prefixe, retourne une nouvelle liste de tous les mots formé à partir du prefixe
def commencent_par(lst_str: list[str], prefixe:str) -> list:
    list_return = []
    for e in lst_str:
        if commence_par(e, prefixe):
            list_return.append(e)
    return list_return

#retourne l'ensemble des mots formé à partir du suffixe et du prefixe, est correspondant à la taille passer en paramètres
def liste_mots (lst_str: list[str], prefixe: str, suffixe: str, n:int) ->list[str]:
    list_return = commencent_par(lst_str, prefixe)
    list_return = finissent_par(list_return, suffixe)
    list_return = mots_Nlettres(list_return, n)

    return list_return

#fonction test -----------------

def test_mots_Nlettres(fonction:callable, result_attendu) ->bool:
    test = False
    if len(fonction) == result_attendu:
        test = True
    return test

def test_commence_par(fonction:callable, resultat_attendu: bool) ->bool:
    test = False
    if fonction == resultat_attendu:
        test = True
    return test

def test_finit_par(fonction:callable, resultat_attendu: bool) ->bool:
    test = False
    if fonction == resultat_attendu:
        test = True
    return test

def test_finissent_par(fonction:callable, result_attendu: list[str]):
    test = False
    if fonction == result_attendu:
        test = True
    return test

def test_commencent_par(fonction:callable, result_attendu: list[str]):
    test = False
    if fonction == result_attendu:
        test = True
    return test

def test_liste_mots(fonction: callable, result_attendu: list[str]) -> bool:
    test = False
    if fonction == result_attendu:
        test = True
    return test

print(test_mots_Nlettres(mots_Nlettres(lst_mot,5),4))
print(test_commence_par(commence_par("intolerable", "in"), True))
print(test_finit_par(finit_par("empiriste", "iste"), True))
print(test_finissent_par(finissent_par(lst_mot_suffixe,"iste"), lst_mot_suffixe_attendu))
print(test_commencent_par(commencent_par(lst_mot_prefixe,"in"), lst_mot_prefixe_attendu))
print(test_liste_mots(liste_mots(lst_mot_prefixe_et_suffixe,"in", "ible",11 ), lst_mot_prefixe_et_suffixe_attendu))

#exo3---------------------------------------------------------------------------------------
#prend en parametres le chemin d'un fichier est retourne sont contenu sous forme de liste (1lignes = 1 index)
def dictionnaire(fichier) ->list:
    file = open(fichier, encoding="utf-8")
    content = []
    line = file.readlines()
    for l in line:   
        #supprime les pays
        a = l.split()
        #eviter de crash en cas de pays qui n'a pas de capital est donc de lignes avec un seule mot
        if len(a) > 1:
            a = a[1]
        content.append(a)
    #del premiere ligne qui est pays capital
    content.pop(0)
    return content

#retourne le contenu d'un fichier sous forme de dictionnaire organisé par la longueur des mots 
def remplire_dict(files) -> dict:
    list_ville = dictionnaire(files)
    dico = {}
    for e in list_ville:
        #verifie si la cle existe si non la cree avant d'ajouter l'element
        if len(e) in dico:
            dico[len(e)] += [e]
        else: 
            dico[len(e)] = [e]
    return dico 

#demande à l'utilisateur de choisir un niveau de difficulté est retourne la partie du dictionnaire correspondante
def choose_level() -> list:
    level = input("choisisser un niveau de difficulté : facile = 1, normale = 2, difficile = 3")
    dico = remplire_dict("capitales.txt")
    list_capitales = []
    if level == "1":
        for key in dico:
            #tout les noms de villes d'une longueur de moins de 7
            if key < 7:
                list_capitales += dico[key]
    elif level ==2: 
        for key in dico:
            #tout les noms de villes d'une longueur suppérieur à 8
            if key > 8:
                list_capitales += dico[key]
    else:
        for key in dico:
            #tout les noms de villes d'une longueur de 6à9
            if key in range(7,9):
                list_capitales += dico[key]
    return list_capitales

#prend en paramètres un charactere est verifie si il est present dans le mot l'ajoute à la liste des indice_connu si ces le cas
def places_lettre(ch : str):
    i = 0
    if ch in runGame.mot:
        for e in runGame.mot:
            if e == ch and i not in runGame.indice_connu:
                runGame.indice_connu.append(i)
                runGame.indice_connu.sort()
            i+=1
    else:
        runGame.erreur +=1
        for e in range(0,runGame.erreur):
            print(list(runGame.pendu.values())[i])
            i+=1

#print les lettres trouvé du mots est _ pour les autres
def outputStr():
    runGame.revele = len(runGame.mot) * "_"
    for e in runGame.indice_connu:
        runGame.revele = runGame.revele[:e] + runGame.mot[e] + runGame.revele[e+1:]
    print(runGame.revele)

#inicie la partie
def runGame():
    list_capitales = choose_level()
    runGame.mot = random.choice(list_capitales)
    #represente les lettres trouvé par le joueur
    runGame.indice_connu = []
    runGame.revele = len(runGame.mot) * "_"
    runGame.erreur = 0
    outputStr()
    runGame.pendu = {
        "c1": "|---]",
        "c2": "| O ",
        "c3": "| T ",
        "c4": "|/ \ ",
        "c5": "|______"
    }
    while runGame.revele != runGame.mot and runGame.erreur <5:
        ch = input("Veuillez choisir une lettre")[0].lower()
        places_lettre(ch)
        outputStr()
    
    if runGame.erreur == 5:
        print("perdu")
    else:
        print("félicitation")

#runGame()


#exo 4--------------------------------------------------------------------------------
####

def mot_correspond(mot, motif) ->bool:
    correspond = True
    i = 0
    while correspond and i < len(mot):
        if mot[i] != motif[i]:
            correspond = False
        i+=1
    return correspond

def present(lettre, mot) ->int:
    indice = -1
    i =0
    while indice == -1 and i < len(mot):
        if lettre == mot[i]:
            indice = i
        i+=1
    return indice

def mot_possible(lettre, mot) -> bool:
    match = True
    i = 0
    while match and i < len(mot):
        if mot[i] not in lettre:
            match = False
        else:
            index = lettre.index(mot[i])
            lettre = lettre[:index] +  lettre[index +1:]
        i+=1
    return match

print(mot_correspond("cheval", "cheval"), "true correspond")
print(mot_correspond("cheval", "aos"), "false correspond")
print(present("e", "elephant"), " true elephant")
print(present("Z", "elephant"), "false elephant")
print(mot_possible("boiujuroan", "bonjour"), "true mot possible")
print(mot_possible("pareilement", "pareillement"), "false mot possible")

def dictionnaire2(fichier) ->list:
    file = open(fichier, encoding="utf-8")
    content = []
    line = file.read().splitlines()
    for l in line:   
        content.append(l)
    return content

def remplire_dict2(files) -> dict:
    list_ville = dictionnaire2(files)
    dico = {}
    for e in list_ville:
        #verifie si la cle existe si non la cree avant d'ajouter l'element
        if len(e) in dico:
            dico[len(e)] += [e]
        else: 
            dico[len(e)] = [e]
    return dico 

def mot_optimaux(lettre) -> list:
    dico = remplire_dict2("littre.txt")
    list_mots_optimaux = []
    i = 0
    for key in dico:
        if key > i:
            i = key
    print(i)
    while i > 0 and len(list_mots_optimaux) == 0:
        if i in dico:
            for mot in dico[i]:
                if mot_possible(lettre, mot):
                    list_mots_optimaux.append(mot)
        i-=1
    return list_mots_optimaux

print(mot_optimaux("madeoile"))


#5---------------------------------------------------------------------------------------------------------------

#prend en paramètres un caractere et retourne true si ces ( ou [ ou {
def ouvrante(car: str) ->bool:
    return car in ["(", "[", "{"]

#prend en paramètre un caractere et retourne true si ces ) ou ] ou }
def fermante(car: str) ->bool:
    return car in [")", "]", "}"]

#prend en parametre un caractere, si celui ci est ( ou [ ou { retourne le caractere fermant ) ] }
def renverse(car: str) -> str:
    if fermante(car):
        if car == ")":
            car =  chr(ord(car) -1)
        else:
             car = chr(ord(car) -2)
    return car

#prend en param un caractere est retourne true si celui-ci est un opérateur arithmétique
def operateur(car: str) ->bool:
    return car in ["*", "+", "=", "-", "/"]

#prend en param un caractere est retourne true si ces un nombre 
def nombre(car: str) ->bool:
    return car.isdigit()

#prend en param un caractere est retourne un bool representant ci il est valide ou non (est un int ou opérateur ou ([{}]))
def caractere_valide(car: int) -> bool:
    return operateur(car) or nombre(car) or fermante(car) or ouvrante(car) or car == " "

#meme chose mais en utilisant un regex 
def caractere_valide_regex(car: int) -> bool:
    regex = "[\d\s(){}+-=\.*\/\]\[]+$"
    bool = False
    if re.match(regex, car) is not None:
        bool = True
    return bool 


print(ouvrante("("), "ouvrante true")
print(ouvrante("az"), "ouvrante false")
print(fermante("]"), "fermante true")
print(fermante("a"), "fermante false")
print(renverse("]"), "renverse [")
print(renverse("}"), "renverse {")
print(renverse(")"), "renverse (")
print(renverse("az"), "renverse az")
print(operateur("/"), "operateur true")
print(operateur("*"), "operateur true")
print(operateur("3"), "operateur false")
print(nombre("345"), "nomrbe true")
print(nombre("ezia"), "nombre false")
print(caractere_valide_regex("]"), "caractere_valide regex true")
print(caractere_valide_regex("]a"), "caractere valide regex false")
print(caractere_valide_regex("a"), "caractere valide regex false")

#prend en param un string verifie que les caractere qui le compose sont valide ainsi que la bonne utilisation des [{()}]
def verif_parenthese(expression: str)->bool:
    correcte = True
    i = 0
    pile = []
    while correcte and  i < len(expression):
        if caractere_valide_regex(expression[i]):

            if expression[i] in ["[","(","{"]:
                pile.append(expression[i])

            elif expression[i] in ["]", ")", "}"]:
                if len(pile) > 0:  # utilisé un try catch permet d'éviter les condition
                    if pile[len(pile)-1] == renverse(expression[i]):
                        pile.pop(len(pile) -1)
                    else:
                        correcte = False
                else: 
                    correcte = False
        else: 
            correcte = False
        i+=1
    if len(pile) != 0:
        correcte = False

    return correcte
        
print(verif_parenthese("8*(10-4) / (6-7) {[]}4**2 + 9.12"), "verif_parenthese true")
print(verif_parenthese("8*(10-4) / (6-7) [{]}4**2 + 9.12"), "verif_parenthese false")
print(verif_parenthese("8*(10-4) / 6-7) []}4**2 + 9.12"), "verif_parenthese false")
print(verif_parenthese("8*(10-4 / (6-7 {[]4**2 + 9.12"), "verif_parenthese false")
print(verif_parenthese(")8*(10-4 / (6-7 ]4**2 + 9.12"), "verif_parenthese false")
print(verif_parenthese("8*(10-4) / (6-7) zadaz"), "verif_parenthese false")
