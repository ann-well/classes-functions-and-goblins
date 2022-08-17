# Text based little game to practice Python

class Protagonist:
    """A class containing basic information about our hero"""
    def __init__(self, name, race, alignment=0, muscle=0, magic=0):
        self.name = name
        self.race = race
        self.alignment = alignment
        self.muscle = muscle
        self.magic = magic

    def __repr__(self):
        return Protagonist(self.name, self.race)

    def __str__(self):
        return(str(self.name + ' The ' + self.race))

    def showYourself(self):
        print('I AM {} THE GREAT {}. Witness my power!'.format(self.name, self.race).upper())

    def changeAlign(self, alignNum):
        self.alignment = self.alignment + alignNum

    def changeMuscle(self, muscleNum):
        self.muscle = self.muscle + muscleNum

    def changeMagic(self, magiceNum):
        self.magic = self.magic + magiceNum


#hero = Protagonist('Bob', 'Dwarf')
#hero.showYourself()







