# Monopoly state machine
import pygame
from pygame.locals import *
import MovementFile
from SpaceClass import Space
from ImageModifier import ImageModifier
import GameWindows
from Player import Player
import tkinter
from CardStacks import cardStacks

BOARDWIDTH = 1000
BOARDHEIGHT = 1000
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (165, 42, 42)
LIGHTBLUE = (168, 255, 255)
MAGENTA = (250, 45, 208)
ORANGE = (255, 127, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 53, 24)
DARKBLUE = (0, 0, 255)
LIGHTGREEN = (191, 219, 174)
gaming = True
pygame.init()
p1MvmtClass = MovementFile.movementLocation()
monopolyBoard = pygame.display.set_mode((BOARDWIDTH, BOARDHEIGHT))
gameWindows = GameWindows.gameWindows(monopolyBoard)
numPlayers = gameWindows.playerSelectWindow()
print("Num Players is:" + str(numPlayers))
players = []
playerNames = gameWindows.playerNamesScreen(numPlayers)
for i in range(numPlayers):
    players.append(Player(playerNames[i], i+1))
for player in players:
    print("Player " + player.playerName + "has turn order " + str(player.turnOrder))
drawPiles = cardStacks(numPlayers)  
spaces=[Space("Go", "PokeBall1", "Little Mac", "Low Tier Tax", "Marth", "King Dedede", "AssistTrophy1", "Kirby", "Meta Knight", "Jail", "Jigglypuff", "Pac Man", "", "", "", 0, 0, 0, 0, 0, 0, 0, 0), Space("Ganondorf", "Little Mac", "Low Tier Tax", "Marth", "King Dedede", "AssistTrophy1", "Kirby", "Meta Knight", "Jail", "Jigglypuff", "Pac Man", "Mewtwo", "", "", "", 2, 10, 30, 90, 160, 250, 60, 50), Space("PokeBall1", "Low Tier Tax", "Marth", "King Dedede", "AssistTrophy1", "Kirby", "Meta Knight", "Jail", "Jigglypuff", "Pac Man", "Mewtwo", "Incineroar", "", "", "", 0, 0, 0, 0, 0, 0, 0, 0), Space("Little Mac", "Marth", "King Dedede", "AssistTrophy1", "Kirby", "Meta Knight", "Jail", "Jigglypuff", "Pac Man", "Mewtwo", "Incineroar", "Ike", "", "", "", 4, 20, 60, 180, 320, 450, 60, 50), Space("Low Tier Tax", "King Dedede", "AssistTrophy1", "Kirby", "Meta Knight", "Jail", "Jigglypuff", "Pac Man", "Mewtwo", "Incineroar", "Ike", "Young Link", "", "", "", 200, 0, 0, 0, 0, 0, 0, 0), Space("Marth", "AssistTrophy1", "Kirby", "Meta Knight", "Jail", "Jigglypuff", "Pac Man", "Mewtwo", "Incineroar", "Ike", "Young Link", "PokeBall2", "", "", "", 25, 25, 50, 100, 200, 200, 200, 0), Space("King Dedede", "Kirby", "Meta Knight", "Jail", "Jigglypuff", "Pac Man", "Mewtwo", "Incineroar", "Ike", "Young Link", "PokeBall2", "Toon Link", "", "", "", 6, 30, 90, 270, 440, 550, 100, 50), Space("AssistTrophy1", "Meta Knight", "Jail", "Jigglypuff", "Pac Man", "Mewtwo", "Incineroar", "Ike", "Young Link", "PokeBall2", "Toon Link", "Link", "Low Tier Tax", "Pac Man", "Marth", 0, 0, 0,0, 0, 0, 0, 0), Space("Kirby", "Jail", "Jigglypuff", "Pac Man", "Mewtwo", "Incineroar", "Ike", "Young Link", "PokeBall2", "Toon Link", "Link", "Free Parking", "", "", "", 6, 30, 90, 270, 400, 550, 100, 50), Space("Meta Knight", "Jigglypuff", "Pac Man", "Mewtwo", "Incineroar", "Ike", "Young Link", "PokeBall2", "Toon Link", "Link", "Free Parking", "Falco", "", "", "", 8, 40, 100, 300, 450, 600, 120, 50), Space("Jail", "Pac Man", "Mewtwo", "Incineroar", "Ike", "Young Link", "PokeBall2", "Toon Link", "Link", "Free Parking", "Falco", "AssistTrophy2", "", "", "", 0, 0, 0, 0,0 ,0 ,0, 0), Space("Jigglypuff", "Mewtwo", "Incineroar", "Ike", "Young Link", "PokeBall2", "Toon Link", "Link", "Free Parking", "Falco", "AssistTrophy2", "Wolf", "", "", "", 10, 50, 150, 450, 625, 750, 140, 100), Space("Pac Man", "Incineroar", "Ike", "Young Link", "PokeBall2", "Toon Link", "Link", "Free Parking", "Falco", "AssistTrophy2", "Wolf", "Fox", "", "", "", 4, 4, 4, 4, 4, 4, 150, 0), Space("Mewtwo", "Ike", "Young Link", "PokeBall2", "Toon Link", "Link", "Free Parking", "Falco", "AssistTrophy2", "Wolf", "Fox", "Roy", "", "", "", 10, 50, 150, 450, 625, 750, 140, 100), Space("Incineroar", "Young Link", "PokeBall2", "Toon Link", "Link", "Free Parking", "Falco", "AssistTrophy2", "Wolf", "Fox", "Roy", "Samus", "", "", "", 12, 60, 180, 500, 700, 900, 160, 100), Space("Ike", "PokeBall2", "Toon Link", "Link", "Free Parking", "Falco", "AssistTrophy2", "Wolf", "Fox", "Roy", "Samus", "Dark Samus", "", "", "", 25, 25, 50, 100, 200, 200, 200, 0), Space("Young Link", "Toon Link", "Link", "Free Parking", "Falco", "AssistTrophy2", "Wolf", "Fox", "Roy", "Samus", "Dark Samus", "Mr Game & Watch", "", "", "", 14, 70, 200, 550, 750, 950, 180, 100), Space("PokeBall2", "Link", "Free Parking", "Falco", "AssistTrophy2", "Wolf", "Fox", "Roy", "Samus", "Dark Samus", "Mr Game & Watch", "Zero Suit Samus", "", "", "", 0, 0, 0, 0, 0, 0, 0, 0), Space("Toon Link", "Free Parking", "Falco", "AssistTrophy2", "Wolf", "Fox", "Roy", "Samus", "Dark Samus", "Mr Game & Watch", "Zero Suit Samus", "Go To Jail", "", "", "", 14, 70, 200, 550, 750, 950, 180, 100), Space("Link", "Falco", "AssistTrophy2", "Wolf", "Fox", "Roy", "Samus", "Dark Samus", "Mr Game & Watch", "Zero Suit Samus", "Go To Jail", "Ryu", "", "", "", 16, 80, 220, 600, 800, 1000, 200, 100), Space("Free Parking", "AssistTrophy2", "Wolf", "Fox", "Roy", "Samus", "Dark Samus", "Mr Game & Watch", "Zero Suit Samus", "Go To Jail", "Ryu", "Terry", "", "", "", 0, 0, 0, 0, 0, 0, 0, 0), Space("Falco", "Wolf", "Fox", "Roy", "Samus", "Dark Samus", "Mr Game & Watch", "Zero Suit Samus", "Go To Jail", "Ryu", "Terry", "PokeBall3", "", "", "", 18, 90, 250, 700, 875, 1050, 220, 150), Space("AssistTrophy2", "Fox", "Roy", "Samus", "Dark Samus", "Mr Game & Watch", "Zero Suit Samus", "Go To Jail", "Ryu", "Terry", "PokeBall3", "Kazuya", "Link", "Mr Game & Watch", "Roy", 0, 0, 0, 0, 0, 0, 0, 0), Space("Wolf", "Roy", "Samus", "Dark Samus", "Mr Game & Watch", "Zero Suit Samus", "Go To Jail", "Ryu", "Terry", "PokeBall3", "Kazuya", "Byleth", "", "", "", 18, 90, 250, 700, 875, 1050, 220, 150), Space("Fox", "Samus", "Dark Samus", "Mr Game & Watch", "Zero Suit Samus", "Go To Jail", "Ryu", "Terry", "PokeBall3", "Kazuya", "Byleth", "AssistTrophy3", "", "", "", 20, 100, 300, 750, 925, 1100, 240, 150), Space("Roy", "Dark Samus", "Mr Game & Watch", "Zero Suit Samus", "Go To Jail", "Ryu", "Terry", "PokeBall3", "Kazuya", "Byleth", "AssistTrophy3", "Pyra", "", "", "", 25,25, 50, 100, 200, 200, 200, 0), Space("Samus", "Mr Game & Watch", "Zero Suit Samus", "Go To Jail", "Ryu", "Terry", "PokeBall3", "Kazuya", "Byleth", "AssistTrophy3", "Pyra", "DLC Tax", "", "", "", 22, 110, 330, 800, 975, 1150, 260, 150), Space("Dark Samus", "Zero Suit Samus", "Go To Jail", "Ryu", "Terry", "PokeBall3", "Kazuya", "Byleth", "AssistTrophy3", "Pyra", "DLC Tax", "Mythra", "", "", "", 22, 110, 330, 800, 975, 1150, 260, 150), Space("Mr Game & Watch", "Go To Jail", "Ryu", "Terry", "PokeBall3", "Kazuya", "Byleth", "AssistTrophy3", "Pyra", "DLC Tax", "Mythra", "Go", "", "", "", 4, 4, 4, 4, 4, 4, 150, 0), Space("Zero Suit Samus", "Ryu", "Terry", "PokeBall3", "Kazuya", "Byleth", "AssistTrophy3", "Pyra", "DLC Tax", "Mythra", "Go", "Ganondorf", "", "", "", 24, 120, 360, 850, 1025, 1200, 280, 150), Space("Go To Jail", "Terry", "PokeBall3", "Kazuya", "Byleth", "AssistTrophy3", "Pyra", "DLC Tax", "Mythra", "Go", "Ganondorf", "PokeBall1", "", "", "", 0, 0, 0, 0,0 ,0, 0, 0), Space("Ryu", "PokeBall3", "Kazuya", "Byleth", "AssistTrophy3", "Pyra", "DLC Tax", "Mythra", "Go", "Ganondorf", "PokeBall1", "Little Mac", "", "", "", 26, 130, 390, 900, 1100, 1275, 300, 200), Space("Terry", "Kazuya", "Byleth", "AssistTrophy3", "Pyra", "DLC Tax", "Mythra", "Go", "Ganondorf", "PokeBall1", "Little Mac", "Low Tier Tax", "", "", "", 26, 130, 390, 900, 1100, 1275, 300, 200), Space("PokeBall3", "Byleth", "AssistTrophy3", "Pyra", "DLC Tax", "Mythra", "Go", "Ganondorf", "PokeBall1", "Little Mac", "Low Tier Tax", "Marth", "", "", "", 0, 0, 0, 0,0 ,0, 0, 0), Space("Kazuya", "AssistTrophy3", "Pyra", "DLC Tax", "Mythra", "Go", "Ganondorf", "PokeBall1", "Little Mac", "Low Tier Tax", "Marth", "King Dedede", "", "", "", 28, 150, 450, 1000, 1200, 1400, 300, 200), Space("Byleth", "Pyra", "DLC Tax", "Mythra", "Go", "Ganondorf", "PokeBall1", "Little Mac", "Low Tier Tax", "Marth", "King Dedede", "AssistTrophy1", "", "", "", 25, 25, 50, 100, 200, 200, 200, 0), Space("AssistTrophy3", "DLC Tax", "Mythra", "Go", "Ganondorf", "PokeBall1", "Little Mac", "Low Tier Tax", "Marth", "King Dedede", "AssistTrophy1", "Kirby", "PokeBall3", "Pac Man","Marth", 0, 0, 0,0 ,0 ,0, 0, 0), Space("Pyra", "Mythra", "Go", "Ganondorf", "PokeBall1", "Little Mac", "Low Tier Tax", "Marth", "King Dedede", "AssistTrophy1", "Kirby", "Meta Knight", "", "", "", 35, 175, 500, 1100, 1300, 1500, 350, 200), Space("DLC Tax", "Go", "Ganondorf", "PokeBall1", "Little Mac", "Low Tier Tax", "Marth", "King Dedede", "AssistTrophy1", "Kirby", "Meta Knight", "Jail", "", "", "", 100, 0, 0, 0,0 ,0, 0, 0), Space("Mythra", "Ganondorf", "PokeBall1", "Little Mac", "Low Tier Tax", "Marth", "King Dedede", "AssistTrophy1", "Kirby", "Meta Knight", "Jail", "Jigglypuff", "", "", "", 50, 200, 600, 1400, 1700, 2000, 400, 200)]
p1Img = pygame.image.load('1Num.png').convert()
p1Img = pygame.transform.scale(p1Img, (30, 30))
font = pygame.font.SysFont('timesnewroman.ttf', 16)
smallFont = pygame.font.SysFont('timesnewroman.ttf', 13)
imageModifier = ImageModifier()
pygame.draw.rect(monopolyBoard, LIGHTGREEN, [0, 0, 1000, 1000])
pygame.draw.rect(monopolyBoard, BLACK, [0, 0, 140, 140], 1)
pygame.draw.rect(monopolyBoard, BLACK, [860, 860, 140, 140], 1)
pygame.draw.rect(monopolyBoard, BLACK, [0, 860, 140, 140], 1)
pygame.draw.rect(monopolyBoard, BLACK, [860, 0, 140, 140], 1)
for i in range(0, 9):
    pygame.draw.rect(monopolyBoard, BLACK, [0, 140 + i*80, 140, 80], 1)
    pygame.draw.rect(monopolyBoard, BLACK, [140 + i*80, 0, 80, 140], 1)
    pygame.draw.rect(monopolyBoard, BLACK, [860, 140 + i*80, 140, 80], 1)
    pygame.draw.rect(monopolyBoard, BLACK, [140 + i*80, 860, 80, 140], 1)

pygame.draw.rect(monopolyBoard, BROWN, [782, 860, 76, 20])
pygame.draw.rect(monopolyBoard, BROWN, [622, 860, 76, 20])
pygame.draw.rect(monopolyBoard, LIGHTBLUE, [142, 860, 76, 20])
pygame.draw.rect(monopolyBoard, LIGHTBLUE, [222, 860, 76, 20])
pygame.draw.rect(monopolyBoard, LIGHTBLUE, [382, 860, 76, 20])
pygame.draw.rect(monopolyBoard, MAGENTA, [120, 782, 20, 76])
pygame.draw.rect(monopolyBoard, MAGENTA, [120, 622, 20, 76])
pygame.draw.rect(monopolyBoard, MAGENTA, [120, 542, 20, 76])
pygame.draw.rect(monopolyBoard, ORANGE, [120, 142, 20, 76])
pygame.draw.rect(monopolyBoard, ORANGE, [120, 222, 20, 76])
pygame.draw.rect(monopolyBoard, ORANGE, [120, 382, 20, 76])
pygame.draw.rect(monopolyBoard, RED, [142, 120, 76, 20])
pygame.draw.rect(monopolyBoard, RED, [302, 120, 76, 20])
pygame.draw.rect(monopolyBoard, RED, [382, 120, 76, 20])
pygame.draw.rect(monopolyBoard, YELLOW, [542, 120, 76, 20])
pygame.draw.rect(monopolyBoard, YELLOW, [622, 120, 76, 20])
pygame.draw.rect(monopolyBoard, YELLOW, [782, 120, 76, 20])
pygame.draw.rect(monopolyBoard, GREEN, [860, 142, 20, 76])
pygame.draw.rect(monopolyBoard, GREEN, [860, 222, 20, 76])
pygame.draw.rect(monopolyBoard, GREEN, [860, 382, 20, 76])
pygame.draw.rect(monopolyBoard, DARKBLUE, [860, 622, 20, 76])
pygame.draw.rect(monopolyBoard, DARKBLUE, [860, 782, 20, 76])
monopolyCenter = pygame.image.load('monopolyCenter.png').convert()
monopolyCenter = pygame.transform.scale(monopolyCenter, (720, 720))
toJailImg = pygame.image.load('goToJail.png').convert()
toJailImg = pygame.transform.scale(toJailImg, (138, 138))
goImg = pygame.image.load('go.png').convert()
goImg = pygame.transform.scale(goImg, (140, 140))
fpImg = pygame.image.load('freeParking.png').convert()
fpImg = pygame.transform.scale(fpImg, (140, 140))
jailImg = pygame.image.load('jail.png').convert()
jailImg = pygame.transform.scale(jailImg, (138, 138))
assistTrophyImg = pygame.image.load('SSBU_Assist_Trophy_Render.png')
assistTrophyImg = pygame.transform.scale(assistTrophyImg, (50, 85))
assistTrophyTextImg = pygame.image.load('assistTrophyWithText.png')
assistTrophyTextImg = pygame.transform.scale(assistTrophyTextImg, (70, 85))
rotated180AssistTrophyTextImg = pygame.transform.rotate(
    assistTrophyTextImg, 180)
rotated90AssistTrophyTextImg = pygame.transform.rotate(assistTrophyTextImg, 90)
pokeBallImg = pygame.image.load('pokeBallWithText.png')
pokeBallImg = pygame.transform.scale(pokeBallImg, (65, 80))
rotated90PokeBallImg = pygame.transform.rotate(pokeBallImg, 90)
rotated270PokeBallImg = pygame.transform.rotate(pokeBallImg, 270)
macImg = pygame.image.load('littleMac.png').convert()
macImg = pygame.transform.scale(macImg, (70, 90))
macText = font.render('Little Mac', True, BLACK)
macText2 = font.render('$60', True, BLACK)
macRect = macText.get_rect()
macRect2 = macText2.get_rect()
macRect.center = (660, 890)
macRect2.center = (655, 985)
monopolyBoard.blit(macText, macRect)
monopolyBoard.blit(macImg, (625, 895))
monopolyBoard.blit(macText2, macRect2)

ganonImg = pygame.image.load('ganon.png').convert()
ganonImg = pygame.transform.scale(ganonImg, (55, 85))
ganonText = font.render('Ganondorf', True, BLACK)
ganonText2 = font.render('$60', True, BLACK)
ganonRect = ganonText.get_rect()
ganonRect2 = ganonText2.get_rect()
ganonRect.center = (820, 890)
ganonRect2.center = (815, 985)
monopolyBoard.blit(ganonText, ganonRect)
monopolyBoard.blit(ganonImg, (790, 895))
monopolyBoard.blit(ganonText2, ganonRect2)

dededeImg = pygame.image.load('dedede.png').convert()
dededeImg = pygame.transform.scale(dededeImg, (60, 85))
dededeText = font.render('King Dedede', True, BLACK)
dededeText2 = font.render('$100', True, BLACK)
dededeRect = dededeText.get_rect()
dededeRect2 = dededeText2.get_rect()
dededeRect.center = (420, 890)
dededeRect2.center = (415, 985)
monopolyBoard.blit(dededeText, dededeRect)
monopolyBoard.blit(dededeImg, (385, 895))
monopolyBoard.blit(dededeText2, dededeRect2)

kirbyImg = pygame.image.load('kirby.png').convert()
kirbyImg = pygame.transform.scale(kirbyImg, (50, 75))
kirbyText = font.render('Kirby', True, BLACK)
kirbyText2 = font.render('$100', True, BLACK)
kirbyRect = kirbyText.get_rect()
kirbyRect2 = kirbyText2.get_rect()
kirbyRect.center = (255, 890)
kirbyRect2.center = (255, 985)
monopolyBoard.blit(kirbyText, kirbyRect)
monopolyBoard.blit(kirbyImg, (235, 900))
monopolyBoard.blit(kirbyText2, kirbyRect2)

metaKnightImg = pygame.image.load('Meta Knight.png').convert()
metaKnightImg = pygame.transform.scale(metaKnightImg, (60, 85))
metaKnightText = font.render('Meta Knight', True, BLACK)
metaKnightText2 = font.render('$120', True, BLACK)
metaKnightRect = metaKnightText.get_rect()
metaKnightRect2 = metaKnightText2.get_rect()
metaKnightRect.center = (180, 890)
metaKnightRect2.center = (175, 985)
monopolyBoard.blit(metaKnightText, metaKnightRect)
monopolyBoard.blit(metaKnightImg, (150, 895))
monopolyBoard.blit(metaKnightText2, metaKnightRect2)

monopolyBoard.blit(imageModifier.space_modifier('jigglypuff.png', 70, 105, 270), (10, 785))
monopolyBoard.blit(imageModifier.space_modifier('pacman.png', 70, 105, 270), (10, 705))
monopolyBoard.blit(imageModifier.space_modifier('mewtwo.png', 70, 105, 270), (10, 625))
monopolyBoard.blit(imageModifier.space_modifier('incineroar.png', 70, 105, 270), (10, 545))
monopolyBoard.blit(imageModifier.space_modifier('ike.png', 70, 105, 270), (10, 465))
monopolyBoard.blit(imageModifier.space_modifier('yLink.png', 70, 105, 270), (10, 385))
monopolyBoard.blit(imageModifier.space_modifier('tLink.png', 70, 105, 270), (10, 225))
monopolyBoard.blit(imageModifier.space_modifier('link.png', 70, 105, 270), (10, 145))
monopolyBoard.blit(imageModifier.space_modifier('falco.png', 70, 105, 180), (145, 10))
monopolyBoard.blit(imageModifier.space_modifier('wolf.png', 70, 105, 180), (305, 10))
monopolyBoard.blit(imageModifier.space_modifier('fox.png', 70, 105, 180), (385, 10))
monopolyBoard.blit(imageModifier.space_modifier('roy.png', 70, 105, 180), (465, 10))
monopolyBoard.blit(imageModifier.space_modifier('samus.png', 60, 105, 180), (550, 10))
monopolyBoard.blit(imageModifier.space_modifier('darkSamus.png', 65, 105, 180), (630, 10))
monopolyBoard.blit(imageModifier.space_modifier('g&w.png', 65, 105, 180), (710, 10))
monopolyBoard.blit(imageModifier.space_modifier('zss.png', 65, 105, 180), (790, 10))
monopolyBoard.blit(imageModifier.space_modifier('ryu.png', 70, 105, 90), (885, 145))
monopolyBoard.blit(imageModifier.space_modifier('terry.png', 70, 105, 90), (885, 225))
monopolyBoard.blit(imageModifier.space_modifier('byleth.png', 70, 120, 90), (870, 465))
monopolyBoard.blit(imageModifier.space_modifier('kazuya.png', 70, 105, 90), (885, 385))
monopolyBoard.blit(imageModifier.space_modifier('pyra.png', 70, 105, 90), (885, 625))
monopolyBoard.blit(imageModifier.space_modifier('steve.png', 70, 115, 90), (870, 705))
monopolyBoard.blit(imageModifier.space_modifier('mythra.png', 70, 105, 90), (885, 785))

marthImg = pygame.image.load('marth.png').convert()
marthImg = pygame.transform.scale(marthImg, (70, 75))
marthText = font.render('Marth', True, BLACK)
marthText2 = font.render('$200', True, BLACK)
marthRect = marthText.get_rect()
marthRect2 = marthText2.get_rect()
marthRect.center = (500, 885)
marthRect2.center = (500, 985)
monopolyBoard.blit(marthText, marthRect)
monopolyBoard.blit(marthImg, (465, 895))
monopolyBoard.blit(marthText2, marthRect2)

dkImg = pygame.image.load('dkFace.png').convert()
dkImg = pygame.transform.scale(dkImg, (60, 85))
dkText = font.render('Low Tier Tax', True, BLACK)
dkText2 = font.render('Pay $200', True, BLACK)
dkRect = dkText.get_rect()
dkRect2 = dkText2.get_rect()
dkRect.center = (580, 890)
dkRect2.center = (575, 985)
monopolyBoard.blit(dkText, dkRect)
monopolyBoard.blit(dkImg, (550, 895))
monopolyBoard.blit(dkText2, dkRect2)
"""text = font.render('Poke Ball', True, BLACK)
textRect = text.get_rect()
textRect.center = (740, 900)
monopolyBoard.blit(pokeBallImg, (695, 905))
monopolyBoard.blit(text, textRect)"""


monopolyBoard.blit(monopolyCenter, (140, 140))
monopolyBoard.blit(toJailImg, (860, 0))
monopolyBoard.blit(goImg, (860, 860))
monopolyBoard.blit(fpImg, (0, 0))
monopolyBoard.blit(jailImg, (0, 860))
monopolyBoard.blit(assistTrophyTextImg, (305, 895))
monopolyBoard.blit(rotated180AssistTrophyTextImg, (225, 30))
monopolyBoard.blit(rotated90AssistTrophyTextImg, (885, 545))
monopolyBoard.blit(pokeBallImg, (705, 890))
monopolyBoard.blit(rotated90PokeBallImg, (880, 310))
monopolyBoard.blit(rotated270PokeBallImg, (40, 310))

#player info    
pygame.draw.rect(monopolyBoard, WHITE, [225, 400, 150, 75])
p1Text = font.render(players[0].playerName + "\nCash: " + str(players[0].money), True, BLACK)
monopolyBoard.blit(p1Text, (230, 410))
pygame.draw.rect(monopolyBoard, WHITE, [500, 400, 150, 75])
p2Text = font.render(players[1].playerName + "\nCash: " + str(players[1].money), True, BLACK)
monopolyBoard.blit(p2Text, (505, 410))
if len(players) >= 3:
    pygame.draw.rect(monopolyBoard, WHITE, [225, 600, 150, 75])
    p3Text = font.render(players[2].playerName + "\nCash: " + str(players[2].money), True, BLACK)
    monopolyBoard.blit(p3Text, (230, 610))
    if len(players) >= 4:
        pygame.draw.rect(monopolyBoard, WHITE, [500, 600, 150, 75])
        p2Text = font.render(players[3].playerName + "\nCash: " + str(players[3].money), True, BLACK)
        monopolyBoard.blit(p2Text, (505, 610))
pygame.display.update()

while gaming:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            pygame.quit()
        elif event.type == KEYDOWN:
            pygame.draw.rect(monopolyBoard, LIGHTGREEN, [0, 0, 1000, 1000])
            pygame.draw.rect(monopolyBoard, BLACK, [0, 0, 140, 140], 1)
            pygame.draw.rect(monopolyBoard, BLACK, [860, 860, 140, 140], 1)
            pygame.draw.rect(monopolyBoard, BLACK, [0, 860, 140, 140], 1)
            pygame.draw.rect(monopolyBoard, BLACK, [860, 0, 140, 140], 1)
            for i in range(0, 9):
                pygame.draw.rect(monopolyBoard, BLACK, [0, 140 + i*80, 140, 80], 1)
                pygame.draw.rect(monopolyBoard, BLACK, [140 + i*80, 0, 80, 140], 1)
                pygame.draw.rect(monopolyBoard, BLACK, [
                                 860, 140 + i*80, 140, 80], 1)
                pygame.draw.rect(monopolyBoard, BLACK, [
                                 140 + i*80, 860, 80, 140], 1)
                pygame.draw.rect(monopolyBoard, BROWN, [782, 860, 76, 20])
                pygame.draw.rect(monopolyBoard, BROWN, [622, 860, 76, 20])
                pygame.draw.rect(monopolyBoard, LIGHTBLUE, [142, 860, 76, 20])
                pygame.draw.rect(monopolyBoard, LIGHTBLUE, [222, 860, 76, 20])
                pygame.draw.rect(monopolyBoard, LIGHTBLUE, [382, 860, 76, 20])
                pygame.draw.rect(monopolyBoard, MAGENTA, [120, 782, 20, 76])
                pygame.draw.rect(monopolyBoard, MAGENTA, [120, 622, 20, 76])
                pygame.draw.rect(monopolyBoard, MAGENTA, [120, 542, 20, 76])
                pygame.draw.rect(monopolyBoard, ORANGE, [120, 142, 20, 76])
                pygame.draw.rect(monopolyBoard, ORANGE, [120, 222, 20, 76])
                pygame.draw.rect(monopolyBoard, ORANGE, [120, 382, 20, 76])
                pygame.draw.rect(monopolyBoard, RED, [142, 120, 76, 20])
                pygame.draw.rect(monopolyBoard, RED, [302, 120, 76, 20])
                pygame.draw.rect(monopolyBoard, RED, [382, 120, 76, 20])
                pygame.draw.rect(monopolyBoard, YELLOW, [542, 120, 76, 20])
                pygame.draw.rect(monopolyBoard, YELLOW, [622, 120, 76, 20])
                pygame.draw.rect(monopolyBoard, YELLOW, [782, 120, 76, 20])
                pygame.draw.rect(monopolyBoard, GREEN, [860, 142, 20, 76])
                pygame.draw.rect(monopolyBoard, GREEN, [860, 222, 20, 76])
                pygame.draw.rect(monopolyBoard, GREEN, [860, 382, 20, 76])
                pygame.draw.rect(monopolyBoard, DARKBLUE, [860, 622, 20, 76])
                pygame.draw.rect(monopolyBoard, DARKBLUE, [860, 782, 20, 76])
            monopolyBoard.blit(macText, macRect)
            monopolyBoard.blit(macImg, (625, 895))
            monopolyBoard.blit(macText2, macRect2)
            monopolyBoard.blit(ganonText, ganonRect)
            monopolyBoard.blit(ganonImg, (790, 895))
            monopolyBoard.blit(ganonText2, ganonRect2)
            monopolyBoard.blit(dededeText, dededeRect)
            monopolyBoard.blit(dededeImg, (385, 895))
            monopolyBoard.blit(dededeText2, dededeRect2)
            monopolyBoard.blit(kirbyText, kirbyRect)
            monopolyBoard.blit(kirbyImg, (235, 900))
            monopolyBoard.blit(kirbyText2, kirbyRect2)
            monopolyBoard.blit(metaKnightText, metaKnightRect)
            monopolyBoard.blit(metaKnightImg, (150, 895))
            monopolyBoard.blit(metaKnightText2, metaKnightRect2)

            monopolyBoard.blit(imageModifier.space_modifier('jigglypuff.png', 70, 105, 270), (10, 785))
            monopolyBoard.blit(imageModifier.space_modifier('pacman.png', 70, 105, 270), (10, 705))
            monopolyBoard.blit(imageModifier.space_modifier('mewtwo.png', 70, 105, 270), (10, 625))
            monopolyBoard.blit(imageModifier.space_modifier('incineroar.png', 70, 105, 270), (10, 545))
            monopolyBoard.blit(imageModifier.space_modifier('ike.png', 70, 105, 270), (10, 465))
            monopolyBoard.blit(imageModifier.space_modifier('yLink.png', 70, 105, 270), (10, 385))
            monopolyBoard.blit(imageModifier.space_modifier('tLink.png', 70, 105, 270), (10, 225))
            monopolyBoard.blit(imageModifier.space_modifier('link.png', 70, 105, 270), (10, 145))
            monopolyBoard.blit(imageModifier.space_modifier('falco.png', 70, 105, 180), (145, 10))
            monopolyBoard.blit(imageModifier.space_modifier('wolf.png', 70, 105, 180), (305, 10))
            monopolyBoard.blit(imageModifier.space_modifier('fox.png', 70, 105, 180), (385, 10))
            monopolyBoard.blit(imageModifier.space_modifier('roy.png', 70, 105, 180), (465, 10))
            monopolyBoard.blit(imageModifier.space_modifier('samus.png', 60, 105, 180), (550, 10))
            monopolyBoard.blit(imageModifier.space_modifier('darkSamus.png', 65, 105, 180), (630, 10))
            monopolyBoard.blit(imageModifier.space_modifier('g&w.png', 65, 105, 180), (710, 10))
            monopolyBoard.blit(imageModifier.space_modifier('zss.png', 65, 105, 180), (790, 10))
            monopolyBoard.blit(imageModifier.space_modifier('ryu.png', 70, 105, 90), (885, 145))
            monopolyBoard.blit(imageModifier.space_modifier('terry.png', 70, 105, 90), (885, 225))
            monopolyBoard.blit(imageModifier.space_modifier('byleth.png', 70, 120, 90), (870, 465))
            monopolyBoard.blit(imageModifier.space_modifier('kazuya.png', 70, 105, 90), (885, 385))
            monopolyBoard.blit(imageModifier.space_modifier('pyra.png', 70, 105, 90), (885, 625))
            monopolyBoard.blit(imageModifier.space_modifier('steve.png', 70, 115, 90), (870, 705))
            monopolyBoard.blit(imageModifier.space_modifier('mythra.png', 70, 105, 90), (885, 785))

            monopolyBoard.blit(marthText, marthRect)
            monopolyBoard.blit(marthImg, (465, 895))
            monopolyBoard.blit(marthText2, marthRect2)
            monopolyBoard.blit(dkText, dkRect)
            monopolyBoard.blit(dkImg, (550, 895))
            monopolyBoard.blit(dkText2, dkRect2)
            """text = font.render('Poke Ball', True, BLACK)
            textRect = text.get_rect()
            textRect.center = (740, 900)
            monopolyBoard.blit(pokeBallImg, (695, 905))
            monopolyBoard.blit(text, textRect)"""
    
            monopolyBoard.blit(monopolyCenter, (140, 140))
            monopolyBoard.blit(toJailImg, (860, 0))
            monopolyBoard.blit(goImg, (860, 860))
            monopolyBoard.blit(fpImg, (0, 0))
            monopolyBoard.blit(jailImg, (0, 860))
            monopolyBoard.blit(assistTrophyTextImg, (305, 895))
            monopolyBoard.blit(rotated180AssistTrophyTextImg, (225, 30))
            monopolyBoard.blit(rotated90AssistTrophyTextImg, (885, 545))
            monopolyBoard.blit(pokeBallImg, (705, 890))
            monopolyBoard.blit(rotated90PokeBallImg, (880, 310))
            monopolyBoard.blit(rotated270PokeBallImg, (40, 310))

            #player info    
            pygame.draw.rect(monopolyBoard, WHITE, [225, 400, 150, 50])
            p1Text = font.render(players[0].playerName + "\nCash: " + str(players[0].money), True, BLACK)
            monopolyBoard.blit(p1Text, (230, 410))
            pygame.draw.rect(monopolyBoard, WHITE, [500, 400, 150, 50])
            p2Text = font.render(players[1].playerName + "\nCash: " + str(players[1].money), True, BLACK)
            monopolyBoard.blit(p2Text, (505, 410))
            if len(players) >= 3:
                pygame.draw.rect(monopolyBoard, WHITE, [225, 600, 150, 50])
                p3Text = font.render(players[2].playerName + "\nCash: " + str(players[2].money), True, BLACK)
                monopolyBoard.blit(p3Text, (230, 610))
                if len(players) >= 4:
                    pygame.draw.rect(monopolyBoard, WHITE, [500, 600, 150, 50])
                    p2Text = font.render(players[3].playerName + "\nCash: " + str(players[3].money), True, BLACK)
                    monopolyBoard.blit(p2Text, (505, 610))
            p1MvmtClass.rollDice()
            if p1MvmtClass.currentSpace.spaceName == "Go":
                monopolyBoard.blit(p1Img, (940, 960))
            elif p1MvmtClass.currentSpace.spaceName == "Little Mac":
                monopolyBoard.blit(p1Img, (820, 960))
            elif p1MvmtClass.currentSpace.spaceName == "PokeBall1":
                monopolyBoard.blit(p1Img, (740, 960))
                drawPiles.drawPokeBall(players[0], players, spaces)
            elif p1MvmtClass.currentSpace.spaceName == "Ganondorf":
                monopolyBoard.blit(p1Img, (660, 960))
            elif p1MvmtClass.currentSpace.spaceName == "Low Tier Tax":
                monopolyBoard.blit(p1Img, (580, 960))
            elif p1MvmtClass.currentSpace.spaceName == "Marth":
                monopolyBoard.blit(p1Img, (500, 960))
            elif p1MvmtClass.currentSpace.spaceName == "King Dedede":
                monopolyBoard.blit(p1Img, (420, 960))
            elif p1MvmtClass.currentSpace.spaceName == "AssistTrophy1":
                monopolyBoard.blit(p1Img, (340, 960))
                drawPiles.drawAssistTrophy(players[0], players, spaces)
            elif p1MvmtClass.currentSpace.spaceName == "Kirby":
                monopolyBoard.blit(p1Img, (260, 960))
            elif p1MvmtClass.currentSpace.spaceName == "Meta Knight":
                monopolyBoard.blit(p1Img, (180, 960))
            elif p1MvmtClass.currentSpace.spaceName == "Jail" or p1MvmtClass.currentSpace.spaceName == "Go To Jail":
                monopolyBoard.blit(p1Img, (10, 970))
            elif p1MvmtClass.currentSpace.spaceName == "Jigglypuff":
                monopolyBoard.blit(p1Img, (80, 810))
            elif p1MvmtClass.currentSpace.spaceName == "Pac Man":
                monopolyBoard.blit(p1Img, (80, 730))
            elif p1MvmtClass.currentSpace.spaceName == "Mewtwo":
                monopolyBoard.blit(p1Img, (80, 650))
            elif p1MvmtClass.currentSpace.spaceName == "Incineroar":
                monopolyBoard.blit(p1Img, (80, 570))
            elif p1MvmtClass.currentSpace.spaceName == "Ike":
                monopolyBoard.blit(p1Img, (80, 490))
            elif p1MvmtClass.currentSpace.spaceName == "Young Link":
                monopolyBoard.blit(p1Img, (80, 410))
            elif p1MvmtClass.currentSpace.spaceName == "PokeBall2":
                monopolyBoard.blit(p1Img, (80, 330))
                drawPiles.drawPokeBall(players[0], players, spaces)
            elif p1MvmtClass.currentSpace.spaceName == "Toon Link":
                monopolyBoard.blit(p1Img, (80, 250))
            elif p1MvmtClass.currentSpace.spaceName == "Link":
                monopolyBoard.blit(p1Img, (80, 170))
            elif p1MvmtClass.currentSpace.spaceName == "Free Parking":
                monopolyBoard.blit(p1Img, (80, 80))
            elif p1MvmtClass.currentSpace.spaceName == "Falco":
                monopolyBoard.blit(p1Img, (160, 80))
            elif p1MvmtClass.currentSpace.spaceName == "AssistTrophy2":
                monopolyBoard.blit(p1Img, (240, 80))
                drawPiles.drawAssistTrophy(players[0], players, spaces)
            elif p1MvmtClass.currentSpace.spaceName == "Wolf":
                monopolyBoard.blit(p1Img, (320, 80))
            elif p1MvmtClass.currentSpace.spaceName == "Fox":
                monopolyBoard.blit(p1Img, (400, 80))
            elif p1MvmtClass.currentSpace.spaceName == "Roy":
                monopolyBoard.blit(p1Img, (480, 80))
            elif p1MvmtClass.currentSpace.spaceName == "Samus":
                monopolyBoard.blit(p1Img, (560, 80))
            elif p1MvmtClass.currentSpace.spaceName == "Dark Samus":
                monopolyBoard.blit(p1Img, (640, 80))
            elif p1MvmtClass.currentSpace.spaceName == "Mr Game & Watch":
                monopolyBoard.blit(p1Img, (720, 80))
            elif p1MvmtClass.currentSpace.spaceName == "Zero Suit Samus":
                monopolyBoard.blit(p1Img, (800, 80))
            elif p1MvmtClass.currentSpace.spaceName == "Ryu":
                monopolyBoard.blit(p1Img, (940, 180))
            elif p1MvmtClass.currentSpace.spaceName == "Terry":
                monopolyBoard.blit(p1Img, (940, 260))
            elif p1MvmtClass.currentSpace.spaceName == "PokeBall3":
                monopolyBoard.blit(p1Img, (940, 340))
                drawPiles.drawPokeBall(players[0], players, spaces)
            elif p1MvmtClass.currentSpace.spaceName == "Kazuya":
                monopolyBoard.blit(p1Img, (940, 420))
            elif p1MvmtClass.currentSpace.spaceName == "Byleth":
                monopolyBoard.blit(p1Img, (940, 500))
            elif p1MvmtClass.currentSpace.spaceName == "AssistTrophy3":
                monopolyBoard.blit(p1Img, (940, 580))
                drawPiles.drawAssistTrophy(players[0], players, spaces)
            elif p1MvmtClass.currentSpace.spaceName == "Pyra":
                monopolyBoard.blit(p1Img, (940, 660))
            elif p1MvmtClass.currentSpace.spaceName == "DLC Tax":
                monopolyBoard.blit(p1Img, (940, 740))
            elif p1MvmtClass.currentSpace.spaceName == "Mythra":
                monopolyBoard.blit(p1Img, (940, 820))

            pygame.display.update()

