#!/bin/python

gameBoard = [ ["Vide", "Vide", "Vide"],
              ["Vide", "Vide", "Vide"],
              ["Vide", "Vide", "Vide"] ]

# Exercice 1

def print_board():
    global gameBoard

    for ligne in gameBoard:
        for case in ligne:
            if case == "Vide":
                print(" - ", end="")
            elif case == "X":
                print(" X ", end="")
            elif case == "O":
                print(" O ", end="")
            else:
                print(" - ", end="")
            # le second argument permet de ne pas sauter des lignes
        print("")

# Exercice 2

def play_once(team):
    global gameBoard

    ligne   = input("Entrez un numero de ligne : 0, 1, 2 : ")
    colonne = input("Entrez un numero de colonne : 0, 1, 2 : ")

    if team == "Circle":
        gameBoard[int(ligne)][int(colonne)] = "O"
    elif team == "Cross":
        gameBoard[int(ligne)][int(colonne)] = "X"

    print_board()

# Exercice 3

def check_if_won():
    global gameBoard

    # check lignes
    for i in range(3):
        if gameBoard[i][0] == gameBoard[i][1] == gameBoard[i][2] != "Vide":
            print(gameBoard[i][0], gameBoard[i][1], gameBoard[i][2])
            return gameBoard[i][0]

    # check colonne
    for j in range(3):
        if gameBoard[0][j] == gameBoard[0][j] == gameBoard[0][j] != "Vide":
            print(gameBoard[0][j], gameBoard[0][j], gameBoard[0][j])
            return gameBoard[0][j]

    # check diagonales
    if gameBoard[0][0] == gameBoard[1][1] == gameBoard[2][2] != "Vide":
            return gameBoard[0][0]
    if gameBoard[2][0] == gameBoard[1][1] == gameBoard[0][2] != "Vide":
        return gameBoard[2][0]

    return None

# Exercice 4

def check_end():
    global gameBoard

    for ligne in gameBoard:
        for case in ligne:
            if case == "Vide":
                return False
    return True

# Exercice 5

current_team = "Circle"

def toggle_team():
    global current_team
    if current_team == "Circle":
        current_team = "Cross"
    if current_team == "Cross":
        current_team = "Circle"

def jeu():
    global current_team
    global gameBoard

    print("Tic Tac Toe :)")
    print("")
    winner = None
    print_board()

    while not check_end():
        play_once(current_team)
        print_board()
        print("winner",check_if_won())
        winner = check_if_won()
        if winner == "X":
            print("Cross won")
        elif winner == "O":
            print("Circle won")

        toggle_team()

jeu()


"""

Exercice 6

Pour faire un puissance 4 il faudrait aggrandir le
tableau de jeu en 6x7

Pour les alignement en diagonales il faudrait
programmer une meilleure methode que pour mon morpion,
un morpion n'a que 2 diagonales donc on peut les verifier
facilement mais cette methode ne s'applique pas a un
puissance 4 directement

Il faudrait prendre en compte la gravite en ne pouvoir
placer un jeton qu'au dessus un autre

"""
