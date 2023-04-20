# Monopoly state machine
import pygame
from pygame.locals import *
from SpaceClass import Space
from ImageModifier import ImageModifier
import GameWindows
from Player import Player
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
BLUE = (0, 0, 255)
GREEN = (0, 53, 24)
DARKBLUE = (0, 0, 255)
LIGHTGREEN = (191, 219, 174)
gaming = True
pygame.init()
monopolyBoard = pygame.display.set_mode((BOARDWIDTH, BOARDHEIGHT))
gameWindows = GameWindows.gameWindows(monopolyBoard)
numPlayers = gameWindows.playerSelectWindow()
print("Num Players is:" + str(numPlayers))
players = []
playerNames = gameWindows.playerNamesScreen(numPlayers)
for i in range(numPlayers):
    players.append(Player(playerNames[i], i+1))
spaces=[Space("Go", "PokeBall1", "Little Mac", "Low Tier Tax", "Marth", "King Dedede", "AssistTrophy1", "Kirby", "Meta Knight", "Jail", "Jigglypuff", "Pac Man", "", "", "", 0, 0, 0, 0, 0, 0, 0, 0), Space("Ganondorf", "Little Mac", "Low Tier Tax", "Marth", "King Dedede", "AssistTrophy1", "Kirby", "Meta Knight", "Jail", "Jigglypuff", "Pac Man", "Mewtwo", "", "", "", 2, 10, 30, 90, 160, 250, 60, 50), Space("PokeBall1", "Low Tier Tax", "Marth", "King Dedede", "AssistTrophy1", "Kirby", "Meta Knight", "Jail", "Jigglypuff", "Pac Man", "Mewtwo", "Incineroar", "", "", "", 0, 0, 0, 0, 0, 0, 0, 0), Space("Little Mac", "Marth", "King Dedede", "AssistTrophy1", "Kirby", "Meta Knight", "Jail", "Jigglypuff", "Pac Man", "Mewtwo", "Incineroar", "Ike", "", "", "", 4, 20, 60, 180, 320, 450, 60, 50), Space("Low Tier Tax", "King Dedede", "AssistTrophy1", "Kirby", "Meta Knight", "Jail", "Jigglypuff", "Pac Man", "Mewtwo", "Incineroar", "Ike", "Young Link", "", "", "", 200, 0, 0, 0, 0, 0, 0, 0), Space("Marth", "AssistTrophy1", "Kirby", "Meta Knight", "Jail", "Jigglypuff", "Pac Man", "Mewtwo", "Incineroar", "Ike", "Young Link", "PokeBall2", "", "", "", 25, 25, 50, 100, 200, 200, 200, 0), Space("King Dedede", "Kirby", "Meta Knight", "Jail", "Jigglypuff", "Pac Man", "Mewtwo", "Incineroar", "Ike", "Young Link", "PokeBall2", "Toon Link", "", "", "", 6, 30, 90, 270, 440, 550, 100, 50), Space("AssistTrophy1", "Meta Knight", "Jail", "Jigglypuff", "Pac Man", "Mewtwo", "Incineroar", "Ike", "Young Link", "PokeBall2", "Toon Link", "Link", "Low Tier Tax", "Pac Man", "Marth", 0, 0, 0,0, 0, 0, 0, 0), Space("Kirby", "Jail", "Jigglypuff", "Pac Man", "Mewtwo", "Incineroar", "Ike", "Young Link", "PokeBall2", "Toon Link", "Link", "Free Parking", "", "", "", 6, 30, 90, 270, 400, 550, 100, 50), Space("Meta Knight", "Jigglypuff", "Pac Man", "Mewtwo", "Incineroar", "Ike", "Young Link", "PokeBall2", "Toon Link", "Link", "Free Parking", "Falco", "", "", "", 8, 40, 100, 300, 450, 600, 120, 50), Space("Jail", "Pac Man", "Mewtwo", "Incineroar", "Ike", "Young Link", "PokeBall2", "Toon Link", "Link", "Free Parking", "Falco", "AssistTrophy2", "", "", "", 0, 0, 0, 0,0 ,0 ,0, 0), Space("Jigglypuff", "Mewtwo", "Incineroar", "Ike", "Young Link", "PokeBall2", "Toon Link", "Link", "Free Parking", "Falco", "AssistTrophy2", "Wolf", "", "", "", 10, 50, 150, 450, 625, 750, 140, 100), Space("Pac Man", "Incineroar", "Ike", "Young Link", "PokeBall2", "Toon Link", "Link", "Free Parking", "Falco", "AssistTrophy2", "Wolf", "Fox", "", "", "", 4, 4, 4, 4, 4, 4, 150, 0), Space("Mewtwo", "Ike", "Young Link", "PokeBall2", "Toon Link", "Link", "Free Parking", "Falco", "AssistTrophy2", "Wolf", "Fox", "Roy", "", "", "", 10, 50, 150, 450, 625, 750, 140, 100), Space("Incineroar", "Young Link", "PokeBall2", "Toon Link", "Link", "Free Parking", "Falco", "AssistTrophy2", "Wolf", "Fox", "Roy", "Samus", "", "", "", 12, 60, 180, 500, 700, 900, 160, 100), Space("Ike", "PokeBall2", "Toon Link", "Link", "Free Parking", "Falco", "AssistTrophy2", "Wolf", "Fox", "Roy", "Samus", "Dark Samus", "", "", "", 25, 25, 50, 100, 200, 200, 200, 0), Space("Young Link", "Toon Link", "Link", "Free Parking", "Falco", "AssistTrophy2", "Wolf", "Fox", "Roy", "Samus", "Dark Samus", "Mr Game & Watch", "", "", "", 14, 70, 200, 550, 750, 950, 180, 100), Space("PokeBall2", "Link", "Free Parking", "Falco", "AssistTrophy2", "Wolf", "Fox", "Roy", "Samus", "Dark Samus", "Mr Game & Watch", "Zero Suit Samus", "", "", "", 0, 0, 0, 0, 0, 0, 0, 0), Space("Toon Link", "Free Parking", "Falco", "AssistTrophy2", "Wolf", "Fox", "Roy", "Samus", "Dark Samus", "Mr Game & Watch", "Zero Suit Samus", "Go To Jail", "", "", "", 14, 70, 200, 550, 750, 950, 180, 100), Space("Link", "Falco", "AssistTrophy2", "Wolf", "Fox", "Roy", "Samus", "Dark Samus", "Mr Game & Watch", "Zero Suit Samus", "Go To Jail", "Ryu", "", "", "", 16, 80, 220, 600, 800, 1000, 200, 100), Space("Free Parking", "AssistTrophy2", "Wolf", "Fox", "Roy", "Samus", "Dark Samus", "Mr Game & Watch", "Zero Suit Samus", "Go To Jail", "Ryu", "Terry", "", "", "", 0, 0, 0, 0, 0, 0, 0, 0), Space("Falco", "Wolf", "Fox", "Roy", "Samus", "Dark Samus", "Mr Game & Watch", "Zero Suit Samus", "Go To Jail", "Ryu", "Terry", "PokeBall3", "", "", "", 18, 90, 250, 700, 875, 1050, 220, 150), Space("AssistTrophy2", "Fox", "Roy", "Samus", "Dark Samus", "Mr Game & Watch", "Zero Suit Samus", "Go To Jail", "Ryu", "Terry", "PokeBall3", "Kazuya", "Link", "Mr Game & Watch", "Roy", 0, 0, 0, 0, 0, 0, 0, 0), Space("Wolf", "Roy", "Samus", "Dark Samus", "Mr Game & Watch", "Zero Suit Samus", "Go To Jail", "Ryu", "Terry", "PokeBall3", "Kazuya", "Byleth", "", "", "", 18, 90, 250, 700, 875, 1050, 220, 150), Space("Fox", "Samus", "Dark Samus", "Mr Game & Watch", "Zero Suit Samus", "Go To Jail", "Ryu", "Terry", "PokeBall3", "Kazuya", "Byleth", "AssistTrophy3", "", "", "", 20, 100, 300, 750, 925, 1100, 240, 150), Space("Roy", "Dark Samus", "Mr Game & Watch", "Zero Suit Samus", "Go To Jail", "Ryu", "Terry", "PokeBall3", "Kazuya", "Byleth", "AssistTrophy3", "Pyra", "", "", "", 25,25, 50, 100, 200, 200, 200, 0), Space("Samus", "Mr Game & Watch", "Zero Suit Samus", "Go To Jail", "Ryu", "Terry", "PokeBall3", "Kazuya", "Byleth", "AssistTrophy3", "Pyra", "DLC Tax", "", "", "", 22, 110, 330, 800, 975, 1150, 260, 150), Space("Dark Samus", "Zero Suit Samus", "Go To Jail", "Ryu", "Terry", "PokeBall3", "Kazuya", "Byleth", "AssistTrophy3", "Pyra", "DLC Tax", "Mythra", "", "", "", 22, 110, 330, 800, 975, 1150, 260, 150), Space("Mr Game & Watch", "Go To Jail", "Ryu", "Terry", "PokeBall3", "Kazuya", "Byleth", "AssistTrophy3", "Pyra", "DLC Tax", "Mythra", "Go", "", "", "", 4, 4, 4, 4, 4, 4, 150, 0), Space("Zero Suit Samus", "Ryu", "Terry", "PokeBall3", "Kazuya", "Byleth", "AssistTrophy3", "Pyra", "DLC Tax", "Mythra", "Go", "Ganondorf", "", "", "", 24, 120, 360, 850, 1025, 1200, 280, 150), Space("Go To Jail", "Terry", "PokeBall3", "Kazuya", "Byleth", "AssistTrophy3", "Pyra", "DLC Tax", "Mythra", "Go", "Ganondorf", "PokeBall1", "", "", "", 0, 0, 0, 0,0 ,0, 0, 0), Space("Ryu", "PokeBall3", "Kazuya", "Byleth", "AssistTrophy3", "Pyra", "DLC Tax", "Mythra", "Go", "Ganondorf", "PokeBall1", "Little Mac", "", "", "", 26, 130, 390, 900, 1100, 1275, 300, 200), Space("Terry", "Kazuya", "Byleth", "AssistTrophy3", "Pyra", "DLC Tax", "Mythra", "Go", "Ganondorf", "PokeBall1", "Little Mac", "Low Tier Tax", "", "", "", 26, 130, 390, 900, 1100, 1275, 300, 200), Space("PokeBall3", "Byleth", "AssistTrophy3", "Pyra", "DLC Tax", "Mythra", "Go", "Ganondorf", "PokeBall1", "Little Mac", "Low Tier Tax", "Marth", "", "", "", 0, 0, 0, 0,0 ,0, 0, 0), Space("Kazuya", "AssistTrophy3", "Pyra", "DLC Tax", "Mythra", "Go", "Ganondorf", "PokeBall1", "Little Mac", "Low Tier Tax", "Marth", "King Dedede", "", "", "", 28, 150, 450, 1000, 1200, 1400, 300, 200), Space("Byleth", "Pyra", "DLC Tax", "Mythra", "Go", "Ganondorf", "PokeBall1", "Little Mac", "Low Tier Tax", "Marth", "King Dedede", "AssistTrophy1", "", "", "", 25, 25, 50, 100, 200, 200, 200, 0), Space("AssistTrophy3", "DLC Tax", "Mythra", "Go", "Ganondorf", "PokeBall1", "Little Mac", "Low Tier Tax", "Marth", "King Dedede", "AssistTrophy1", "Kirby", "PokeBall3", "Pac Man","Marth", 0, 0, 0,0 ,0 ,0, 0, 0), Space("Pyra", "Mythra", "Go", "Ganondorf", "PokeBall1", "Little Mac", "Low Tier Tax", "Marth", "King Dedede", "AssistTrophy1", "Kirby", "Meta Knight", "", "", "", 35, 175, 500, 1100, 1300, 1500, 350, 200), Space("DLC Tax", "Go", "Ganondorf", "PokeBall1", "Little Mac", "Low Tier Tax", "Marth", "King Dedede", "AssistTrophy1", "Kirby", "Meta Knight", "Jail", "", "", "", 100, 0, 0, 0,0 ,0, 0, 0), Space("Mythra", "Ganondorf", "PokeBall1", "Little Mac", "Low Tier Tax", "Marth", "King Dedede", "AssistTrophy1", "Kirby", "Meta Knight", "Jail", "Jigglypuff", "", "", "", 50, 200, 600, 1400, 1700, 2000, 400, 200)]
drawPiles = cardStacks(numPlayers, spaces, monopolyBoard)  
for player in players:
    player.currentSpace = spaces[0]
    player.spaces = spaces
playerIndex = 0
activePlayer = players[playerIndex]
p1Img = pygame.image.load('1Num.png').convert()
p1Img = pygame.transform.scale(p1Img, (20, 20))
p2Img = pygame.image.load('2Num.png').convert()
p2Img = pygame.transform.scale(p2Img, (20, 20))
p3Img = pygame.image.load('3Num.png').convert()
p3Img = pygame.transform.scale(p3Img, (20, 20))
p4Img = pygame.image.load('4Num.png').convert()
p4Img = pygame.transform.scale(p4Img, (20, 20))
font = pygame.font.SysFont('timesnewroman.ttf', 16)
smallFont = pygame.font.SysFont('timesnewroman.ttf', 13)
imageModifier = ImageModifier()
monopolyCenter = imageModifier.space_modifier('monopolyCenter.png', 720, 720, 0)
toJailImg = imageModifier.space_modifier('goToJail.png', 138, 138, 0)
goImg = imageModifier.space_modifier('go.png', 140, 140, 0)
fpImg = imageModifier.space_modifier('freeParking.png', 140, 140, 0)
jailImg = imageModifier.space_modifier('jail.png', 140, 140, 0)
#assistTrophyImg = imageModifier.space_modifier('SSBU_Assist_Trophy_Render.png', 50, 85, 0)
assistTrophyTextImg = imageModifier.space_modifier('assistTrophyWithText.png', 70, 85, 0)
rotated180AssistTrophyTextImg = pygame.transform.rotate(assistTrophyTextImg, 180)
rotated90AssistTrophyTextImg = pygame.transform.rotate(assistTrophyTextImg, 90)
pokeBallImg = imageModifier.space_modifier('pokeBallWithText.png', 65, 80, 0)
rotated90PokeBallImg = pygame.transform.rotate(pokeBallImg, 90)
rotated270PokeBallImg = pygame.transform.rotate(pokeBallImg, 270)
gameWindows.createBoard(font)

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
players[0].getNewBoardPos(monopolyBoard, players[0], 0, players, drawPiles, activePlayer, 0)
players[1].getNewBoardPos(monopolyBoard, players[1], 1, players, drawPiles, activePlayer, 0)
if len(players) >= 3:
    players[0].getNewBoardPos(monopolyBoard, players[2], 2, players, drawPiles, activePlayer, 0)
    if len(players) == 4:
        players[0].getNewBoardPos(monopolyBoard, players[3], 3, players, drawPiles, activePlayer, 0)
pygame.display.update()

while gaming:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            gameWindows.createBoard(font)
            posList = []
            posList.append([860, 860, 140, 140])
            for i in range(8,-1, -1):
                posList.append([140 + i*80, 860, 80, 140])
            posList.append([0, 860, 140, 140])
            for i in range(8, -1, -1):
                posList.append([0, 140+80*i, 140, 80])
            posList.append([0, 0, 140, 140])
            for i in range(0, 9):
                posList.append([140+i*80, 0, 80, 140])
            posList.append([860, 0, 140, 140])
            for i in range(0, 9):
                posList.append([860, 140+i*80, 140, 80])
            
            for i in range(len(spaces)):
                spaces[i].setOwnerOutline(monopolyBoard, players, posList[i])

            monopolyBoard.blit(marthText, marthRect)
            monopolyBoard.blit(marthImg, (465, 895))
            monopolyBoard.blit(marthText2, marthRect2)
            monopolyBoard.blit(dkText, dkRect)
            monopolyBoard.blit(dkImg, (550, 895))
            monopolyBoard.blit(dkText2, dkRect2)
    
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
                    p4Text = font.render(players[3].playerName + "\nCash: " + str(players[3].money), True, BLACK)
                    monopolyBoard.blit(p4Text, (505, 610))
            if activePlayer.isBankrupt == False:
                roll = activePlayer.rollDice(monopolyBoard)
                players[0].getNewBoardPos(monopolyBoard, players[0], 0, players, drawPiles, activePlayer, roll)
                players[1].getNewBoardPos(monopolyBoard, players[1], 1, players, drawPiles, activePlayer, roll)
                if len(players) >= 3:
                    players[2].getNewBoardPos(monopolyBoard, players[2], 2, players, drawPiles, activePlayer, roll)
                    if len(players) == 4:
                        print("test 4")
                        players[3].getNewBoardPos(monopolyBoard, players[3], 3, players, drawPiles, activePlayer, roll)
                if activePlayer.money < 0:
                    activePlayer.isBankrupt = True
                    #calculate everyone's total net worth and decide winner
                    winner = players[0]
                    maxWorth = players[0].calcNetWorth()
                    for player in players:
                        netWorth = player.calcNetWorth()
                        if netWorth > maxWorth:
                            winner = player
                            max = netWorth
                    monopolyBoard.fill(WHITE)
                    winnerText = font.render("The winner is " + winner.playerName + "!")
                    monopolyBoard.blit(winnerText, (500, 500))
                
                
            if activePlayer.rolledDoubles == False or activePlayer.inJail == True or activePlayer.isBankrupt == True:
                playerIndex = (playerIndex + 1) % numPlayers
                activePlayer = players[playerIndex]

            pygame.display.update()

