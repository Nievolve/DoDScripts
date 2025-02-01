import random
import lists
import charCreation

def grundegenskaper():
    t61,t62,t63,t64 = random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)
    diceList = [t61,t62,t63,t64]
    diceList.remove(min(diceList))
    return diceList

def randomSläkte():
    choice = random.choice(lists.races)
    charCreation.label.config(choice)
    return choice

def randomYrke():
    choice = random.choice(lists.professions)
    charCreation.label.config(choice)
    return choice


if __name__ == "__main__":
    grundegenskaper()