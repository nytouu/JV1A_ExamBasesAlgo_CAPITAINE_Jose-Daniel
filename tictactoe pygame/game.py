#!/bin/python

"""
morpion fait l'annee derniere en cours de lycee NSI
la consigne etait de faire un projet sous pygame
et d'utiliser les classes

"""

import pygame, sys
from pygame.locals import *

# initialisation
# de pygame et des variables dont pygame a besoin

clock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption('Tic Tac Toe')

WIDTH = 800
HEIGHT = 800

screen = pygame.display.set_mode((HEIGHT, WIDTH),0,32)

class Board():

    # valeurs que les cases du tableau peuvent prendre
    NULL = 0
    CIRCLE = 1
    CROSS = 2

    def __init__(self):
        self.click = False

        pygame.mouse.set_visible(False)

        # curosr = 16x16 donc 16/2 pour centrer
        self.cursoroffset = [-8, -8]

        # la methode convert_alpha permet de garder la transparence
        self.cursorimg = pygame.image.load('cursor.png').convert_alpha()

        self.crossimg = pygame.image.load('cross.png').convert()
        self.circleimg = pygame.image.load('circle.png').convert()

        self.framerate = 144

        # self.game contient le tableau pour la logique du jeu
        self.game = [ [0,0,0],
                      [0,0,0],
                      [0,0,0] ]

        # self.rects est un tableau qui contient les hitbox pygame des cases pour cliquer dessus
        self.rects = [ [],
                       [],
                       [] ]

        self.current_team = Board.CIRCLE

        self.init_rects()

        # tant qu'il n'y a pas de gagnant, on itere la boucle de jeu
        while self.check_win() == None:
            self.loop()

        # lorqu'on a trouve un gagnant (ou lorsqu'il n'y en a pas) on sors de la boucle et on annonce le gagner
        # si il n'y a pas de gagnant, la methode announce_winner prend en charge l'egalite
        self.announce_winner()

        pygame.quit()
        sys.exit()

    def init_rects(self):
        for i in range(3):
            for j in range(3):
                self.rects[i].append( (pygame.Rect(i*WIDTH/3,j*HEIGHT/3,WIDTH/3,HEIGHT/3),[j,i]) )

    def announce_winner(self):
        if self.check_win() == Board.CIRCLE:
            print("Circle won!")
        elif self.check_win() == Board.CROSS:
            print("Cross won!")
        else:
            print("Nobody won :(")

    def loop(self):
        # game loop
        self.draw()

        # boutons pour pygame
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    mx, my = pygame.mouse.get_pos()
                    self.on_click([mx,my])

        # update le display pour draw les frames
        pygame.display.update()
        clock.tick(self.framerate)

    def draw(self):
        # clear screen
        screen.fill((0,0,0))
        # draw shapes
        for i in range(3):
            for j in range(3):
                self.draw_shape(self.game[i][j],[i,j])

        # draw board
        self.draw_board()

        mx, my = pygame.mouse.get_pos()
        screen.blit(self.cursorimg, (mx + self.cursoroffset[0], my + self.cursoroffset[1]))

    def draw_board(self):
        # il n'y a que deux lignes verticales et horizontales
        # pour appliquer cela a un puissance 4 il faudrait iterer 6 fois pour les lignes verticales
        # et 5 fois pour les lignes horizontales
        for i in range(2):
            for j in range(2):
                pygame.draw.line(screen,(255,255,255),[WIDTH*(i+1)/3,0],[WIDTH*(i+1)/3,HEIGHT],2)
                pygame.draw.line(screen,(255,255,255),[0,HEIGHT*(j+1)/3],[WIDTH,HEIGHT*(j+1)/3],2)

                # ici pour appliquer ce code a un puissance 4 il faudrait changer les coordonnees
                # d'affichage, au lieu d'avoir WIDTH/3 il faudrait WIDTH/7 et HEIGHT/6

    def draw_shape(self,shape,coords):
        if shape == Board.NULL:
            # rien besoin de draw
            pass
        elif shape == Board.CROSS:
            screen.blit(self.crossimg,(HEIGHT/3*coords[1],WIDTH/3*coords[0]))
        elif shape == Board.CIRCLE:
            screen.blit(self.circleimg,(HEIGHT/3*coords[1],WIDTH/3*coords[0]))

    def on_click(self,curpos):
        for line in self.rects:
            for rect in line:
                if rect[0].collidepoint(curpos):
                    x = rect[1][0]
                    y = rect[1][1]

                    if self.game[x][y] == Board.NULL:
                        self.game[x][y] = self.current_team

                        # on ne change de team que si une case libre est jouee
                        self.toggle_team()

    def toggle_team(self):
        if self.current_team == Board.CIRCLE:
            self.current_team = Board.CROSS
        elif self.current_team == Board.CROSS:
            self.current_team = Board.CIRCLE

    def set_circle(self,coords):
        self.game[coords[0]][coords[1]] = Board.CIRCLE

    def set_cross(self,coords):
        self.game[coords[0]][coords[1]] = Board.CROSS

    def check_win(self):
        # check lignes
        for i in range(3):
            if self.game[i][0] == self.game[i][1] == self.game[i][2] != 0:
                return self.game[i][0]

        # check colonnes
        for j in range(3):
            if self.game[0][j] == self.game[1][j] == self.game[2][j] != 0:
                return self.game[0][j]

        # check diagonales
        if self.game[0][0] == self.game[1][1] == self.game[2][2] != 0:
            return self.game[0][0]
        if self.game[2][0] == self.game[1][1] == self.game[0][2] != 0:
            return self.game[2][0]

        # check si il y a egalite
        diff = 0
        for row in self.game:
            for square in row:
                if square != Board.NULL:
                    diff+=1

        if diff == 9:
            return Board.NULL # != None

        # sinon pas de gagnant
        return None

game = Board()
