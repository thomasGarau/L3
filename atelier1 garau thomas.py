from datetime import datetime
from math import *
from datetime import date

#1 -------------------------------------------------------------------------------------
interpretation={
    "denutrition":{
        "min": 0,
        "max":16.4,
    },
    "maigreur":{
        "min":16.5,
        "max":18.4
    },
    "normale":{
        "min":18.5,
        "max":24.9
    },
    "surpoids":{
        "min":25,
        "max":29.9
    },
    "obesite moderee":{
        "min":30,
        "max":34.9
    },
    "obesite severe":{
        "min":35,
        "max":39.9
    },
    "obesite morbide":{
        "min":40
    }
}
def message_imc(imc):
    if imc >= 40:
        return "obesite morbide"
    else:
        for key, value in interpretation.items():
            if imc > value['min'] and imc < value['max']:
                return key

def message_imcTest():
    print(message_imc(15))
    print(message_imc(22))
    print(message_imc(28))
    print(message_imc(37))
    print(message_imc(41))

message_imcTest()

#2 -------------------------------------------------------------------------------------

def est_bissextile(year):
    if (year%100 == 0 and year%400 == 0 and year%4 == 0):
        return True
    elif (year%100 != 0 and year%400 != 0):
        return(year%4 == 0)
    else: 
        return False

def test_bissextile():
    b = 0
    i = 0
    while i != 2000:
        if est_bissextile(i):
            print("bbb")
            b += 1
        i+=1
    print(b)
test_bissextile


#3 ---------------------------------------------------------------------------------------

def discriminant(a,b,c):
    """détermine le discriminant

    Args:
        a (int): représente ax²
        b (int): représente bx
        c (int): représente c

    Returns:
        int: return le discriminant
    """
    return b**2 - 4 * a * c

def racine_unique(a,b):
    """détermine la solution unique à delta

    Args:
        a (int): représente 2a
        b (int): représente -b

    Returns:
        int: return la racine unique
    """
    return -b / (2*a)

def racine_double(a,b,delta,num):
    """détermine les deux solution à delta

    Args:
        a (int): 2a
        b (int): -b
        delta (int): discriminant
        num (int): 1 ou 2 pour 1er racine ou seconde

    Returns:
        _type_: les deux racine à delta
    """
    if num == 1:
        return -b + sqrt(delta) / 2 * a
    elif num == 2:
        return -b - sqrt(delta) / 2 * a

def str_equation(a,b,c):
    """ retourne une écriture simplifié de l'équation

    Args:
        a (int): ax²
        b (int): bx
        c (int): c
 
    Returns:
        string: retourne l'équation simplifié
    """
    texte = ""

    if a != 1:
        if a !=0:
           texte = f"{a}x²"
    else:
        texte = "x²"

    if a != 0 and b != 0:
        texte = texte + "+"

    if b != 0: 
        if b !=1:
            texte = texte + f"{b}x "
        else:
            texte = texte + "x"

    if c != 0: 
        if (b != 0 or a != 0) and c > 0: 
            texte = texte + "+"
        texte = texte + f"{c}"
        
    return texte + "=0"

def solution_equation(a,b,c,delta):
    if 4*a*c > b**2:
        return f"Solution de l'équation {str_equation(a,b,c)}: \n Pas de racine réelle"
    elif 4*a*c == b**2:
        return f"Solution de l'équation {str_equation(a,b,c)} \n Racine unique : \n x={-b / 2 * a}"
    elif 4*a*c < b**2:
        return f"Solution de l'équation {str_equation(a,b,c)} \n Deux racines: \n x1={(-b + sqrt(delta)) / 2 * a} \n x2={(-b - sqrt(delta)) / 2 * a} "

def equation(a,b,c,delta):
    if 4*a*c > b**2:
        print(f"Solution de l'équation {str_equation(a,b,c)}: \n Pas de racine réelle")
    elif 4*a*c == b**2:
        print(f"Solution de l'équation {str_equation(a,b,c)}: \n x={-b / 2 * a}")
    elif 4*a*c < b**2:
        print(f"Solution de l'équation {str_equation(a,b,c)}: \n Deux racines: \n x1={(-b + sqrt(delta)) / 2 * a} \n x2={(-b - sqrt(delta)) / 2 * a} ")

def test():
    equation(2,6,5,4)
    equation(-2,3,7,65)
    equation(2,4,2,0)

test()





#4 ----------------------------------------------------------------------------------------------------

def date_est_valide(jour: int, mois: int, annee: int) -> bool:
    """verifie la validite de la saisi de l'utilisateur 

    Args:
        jour (int): représente le jours de naissance
        mois (int): représente le mois de naissance
        annee (int): représente l'annee de naissance

    Returns:
        bool: true ou false en fonction de la validité de la date
    """
    currentDateTime = datetime.today()
    date = currentDateTime.date()
    year = date.strftime("%Y")
    year =int(year)
    return(jour in range(1,32) and mois in range(1,13) and annee in range(1900, year+1))

def saisie_date_naissance():
    """demande a l'utilisateur de saisir ca date de naissance

        returns :
        date : retourne la date de naissance de l'utilisateur
    """
    i = 0
    day = 0
    month = 0
    year = 0
    while date_est_valide(day, month, year) != True:
        if i > 0:
            print("Veuillz uniquement saisir des nombres entiers")
        day = int(input("Veuillez saisir votre jours de naissance"))
        month = int(input("Veuillez saisir votre mois de naissance"))
        year = int(input("Veuillez saisir votre annee de naissance"))
        i+=1
    
    return(datetime(year=int(year),month=int(month),day=int(day)))

def age(date_naissance):
    """calcule l'age de l'utilisateur 

    Args:
        date_naissance (date): représente la date de naissance de l'utilisateur

    Returns:
        int: age de l'utilisateur
    """
    today = datetime.today()
    diff =today - date_naissance
    return floor(diff.days / 365)

def est_majeur(age):
    """détermine si l'utilisateur est majeur

    Args:
        age (int): représente l'age de l'utilisateur

    Returns:
        bool: true si majeur false si non
        int: l'age de l'utilisateur
    """
    majeur = age >= 18
    return majeur, age

def test_acces():
    """autorise l'acces si l'utilisateur est majeur le refuse si non 
    """
    [majeur, ages] = est_majeur(age(saisie_date_naissance())) 
    if majeur:
        print(f"Bonjour, vous avez {ages} ans, Accès autorisé ")
    else:
        print(f"Bonjour, vous avez {ages} ans, Accès autorisé ")

test_acces()
