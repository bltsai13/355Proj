from MovementFile import movementLocation
class Player:
    def __init__(self, playerName, turnOrder):
        self.playerName = playerName
        self.money = 1500
        self.properties = []
        self.hasGetOutOfJailFree = False
        self.inJail = False
        self.turnsInJail = 0
        self.isBankrupt = False
        self.turnOrder = turnOrder
        self.consecutiveDoubles = 0
        self.currentSpace = movementLocation().spaces[0]