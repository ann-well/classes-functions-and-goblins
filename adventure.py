# Text based little game to practice Python

class Character:
    """A class containing basic information about characters"""
    def __init__(self, name, race, inventory):
        self.name = name
        self.race = race
        self.inventory = inventory

    def __repr__(self):
        return Character(self.name, self.race)

    def __str__(self):
        return(str(self.name + ' The ' + self.race))

    def showYourself(self):
        print('I AM {} THE GREAT {}. Witness my power!'.format(self.name, self.race).upper())

    def showInventory(self):
        print('Currently in your inventory:')
        for item in self.inventory:
            print('* ', item)

class Protagonist(Character):
    def __init__(self, name, race, inventory, alignment=0, magic=0):
        super().__init__(name, race, inventory)
        self.alignment = alignment
        self.magic = magic

    def changeAlign(self,  alignNum):
        self.alignment = self.alignment + alignNum

    def changeMagic(self, magiceNum):
        self.magic = self.magic + magiceNum

class Npc(Character):
    def __init__(self, name, race, inventory, friend=0):
        super().__init__(name, race, inventory)
        self.friend = friend

    def changeFriend(self, friendNum):
        self.friend = self.friend + friendNum

hop = Npc('Hop', 'Goblin', ['old coin'])
hop.showYourself()

hero = Protagonist('Bob', 'Dwarf', ['amulet', 'torch'])
hop.showYourself()
hop.showInventory()

import time

print('''--You wake up in a dark cold place. You feel the rocks beneath you. You also feel strangely calm,
(as if you didn't just wake up in a dark cold place). You begin to lift your head from the ground to take a look around when suddenly...--''')
#input("Press Enter to continue...")
print('\nHello there my dear adventurer. Fancy seeing you there!')
print('--You hear a friendly voice, booming through your surroundings--')
print('''We are in quite a predicament, aren't we?''')

ans = input()
if ans == 'Who are you?':
    hero.changeAlign(-1)









