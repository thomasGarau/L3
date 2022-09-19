import math

ZONE_OM1 = ['guyane', 'guadeloupe', 'martinique', 'reunion', 'st-pierre', 'st-Barthelemy', 'st-martin', 'mayote']
ZONE_OM2 = ['nouvelle-caledonie', 'polynesie', 'wallis-et-futuna']
STICKER_SUIVI = .5
BIBLIOTHEQUE = {
    'lettre_verte' :{
        20 : 1.16,
        100: 2.32,
        250: 4,
        500: 6,
        1000: 7.5,
        3000: 10.5,
    },

    'lettre_prioritaire' :{
        20 : 1.43,
        100: 2.86,
        250: 5.26,
        500: 7.89,
        3000: 11.44,
    },

    'ecopli' :{
        20 : 1.14,
        100: 2.28,
        250: 3.92,
    },

    'eco_outre_mer' :{
        500 : 8.35,
        1000: 11.2,
        2000: 14.1,
        5000: 23.65,
        10000: 37.5,
        15000: 75.85,
        30000: 87.4
    }
}

def prix():
    """détermine le prix de l'envoi d'un colis ou d'une lettre

    Returns:
        int: prix de l'envoi
    """
    #récupére les saisie de l'utilisateur
    LETTRE_TYPE = int(input("Veuillez saisir le type de lettre à envoyer : 1 = verte, 2 = prioritaire, 3 = ecopli, 4 = outre-mer"))
    LETTRE_POID = int(input("Veuillez saisir le poid de votre lettre"))
    LETTRE_DEST = input("Veuillez renseigner la destination de votre envoi, zone disponible :'\n' guyane, guadeloupe, martinique, reunion, st-pierre, st-Barthelemy, st-martin, mayote nouvelle-caledonie, polynesie, wallis-et-futuna ").lower()
    price = 0
    previous_value = 0
    complement = 0


    if LETTRE_TYPE == 1 or LETTRE_TYPE == 2 or LETTRE_TYPE == 3:
        STICKER = input("Voulez vous un sticker de suivis pour 0.5€ supplémentaire ? oui ou non")
        if STICKER == "oui" :
            price += .5

    #associe l'input de l'utilisateur concernant le type d'envoi au bon dictionnaire de tarif
    match LETTRE_TYPE:
        case 1:
            envoi = "lettre_verte"
        case 2: 
            envoi = "lettre_prioritaire"
        case 3:
            envoi = "ecopli"
        case 4:
            envoi = "eco_outre_mer"

    # récupére le premier et le dernier index pour obtenir le poid max et min 
    POID_MAX = list(BIBLIOTHEQUE[envoi].keys())[-1]
    if LETTRE_POID < list(BIBLIOTHEQUE[envoi].keys())[0]:
        # si inferieur à poid min alors on attribu le prix min 
        price = list(BIBLIOTHEQUE[envoi].value())[0]
    if LETTRE_POID > POID_MAX :
        # si trop lourd arrette la fonction pour que l'utilisateur resaisisse le poid
        print(f"trop lourd. le poid maximum pour ce type d'envois est de : {POID_MAX}")
        return
    
    #parcours le dico associé au type d'envoi jusqua obtenir la tranche supérieur à celle de l'envoi 
    #une fois trouvé on applique la tranche précedente, puisque la boucle ce casse avant de modifié previous_value 
    for key, value in BIBLIOTHEQUE[envoi].items():
        if LETTRE_POID < key:
            break
        else:
            previous_value = value
    
    #applique le tarif om1 ou om2 si le type de colis le poid est la destination le requiert 
    if LETTRE_POID > 100:
        if LETTRE_DEST in ZONE_OM1:
            match envoi:
                case "lettre_verte":
                    complement = .05
                case "lettre_prioritaire":
                    complement = .05
                case "ecopli":
                    complement = .02
        elif LETTRE_DEST in ZONE_OM2:
            match envoi:
                case "lettre_verte":
                    complement = .11
                case "lettre_prioritaire":
                    complement = .11
                case "ecopli":
                    complement = .05

        #calcule et retourne le tarif
        complement = math.ceil(LETTRE_POID / 10) * complement
    return (price + complement + previous_value)

print(prix())

