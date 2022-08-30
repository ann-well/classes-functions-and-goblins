# Text based little game to practice Python
import random, sys, time
import pyinputplus as pyip

#global timesPlayed
global TIMES_PLAYED
TIMES_PLAYED = 0

def printTalk(charLine):
    """Outputs a line spoken by a character, with 1 second break before"""
    time.sleep(1)
    print('--', charLine, '--')

def printInner(innerLine):
    """Outputs a line of inner monologue, with 1 second break before"""
    time.sleep(1)
    print(innerLine)

class Character:
    """A class containing basic information about characters"""
    def __init__(self, name, race, hp, inventory):
        self.name = name
        self.race = race
        self.hp = hp
        self.inventory = inventory

    def __repr__(self):
        return Character(self.name, self.race, self.hp, self.inventory)

    def __str__(self):
        return(str(self.name + ' The ' + self.race))

    def showYourself(self):
        """Outputs a message containing the character's name and race"""
        print('I AM {} THE GREAT {}. Witness my power!'.format(self.name, self.race).upper())

    def showInventory(self):
        """Outputs the character's current inventory"""
        print('Currently in your inventory:')
        for item in self.inventory:
            print('* ', item)

    def change_hp(self, hpNum):
        """Changes the character's hit point, positive numbers for damage taken and negative for damage healed"""
        self.hp = self.hp - hpNum

class Protagonist(Character):
    """A subclass for the characteristic of the main protagonist, adding alignment and magic as attributes"""
    def __init__(self, name, race, hp, inventory, party, alignment=0, hand=2):
        super().__init__(name, race, hp, inventory)
        self.party = party
        self.alignment = alignment
        self.hand = hand
    def attack_dmg(self):
        """Outputs the damage caused by the protagonist, random range depending on the number of hands left and the presence of a weapon"""
        if self.hand == 2 and 'sword' in self.inventory:
            return random.randint(5, 7)
        elif self.hand == 1 and 'sword' in self.inventory:
            return random.randint(3, 4)
        elif self.hand == 2 and 'sword' not in self.inventory:
            return random.randint(2, 3)
        elif self.hand == 1 and 'sword' not in self.inventory:
            return random.randint(0, 3)

    def change_align(self,  alignNum):
        """Changes the protagonist allignment, positive numbers for increasing it and negative for decreasing"""
        self.alignment = self.alignment + alignNum

    def remove_hand(self):
        """Changes the number of hands that the protagonist has left"""
        self.hand = self.hand - 1

class Npc(Character):
    """A subclass fot the characteristics of npcs, adding friendliness towards the hero as an attribute"""
    def __init__(self, name, race, hp, inventory, friend=0):
        super().__init__(name, race, hp, inventory)
        self.friend = friend

    def change_friend(self, friendNum):
        """Changes the friendliness towrads the hero, positive numbers for increasing it and negative for decreasing"""
        self.friend = self.friend + friendNum

class Enemy(Character):
    """A subclass for enemies, adding their attack power"""
    def __init__(self, name, race, hp, inventory, power):
        super().__init__(name, race, hp, inventory)
        self.power = power

    def enemy_rage(self):
        """Changes the enemy's power levels if enraged"""
        self.power = self.power * 2

    def attack_dmg(self):
        """Outputs the enemy's damage, random range depending on the power level"""
        return int(random.randint(4,6) * self.power)



# attacker is the one attacking first
def fight(attacker, defender):
    while not attacker.hp <= 0:
        # attacker attacks
        if isinstance(attacker, Protagonist):
            input("Press Enter to attack!")
        attacker_dmg = attacker.attack_dmg()
        if isinstance(defender, Protagonist):
            print('You suffer ', attacker_dmg, ' dmg')
        else:
            print(attacker_dmg, ' DMG!')
        defender.change_hp(attacker_dmg)
        if defender.hp <= 0:
            if isinstance(defender, Protagonist):
                death()
            else:
                break
        time.sleep(1)
        # defender attacks
        if isinstance(defender, Protagonist):
            input("Press Enter to attack!")
        defender_dmg = defender.attack_dmg()
        if isinstance(attacker, Protagonist):
            print('You suffer ', defender_dmg, ' dmg')
        else:
            print(defender_dmg, ' DMG!')
        attacker.change_hp(defender_dmg)
        if attacker.hp <= 0:
            if isinstance(attacker, Protagonist):
                death()
            else:
                break
    print('You stand victorious. The bloodied remains of your opponent are spread at you feet')

def death():
    print('''You've reached the end of your adventure.''')
    time.sleep(1)
    print('You\'ve fought this fight {} times'.format(TIMES_PLAYED))
    print('''Worms are slowly starting to circle your lifeless body, like tiny wingless vultures.''')
    time.sleep(1)
    print('''Soon your flesh will become nothing more than just their food''')
    time.sleep(1)
    for i in range(5):
        print('.')
        time.sleep(0.5)
    print('''Do you want to start again?''')
    contin = pyip.inputYesNo()
    if contin == 'yes':
        startingPoint()
        return
    else:
        sys.exit()

import random
def meadow():
    printInner('The cave opens up to a pretty scenic view - a quiet little meadow surrounded by trees')
    if 'Hop' not in hero.party and 'sword' not in hero.inventory:
        printTalk('''...goodbye then''')
        printInner('''Hop ran away. You're on your own now''')
    elif 'Hop' in hero.party and 'sword' not in hero.inventory:
        printTalk('''Let's fo this, partner!''')

    def event1():
        printInner('''At the edge of the meadow, in the bushes, you see a faint movement''')
        printInner('''Before you get the chance to decide if it's worth investigating, something jumps out''')
        printInner('''It's a BADGER!''')
        if hero.alignment > 3:
            printInner('''He's so cute! *.*''')
            printInner('''You let out an audible gasp''')
        if 'Hop' in hero.party:
            printTalk('''You better watch out, they're quite ferocious!''')
        printInner('''The badger seems to just look at you with his tiny beady eyes''')
        time.sleep(1)
        print('''---What will you do?---
    A - *Make yourself smaller and approach the badger slowly, with an outstreched hand.*
    B - *Stare back at him*
    C - Hello, badger!
    D - *attack the badger before he gets the chance to strike first*''')
        ans = input()
        while True:
            if ans.upper() not in ['A', 'B', 'C', 'D']:
                print('Please choose A B C or D')
                continue
            elif ans.upper() == 'A':
                hero.change_align(5)
                printInner('''You approach the badger. It looks sweet and innocent. Maybe you can make a new friend!''')
                printInner('''but SUDDENLY''')
                printInner('''It attacks you without any warning!''')
                if 'Hop' in hero.party and hop.friend > 8:
                    printTalk('''BEGONE DEMON!!!''')
                    printInner('''Hop put himself between you and the beast!''')
                    printInner('''The badger sinks its teeth in the sword that Hop had drawn''')
                    printInner('''The sword broke... Just how strong is this thing?!''')
                    hop.inventory.remove('sword')
                    printInner('''You both scream and run into the woods while the badger EATS the metal''')
                else:
                    printInner('''The badger sinks its enormous teeth into you hand!''')
                    printInner('''One chomp and the whole hand is... gone''')
                    printInner('''Screaming, you run away into the woods''')
                    printInner('''You haven't made a new friend and you lost your old hand.''')
                    hero.remove_hand()
                    if 'Hop' in hero.party:
                        printTalk('''HE ATE YOUR HAND!!!''')
                        printInner('''Yes, and bringing it up is not helpful''')
                        printInner('''Both you and Hop scream some more and enter the woods''')
                break
            elif ans.upper() == 'B':
                hero.change_align(-3)
                printInner('''The badger bares his teeth. There's a lot of them. More than it should be...''')
                printInner('''You decide to slowly back away and enter the woods, keeping an eye on the tiny devil''')
                if 'Hop' in hero.party:
                    printInner('''Hop agrees wholeheartedly with this decision and follows you''')
                break
            elif ans.upper() == 'C':
                hero.change_align(4)
                printInner('''The badger does not say hello back. Rude''')
                printInner('''But he seems to be pleased with your politeness''')
                printInner('''The animal turns away and trots into the woods''')
                if 'Hop' in hero.party:
                    printTalk('''We dodged a bullet there!''')
                printInner('''You follow the badger into the woods, but he knows (and probably owns) the place, so you lose him immediately''')
                break
            elif ans.upper() == 'D':
                printInner('''You try to tackle the badger''')
                if 'Hop' in hero.party:
                    printTalk('NOOO!')
                    printInner('''Hop shouts, but you are unstoppable''')
                printInner('''The beast is surprisingly agile!''')
                printInner('''He slithers his way from your attempts to grapple him and bites your hand''')
                printInner('''You feel a sharp pain, look down on the badger...''')
                printInner('''He is currently running away with''')
                printInner('YOUR HAND')
                printInner('''in his teeth...''')
                printInner('''The badger ate your hand. You scream and run into the woods''')
                hero.remove_hand()
                if 'Hop' in hero.party:
                    printInner('''You hear Hop running after you. He is also screaming''')
                break
    def event2():
        printInner('''You spot some rubble in the thick grass nearby.''')
        printInner('''Upon closer inspection it seems that it was, at some point... a gravestone?''')
        printInner('You look around')
        printInner('''Now you notice it: you are surrounded by dilapidated graves''')
        if 'Hop' in hero.party:
            printInner('''Hop moved closer to one of them''')
            printTalk('Here lies... Ongar the Great {}'.format(hero.race).title())
            printTalk('''Poor soul...''')
        else:
            printInner('''You read the inscription on one of the less broken stones''')
            printInner('Here lies... Ongar the Great {}'.format(hero.race).title())
        printInner('''You vaguely recognize this name...''')
        printInner('''The only other inscription that is partially readable is''')
        printInner('''....p the Gobli..''')
        if 'Hop' in hero.party:
            printInner('''Hop looks at this one with sadness, and lowers his head in a silent prayer''')
        time.sleep(1)
        print('''---What will you do?---
    A - *ignore the graveyard and move on*
    B - *pluck some flowers and put them near the stones*
    C - *search for loot*
    D - *kick the goblin grave*''')
        ans = input()
        while True:
            if ans.upper() not in ['A', 'B', 'C', 'D']:
                print('Please choose A B C or D')
                continue
            elif ans.upper() == 'A':
                hero.change_align(-3)
                if 'Hop' in hero.party:
                    hop.change_friend(-2)
                    printInner('''Hop looks at you with disapproval''')
                printInner('''You enter the woods''')
                break
            elif ans.upper() == 'B':
                hero.change_align(3)
                printInner('You honoured the fallen and moved on into the woods')
                if 'Hop' in hero.party:
                    hop.change_friend(4)
                    printTalk('''...Thank you''')
            elif ans.upper() == 'C':
                printInner('''You decided to become a graverobber''')
                hero.change_align(-4)
                if 'Hop' in hero.party:
                    printInner('''Hop looks at you''')
                    printTalk('''Are you sure this is what you want to do?''')
                    grave = pyip.inputYesNo()
                    if grave == 'no':
                        printInner('''After some consideration... no. It's not the greatest idea''')
                        hero.change_align(1)
                    else:
                        printInner('''Yes it is''')
                        hop.change_friend(-5)
                printInner('''After some unholy searching you find''')
                printInner('''nothing. Hope it was worth it''')
                break
            elif ans.upper() == 'D':
                hero.change_align(-7)
                if 'Hop' in hero.party:
                    hop.change_friend(-10)
                    printTalk('What are you doing?!')
                    printInner('''Hop looks at you in complete and utter shock''')
                    printInner('''You kick the grave again''')
                    printTalk('''You dick.''')
                    printInner('''The goblin draws a sword and charges at you''')
                    bad_hop = Enemy(hop.name, hop.race, hop.hp, hop.inventory, 0.5)
                    bad_hop.enemy_rage()
                    initiative = random.randint(1,2)
                    if initiative == 1:
                        fight(hero, bad_hop)
                    else:
                        fight(bad_hop, hero)
#HERE I AM NOW

    def event3():
        pass

    event = random.randint(1,3)
    if event == 1:
        event2()
    elif event == 2:
        event2()
    elif event == 3:
        event2()


def caveOne():

    def addToParty():
        printInner('Will you join forces with Hop the Goblin?')
        addToParty = pyip.inputYesNo()
        if addToParty == 'yes':
            hero.party.append('Hop')
            printTalk('''Great! Let's go!''')
            printInner('''That's a very enthusiastic party member you just gained''')
        else:
            printTalk('''If that's what you want... we'll split as soon as we get out of here''')
            hop.change_friend(-5)

        printInner('''Both of you, using the goblin's torch as source of light, search for a way out''')
        if 'Hop' in hero.party:
            printTalk('''Do you remember anything?''')
            printInner('''You don't''')
            printTalk('''Me too... But we must be adventurers! Maybe we were attacked and ended up braindamaged in a cave?''')
            printInner('''That does make sense''')
            hop.change_friend(2)
            printInner('''After a moment of friendly banter you reach the exit''')
        else:
            printInner('''After a moment of awkward silence you reach the exit''')
            printTalk('''So this is where we part ways''')
            printInner('''Said the goblin and walked away without looking''')
            printInner('''Do you hear... sniffling?''')


    printInner('''A face emerges from the darkness, illuminated by a small makeshift torch. It is...''')
    time.sleep(0.5)
    if hero.race.lower() == 'goblin':
        printInner('...a familiar face! It appears to be a fellow goblin')
        hop.change_friend(5)
    else:
        printInner('''...a goblin face?!''')
        if hero.alignment <= -5:
            printInner('''You don't trust goblins. No one should.''')
            hero.change_align(-1)
        else:
            printInner('''You are quite shocked, but he does seem nice.''')

    while True:
        time.sleep(1)
        print('''---What will you do?---
    A - Hello there, how are you?
    B - Are you going to kill me?
    C - *stare at the goblin*
    D - *attack the goblin''')
        ans = input()
        if ans.upper() not in ['A', 'B', 'C', 'D']:
            print('Please choose A B C or D')
            continue
        elif ans.upper() == 'A':
            hero.change_align(2)
            hop.change_friend(5)
            printTalk('''Oh it's so nice to finally talk to you! I'm quite alright, but I was worried about you''')
            printTalk('''So I stayed right here and waited for you to wake up too!''')
            printTalk('''I woke up not long ago and almost had a heart attack, so I wanted to spare you the shock as much as I could''')
            printTalk('''I think we should look team up, we don't know what is out there''')
            addToParty()
            break
        elif ans.upper() == 'B':
            hop.change_friend(-3)
            if hero.race.lower() != 'goblin':
                printTalk('''Why would I... is it because I am a goblin?''')
            else:
                printTalk('''Why would I attack my brethren?''')
            printTalk('''No no no, I waited for you to get up so we can leave this place!''')
            if hop.friend < 0:
                printTalk('''...But now I think we maybe should split up as soon as we get out''')
                printInner('''The goblin looks sad''')
            else:
                printTalk('Shall we go outside together?')
                addToParty()
            break
        elif ans.upper() == 'C':
            printTalk('''Are you okay?''')
            hop.change_friend(-2)
            hero.change_align(-1)
            printTalk('''I'm not gonna hurt you!''')
            printTalk('''I waited for you to get up so we can leave this place!''')
            if hop.friend < 0:
                printTalk('''...But now I think we maybe should split up as soon as we get out''')
                printInner('''The goblin looks sad''')
            else:
                printTalk('Shall we go outside together?')
                addToParty()
            break
        elif ans.upper() == 'D':
            printInner('''You strike fast, so that this treacherous being wouldn't have a chance to do anything''')
            attackHop()
            break
    meadow()

def attackHop():
    bad_hop = Enemy(hop.name, hop.race, hop.hp, hop.inventory, 0.5)
    fight(hero, bad_hop)
    printInner('A discarded torch is dying slowly, but in its last feint flickers you manage to find a SWORD next to the body')
    printInner('''They... didn't use it against you, although it was within their reach...''')
    printInner('''You pick up the sword''')
    hero.inventory.append('sword')
    printInner('''There's something shiny sticking out of the rugged garments.''')
    printInner('''Upon closer examination it appears to be a OLD COIN''')
    printInner('It is a bit bloodied, but looks VERY expensive')
    printInner('''Will you take it?''')
    coin = pyip.inputYesNo()
    if coin == 'yes':
        printInner('You took the coin')
        hero.inventory.append('old coin')
        hero.change_align(-5)
    else:
        printInner('You decide to leave the coin with its previous unfortunate owner')
        hero.change_align(2)
    printInner('You start looking for the exit')
    meadow()

# THE BEGINNING
print('Please enter your name:')
heroName = input()

def startingPoint():
    global hop
    hop = Npc('Hop', 'Goblin', 9, ['old coin', 'sword'], friend=5)

    print('What race would you like to become?:')
    heroRace = input()
    global hero
    hero = Protagonist(heroName, heroRace, 9, [], [])

    global TIMES_PLAYED
    TIMES_PLAYED = TIMES_PLAYED + 1

    printInner('''You wake up in a dark cold place. You feel the rocks beneath you. You also feel strangely calm,
(as if you didn't just wake up in a dark cold place). You begin to lift your head from the ground to take a look around when suddenly...''')
    printTalk('Hello there my dear adventurer. Fancy seeing you there!')
    printInner('You hear a friendly voice, booming through your surroundings')
    printTalk('''We are in quite a predicament, aren't we?''')
    time.sleep(1)
    while True:
        print('''---What do you do?---
        A - *look around*
        B - *go back to sleep*
        C - Who are you?
        D - Where am I?''')
        ans = input()
        if hero.alignment == -5:
            printTalk('Are you... ignoring me?')
            hop.change_friend(-3)
            printInner('''You reluctantly get up. Darkness still surrounds you, but you decided you don't need friends
    on this journey, apparently''')
            time.sleep(1)
            break
        elif ans.upper() == 'A':
            printInner('You look around. It is dark and you see nothing')
            hero.change_align(-1)
            continue
        elif ans.upper() == 'B':
            printInner('''...Seriously?
Well you're lying on what seems to be rocks, so you try your best but the sleep doesn't come''')
            hero.change_align(-1)
            continue
        elif ans.upper() == 'C':
            printTalk('''My name is Hop, and if you turn around you can see me!''')
            break
        elif ans.upper() == 'D':
            printTalk('''In a cave!''')
            printInner('exclaimed the friendly voice eagerly')
            printInner('''You'll have to see for yourself who is talking to you''')
            break

        elif 'attack' in ans.lower() or 'kill' in ans.lower():
            printInner('''Attack is the best defense. You jump towards the source of the voice, ready to strike''')
            hero.change_align(-10)
            hop.change_friend(-7)
            attackHop()
            return
        elif ans.upper() not in ('A', 'B', 'C', 'D'):
            printInner('You little rebel. Please enter A B C or D')
            continue

    time.sleep(0.5)
    printInner('You turn around to see the owner of the voice')
    caveOne()

startingPoint()









