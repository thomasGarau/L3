from contextlib import nullcontext
import random

def game():
    game.player1_score = 0
    game.player2_score = 0
    game.player1_name = ""
    game.player2_name = ""

    #choix du mode de jeux est des pseudos
    game.GAME_CHOICE = input("Voulez vous jouer contre un autres joueur ou contre la machine ? J = joueur M = machine ")
    while game.player1_name == game.player2_name:
        game.player1_name = input("Joueur1 qu'elle est votre nom?")
        if game.GAME_CHOICE == "J":
            game.player2_name = input("Joueur2 qu'elle est votre nom?")
        else: 
            game.player2_name = "Machine"

    #bo5 continue tant qu'un joueur n'atteint pas 3points
    while game.player1_score <3 and game.player2_score <3:
        restart = input("Voulez vous effectuer une manche? 0 = non; 1 = oui")
        if restart == "1":
            set()
        else:
            return

    if game.player1_score >= 3:
        print(f"Félicitation {game.player1_name} vous avez gagner")
    else:
        print(f"Felicitation {game.player2_name} vous avez gagner")


def set():
    set.player1_choice = int(input(f"{game.player1_name} Que voulez vous jouer? 0 = pierre; 1 = ciseaux; 2 = feuille; 3 = puits"))
    if game.GAME_CHOICE == "J":
        set.player2_choice = int(input(f"{game.player2_name} Que voulez vous jouer? 0 = pierre; 1 = ciseaux; 2 = feuille; 3 = puits"))
    else: 
        set.player2_choice = random.randint(0,3)
    
    count_points()

def count_points():
    LIST = [1,2,3]

    #si les deux joueur joue pareille ex-aequo
    if set.player1_choice == set.player2_choice:
        print(f"{game.player1_name} à joué {set.player1_choice}, {game.player2_name} à joué {set.player2_choice}, ex-aequo  ")

    #si aucun des deux utilise le puits on utilise une liste pour déterminé le vainqueur index précedent = perd index suivant = gagne
    elif set.player1_choice != 3 and set.player2_choice != 3:
        if LIST[set.player1_choice +1] == set.player2_choice:
            game.player1_score +=1
            print(f"{game.player1_name} à joué {set.player1_choice}, {game.player2_name} à joué {set.player2_choice}, {game.player1_name} gagne ")
        else:
            game.player2_score +=1
            print(f"{game.player1_name} à joué {set.player1_choice}, {game.player2_name} à joué {set.player2_choice}, {game.player2_name} gagne ")

    #si non on vérifie les deux scénario de viquetoire impliquant puit pour 1 si elle ne sont pas rempli il perd forcement vu qu'il ne peut y'avoir d'égalité 
    else:
        if set.player1_choice == 3 and set.player2_choice != 2 or set.player1_choice == 2:
            game.player1_score += 1
            print(f"{game.player1_name} à joué {set.player1_choice}, {game.player2_name} à joué {set.player2_choice}, {game.player1_name} gagne ")
        else:
            game.player2_score += 1
            print(f"{game.player1_name} à joué {set.player1_choice}, {game.player2_name} à joué {set.player2_choice}, {game.player2_name} gagne ")
    #problème sur les condition pour le comptage de points
game()