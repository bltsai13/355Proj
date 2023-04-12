from SpaceClass import Space
from random import randint
class movementLocation:

    def __init__(self, inJail=False, turnsInJail=0, isDouble=False, consecutiveDoubles=0, spaces=[Space("Go", "PokeBall1", "Little Mac", "Low Tier Tax", "Marth", "King Dedede", "AssistTrophy1", "Kirby", "Meta Knight", "Jail", "Jigglypuff", "Pac Man", "", "", "", 0, 0, 0, 0, 0, 0, 0, 0), Space("Ganondorf", "Little Mac", "Low Tier Tax", "Marth", "King Dedede", "AssistTrophy1", "Kirby", "Meta Knight", "Jail", "Jigglypuff", "Pac Man", "Mewtwo", "", "", "", 2, 10, 30, 90, 160, 250, 60, 50), Space("PokeBall1", "Low Tier Tax", "Marth", "King Dedede", "AssistTrophy1", "Kirby", "Meta Knight", "Jail", "Jigglypuff", "Pac Man", "Mewtwo", "Incineroar", "", "", "", 0, 0, 0, 0, 0, 0, 0, 0), Space("Little Mac", "Marth", "King Dedede", "AssistTrophy1", "Kirby", "Meta Knight", "Jail", "Jigglypuff", "Pac Man", "Mewtwo", "Incineroar", "Ike", "", "", "", 4, 20, 60, 180, 320, 450, 60, 50), Space("Low Tier Tax", "King Dedede", "AssistTrophy1", "Kirby", "Meta Knight", "Jail", "Jigglypuff", "Pac Man", "Mewtwo", "Incineroar", "Ike", "Young Link", "", "", "", 200, 0, 0, 0, 0, 0, 0, 0), Space("Marth", "AssistTrophy1", "Kirby", "Meta Knight", "Jail", "Jigglypuff", "Pac Man", "Mewtwo", "Incineroar", "Ike", "Young Link", "PokeBall2", "", "", "", 25, 25, 50, 100, 200, 200, 200, 0), Space("King Dedede", "Kirby", "Meta Knight", "Jail", "Jigglypuff", "Pac Man", "Mewtwo", "Incineroar", "Ike", "Young Link", "PokeBall2", "Toon Link", "", "", "", 6, 30, 90, 270, 440, 550, 100, 50), Space("AssistTrophy1", "Meta Knight", "Jail", "Jigglypuff", "Pac Man", "Mewtwo", "Incineroar", "Ike", "Young Link", "PokeBall2", "Toon Link", "Link", "Low Tier Tax", "Pac Man", "Marth", 0, 0, 0,0, 0, 0, 0, 0), Space("Kirby", "Jail", "Jigglypuff", "Pac Man", "Mewtwo", "Incineroar", "Ike", "Young Link", "PokeBall2", "Toon Link", "Link", "Free Parking", "", "", "", 6, 30, 90, 270, 400, 550, 100, 50), Space("Meta Knight", "Jigglypuff", "Pac Man", "Mewtwo", "Incineroar", "Ike", "Young Link", "PokeBall2", "Toon Link", "Link", "Free Parking", "Falco", "", "", "", 8, 40, 100, 300, 450, 600, 120, 50), Space("Jail", "Pac Man", "Mewtwo", "Incineroar", "Ike", "Young Link", "PokeBall2", "Toon Link", "Link", "Free Parking", "Falco", "AssistTrophy2", "", "", "", 0, 0, 0, 0,0 ,0 ,0, 0), Space("Jigglypuff", "Mewtwo", "Incineroar", "Ike", "Young Link", "PokeBall2", "Toon Link", "Link", "Free Parking", "Falco", "AssistTrophy2", "Wolf", "", "", "", 10, 50, 150, 450, 625, 750, 140, 100), Space("Pac Man", "Incineroar", "Ike", "Young Link", "PokeBall2", "Toon Link", "Link", "Free Parking", "Falco", "AssistTrophy2", "Wolf", "Fox", "", "", "", 4, 4, 4, 4, 4, 4, 150, 0), Space("Mewtwo", "Ike", "Young Link", "PokeBall2", "Toon Link", "Link", "Free Parking", "Falco", "AssistTrophy2", "Wolf", "Fox", "Roy", "", "", "", 10, 50, 150, 450, 625, 750, 140, 100), Space("Incineroar", "Young Link", "PokeBall2", "Toon Link", "Link", "Free Parking", "Falco", "AssistTrophy2", "Wolf", "Fox", "Roy", "Samus", "", "", "", 12, 60, 180, 500, 700, 900, 160, 100), Space("Ike", "PokeBall2", "Toon Link", "Link", "Free Parking", "Falco", "AssistTrophy2", "Wolf", "Fox", "Roy", "Samus", "Dark Samus", "", "", "", 25, 25, 50, 100, 200, 200, 200, 0), Space("Young Link", "Toon Link", "Link", "Free Parking", "Falco", "AssistTrophy2", "Wolf", "Fox", "Roy", "Samus", "Dark Samus", "Mr Game & Watch", "", "", "", 14, 70, 200, 550, 750, 950, 180, 100), Space("PokeBall2", "Link", "Free Parking", "Falco", "AssistTrophy2", "Wolf", "Fox", "Roy", "Samus", "Dark Samus", "Mr Game & Watch", "Zero Suit Samus", "", "", "", 0, 0, 0, 0, 0, 0, 0, 0), Space("Toon Link", "Free Parking", "Falco", "AssistTrophy2", "Wolf", "Fox", "Roy", "Samus", "Dark Samus", "Mr Game & Watch", "Zero Suit Samus", "Go To Jail", "", "", "", 14, 70, 200, 550, 750, 950, 180, 100), Space("Link", "Falco", "AssistTrophy2", "Wolf", "Fox", "Roy", "Samus", "Dark Samus", "Mr Game & Watch", "Zero Suit Samus", "Go To Jail", "Ryu", "", "", "", 16, 80, 220, 600, 800, 1000, 200, 100), Space("Free Parking", "AssistTrophy2", "Wolf", "Fox", "Roy", "Samus", "Dark Samus", "Mr Game & Watch", "Zero Suit Samus", "Go To Jail", "Ryu", "Terry", "", "", "", 0, 0, 0, 0, 0, 0, 0, 0), Space("Falco", "Wolf", "Fox", "Roy", "Samus", "Dark Samus", "Mr Game & Watch", "Zero Suit Samus", "Go To Jail", "Ryu", "Terry", "PokeBall3", "", "", "", 18, 90, 250, 700, 875, 1050, 220, 150), Space("AssistTrophy2", "Fox", "Roy", "Samus", "Dark Samus", "Mr Game & Watch", "Zero Suit Samus", "Go To Jail", "Ryu", "Terry", "PokeBall3", "Kazuya", "Link", "Mr Game & Watch", "Roy", 0, 0, 0, 0, 0, 0, 0, 0), Space("Wolf", "Roy", "Samus", "Dark Samus", "Mr Game & Watch", "Zero Suit Samus", "Go To Jail", "Ryu", "Terry", "PokeBall3", "Kazuya", "Byleth", "", "", "", 18, 90, 250, 700, 875, 1050, 220, 150), Space("Fox", "Samus", "Dark Samus", "Mr Game & Watch", "Zero Suit Samus", "Go To Jail", "Ryu", "Terry", "PokeBall3", "Kazuya", "Byleth", "AssistTrophy3", "", "", "", 20, 100, 300, 750, 925, 1100, 240, 150), Space("Roy", "Dark Samus", "Mr Game & Watch", "Zero Suit Samus", "Go To Jail", "Ryu", "Terry", "PokeBall3", "Kazuya", "Byleth", "AssistTrophy3", "Pyra", "", "", "", 25,25, 50, 100, 200, 200, 200, 0), Space("Samus", "Mr Game & Watch", "Zero Suit Samus", "Go To Jail", "Ryu", "Terry", "PokeBall3", "Kazuya", "Byleth", "AssistTrophy3", "Pyra", "DLC Tax", "", "", "", 22, 110, 330, 800, 975, 1150, 260, 150), Space("Dark Samus", "Zero Suit Samus", "Go To Jail", "Ryu", "Terry", "PokeBall3", "Kazuya", "Byleth", "AssistTrophy3", "Pyra", "DLC Tax", "Mythra", "", "", "", 22, 110, 330, 800, 975, 1150, 260, 150), Space("Mr Game & Watch", "Go To Jail", "Ryu", "Terry", "PokeBall3", "Kazuya", "Byleth", "AssistTrophy3", "Pyra", "DLC Tax", "Mythra", "Go", "", "", "", 4, 4, 4, 4, 4, 4, 150, 0), Space("Zero Suit Samus", "Ryu", "Terry", "PokeBall3", "Kazuya", "Byleth", "AssistTrophy3", "Pyra", "DLC Tax", "Mythra", "Go", "Ganondorf", "", "", "", 24, 120, 360, 850, 1025, 1200, 280, 150), Space("Go To Jail", "Terry", "PokeBall3", "Kazuya", "Byleth", "AssistTrophy3", "Pyra", "DLC Tax", "Mythra", "Go", "Ganondorf", "PokeBall1", "", "", "", 0, 0, 0, 0,0 ,0, 0, 0), Space("Ryu", "PokeBall3", "Kazuya", "Byleth", "AssistTrophy3", "Pyra", "DLC Tax", "Mythra", "Go", "Ganondorf", "PokeBall1", "Little Mac", "", "", "", 26, 130, 390, 900, 1100, 1275, 300, 200), Space("Terry", "Kazuya", "Byleth", "AssistTrophy3", "Pyra", "DLC Tax", "Mythra", "Go", "Ganondorf", "PokeBall1", "Little Mac", "Low Tier Tax", "", "", "", 26, 130, 390, 900, 1100, 1275, 300, 200), Space("PokeBall3", "Byleth", "AssistTrophy3", "Pyra", "DLC Tax", "Mythra", "Go", "Ganondorf", "PokeBall1", "Little Mac", "Low Tier Tax", "Marth", "", "", "", 0, 0, 0, 0,0 ,0, 0, 0), Space("Kazuya", "AssistTrophy3", "Pyra", "DLC Tax", "Mythra", "Go", "Ganondorf", "PokeBall1", "Little Mac", "Low Tier Tax", "Marth", "King Dedede", "", "", "", 28, 150, 450, 1000, 1200, 1400, 300, 200), Space("Byleth", "Pyra", "DLC Tax", "Mythra", "Go", "Ganondorf", "PokeBall1", "Little Mac", "Low Tier Tax", "Marth", "King Dedede", "AssistTrophy1", "", "", "", 25, 25, 50, 100, 200, 200, 200, 0), Space("AssistTrophy3", "DLC Tax", "Mythra", "Go", "Ganondorf", "PokeBall1", "Little Mac", "Low Tier Tax", "Marth", "King Dedede", "AssistTrophy1", "Kirby", "PokeBall3", "Pac Man","Marth", 0, 0, 0,0 ,0 ,0, 0, 0), Space("Pyra", "Mythra", "Go", "Ganondorf", "PokeBall1", "Little Mac", "Low Tier Tax", "Marth", "King Dedede", "AssistTrophy1", "Kirby", "Meta Knight", "", "", "", 35, 175, 500, 1100, 1300, 1500, 350, 200), Space("DLC Tax", "Go", "Ganondorf", "PokeBall1", "Little Mac", "Low Tier Tax", "Marth", "King Dedede", "AssistTrophy1", "Kirby", "Meta Knight", "Jail", "", "", "", 100, 0, 0, 0,0 ,0, 0, 0), Space("Mythra", "Ganondorf", "PokeBall1", "Little Mac", "Low Tier Tax", "Marth", "King Dedede", "AssistTrophy1", "Kirby", "Meta Knight", "Jail", "Jigglypuff", "", "", "", 50, 200, 600, 1400, 1700, 2000, 400, 200)], currentSpace=Space("Go", "PokeBall1", "Little Mac", "Low Tier Tax", "Marth", "King Dedede", "AssistTrophy1", "Kirby", "Meta Knight", "Jail", "Jigglypuff", "Pac Man", "", "", "", 0, 0, 0, 0, 0, 0, 0, 0)):
        self.inJail = inJail
        self.turnsInJail = turnsInJail
        self.isDouble = isDouble
        self.consecutiveDoubles = consecutiveDoubles
        self.spaces = spaces
        self.currentSpace = currentSpace

    def findSpace(self, spaceName):
        for space in self.spaces:
            if spaceName == space.spaceName:
                print("First: " + space.spaceName)
                return space
    
    def newLocation(self, roll):
        if self.consecutiveDoubles == 3 or roll == 0:
            return "Jail"
        match roll:
            case 2:
                print(self.currentSpace.move2)
                return self.currentSpace.move2
            case 3:
                print(self.currentSpace.move3)
                return self.currentSpace.move3
            case 4:
                print(self.currentSpace.move4)
                return self.currentSpace.move4
            case 5:
                print(self.currentSpace.move5)
                return self.currentSpace.move5
            case 6:
                print(self.currentSpace.move6)
                return self.currentSpace.move6
            case 7:
                print(self.currentSpace.move7)
                return self.currentSpace.move7
            case 8:
                print(self.currentSpace.move8)
                return self.currentSpace.move8
            case 9:
                print(self.currentSpace.move9)
                return self.currentSpace.move9
            case 10:
                print(self.currentSpace.move10)
                return self.currentSpace.move10
            case 11:
                print(self.currentSpace.move11)
                return self.currentSpace.move11
            case 12:
                print(self.currentSpace.move12)
                return self.currentSpace.move12
            
    def rollDice(self):
        dice1Roll = randint(1,6)
        dice2Roll = randint(1,6)
        if dice1Roll == dice2Roll:
            self.isDouble = True
            self.consecutiveDoubles += 1
            self.inJail = False
            self.turnsInJail = 0
        else:
            self.isDouble = False
            self.consecutiveDoubles = 0
        totalRoll = dice1Roll + dice2Roll
        if self.inJail:
            self.turnsInJail += 1
            if self.turnsInJail >= 3:
                self.turnsInJail = 0
                self.inJail = False
            else:
                totalRoll = 0
                print("You're still in jail!")
        print("Current dice roll is: " + str(dice1Roll) + ", " + str(dice2Roll))

        self.currentSpace = self.findSpace(self.newLocation(totalRoll))
        if self.currentSpace.spaceName == 'Go To Jail':
            self.currentSpace = self.findSpace('Jail')
            self.inJail = True
            self.turnsInJail = 0
        print("Current space is: " + self.currentSpace.spaceName)

    

            

