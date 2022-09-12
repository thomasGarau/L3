import re
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

def is_consecutif(LIST: list[str], e: int) ->bool:
    consecutif = False
    i = 0
    while consecutif is False and i < len(LIST) -1:
        if LIST[i] == "." and LIST[i+1] == ".":
            consecutif = True
        i+=1
    return consecutif

def is_mail(str: str) ->bool:
    code = "(0,0)"
    i = 0
    LIST = str.split('@', 1)
    print(LIST)
    if "@" not in LIST :
        #le séparateur étant @ si il y'a deux @ le premier seras supprimer est le second ce retrouveras nécessairement dans la liste[1] quand bien même les deux ce trouve dans le corp du mail
        if LIST[0][0] == "." or LIST[0][len(LIST[0])-1] == "." or "@" in LIST[0] :
            code = "(0,1)"
        elif is_consecutif(LIST[0], 0):
             code = "(0,1)"
        elif is_consecutif(LIST[1], 1):
            code = "(0,3)"
        elif LIST[1][0] == "." or LIST[1][len(LIST[1])-1] == "." or "@" in LIST[1] :
            code = "(0,3)"
        elif "." not in LIST[1]:
            code = "(0,4)"   
    else: 
        code = "(0,2)"

    return code

#non regex 
#true
print(is_mail("thomas.garau8@gmail.com"), "00")
print(is_mail("thom.as.ga.rau8@gmail.com"), "00")
print(is_mail("thom.as.ga_rau8@gma-il.com")," 00")
#false
print(is_mail("thomas..garau8@gmail.com"), "01")
print(is_mail("thomas.garau8.@gmail.com"), "01")
print(is_mail("thomas.gara@u8@gmail.com"), "01")

print(is_mail("thomas.garau8@gmail..c"), "03")
print(is_mail("thomas.garau8@gmail.c."), "03")
print(is_mail("thomas.garau8@gmailzee"), "04")
