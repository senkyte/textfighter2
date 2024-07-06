import time
import random

class Move:
    def __init__(self, movetype, name, damage, chant=None, delay=None,chant2="",energy_gain=5,cost=20):
        self.name = name
        self.damage = damage
        self.chant = chant
        self.movetype = movetype
        self.delay = delay
        self.chant2 = chant2
        self.original_damage = damage
        self.cost = cost
        self.energy_gain = energy_gain
    def randomize_damage(self):
        if self.name == 'Randomised Blast':
            self.damage = random.randint(1000, 24000)
        else:
            self.damage = self.original_damage
    def use(self,player,enemy):
        if self.name == 'Randomised Blast':
            self.randomize_damage()
        if random.randint(1,8) == 8:
            crit = True
            print("The move crit!\n")
        else:
            crit = False
        if 'Attack' in self.movetype:
            if crit == True:
                enemy.health -= (self.damage - enemy.debuff_value + player.buff_value) * (100 - enemy.protection)/100 * 1.5
            else:
                enemy.health -= (self.damage - enemy.debuff_value + player.buff_value) * (100 - enemy.protection)/100
            print("{} used {}!".format(player.name,self.name))
            time.sleep(1)
            if self.chant is not None:
                print()
                print(self.chant)
                print()
            time.sleep(1)
            print("\n{} took {} damage!".format(enemy.name,(self.damage + enemy.debuff_value)))
        if 'Debuff' in self.movetype:
            print("{} used {}!".format(player.name,self.name))
            time.sleep(1)
            enemy.debuff_value += self.damage
            if self.chant is not None:
                print()
                print(self.chant)
                print()
            time.sleep(1)
            print("\n{} had their damage reduced by {}!".format(enemy.name,self.damage))
            time.sleep(1)
        if 'Buff' in self.movetype:
            print("{} used {}!".format(player.name,self.name))
            time.sleep(1)
            if self.chant is not None:
                print()
                print(self.chant)
                print()
            player.buff_value += self.damage
            print("\n{} had their damage increased by {}!".format(player.name,self.damage))
        if 'Heal' in self.movetype:
            print("{} used {}!".format(player.name,self.name))
            time.sleep(1)
            if self.chant is not None:
                print()
                print(self.chant)
                print()
            player.health += self.damage
            print("\n{} regenerated {} health!".format(player.name,self.damage))
        if 'Ultimate' in self.movetype:
            if player.energy >= self.cost:
                print("{} used {}!".format(player.name,self.name))
                time.sleep(1)
                if self.chant is not None:
                    print()
                    print(self.chant)
                    print()
                player.energy -= self.cost
                print("\n{} energy has been consumed!".format(self.cost))
                if crit == True:
                    enemy.health -= (self.damage - enemy.debuff_value + player.buff_value) * (100 - enemy.protection)/100 * 1.5
                else:
                    enemy.health -= (self.damage - enemy.debuff_value + player.buff_value) * (100 - enemy.protection)/100
                print("\n{} dealt {} damage to {}!".format(player.name,self.damage,enemy.name))
            else:
                print("You do not have enough energy!")
        if 'Ultimate' not in self.movetype:
            player.energy += self.energy_gain
        if 'Defence' in self.movetype:
            if player.protection == 0:
                print("{} used {}!".format(player.name,self.name))
                time.sleep(1)
                if self.chant is not None:
                    print()
                    print(self.chant)
                    print()
                player.protection += self.damage
                print("\n{} increased their defence by {}%!".format(player.name,self.damage))
            elif player.protection >= 50:
                print("\n{}'s defence cannot go any further!".format(player.name))
            else:
                player.protection += (self.damage/100) * player.protection
                print("{} used {}!".format(player.name,self.name))
                time.sleep(1)
                if self.chant is not None:
                    print()
                    print(self.chant)
                    print()
                player.protection += self.damage
                print("\n{} increased their defence by {}%!".format(player.name,self.damage))
            
        if 'Charge' in self.movetype:
            player.energy += self.damage
            print("\n{} has their energy charged by {}!".format(player.name,self.damage))
            
                
                
                
            
        
class Fighter:
    def __init__(self, name, health, move1, move2, move3, move4, debuff_value=0, delay=0, win="", loss="",entry="",buff_value=0,energy=0,protection=0) -> None:
        self.name = name
        self.health = health
        self.maxhealth = health
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.move4 = move4
        self.debuff_value = debuff_value
        self.buff_value = buff_value
        self.delay = delay
        self.win = win
        self.loss = loss
        self.entry = entry
        self.energy = energy
        self.protection = protection
        
   
        


 
     # Ensure health doesn't exceed max health
def reset(player)-> None:
    player.health = player.maxhealth
    player.debuff_value = 0
    player.buff_value = 0
    player.energy = 0
    player.protection = 0

def Battle(player, enemy):
    print(player.entry)
    print()
    print(enemy.entry)
    print()
    # Our turn
    while True:
        print("{}'s health: {}".format(enemy.name,enemy.health))
        print("{}'s health: {}".format(player.name,player.health))
        print("{}'s energy: {}".format(player.name,player.energy))
        print()
        playermoves = [player.move1,player.move2,player.move3,player.move4]
        for i in range(4):      
            if playermoves[i].movetype != "Ultimate":
                print("{}.{} {}(+{} Energy)".format(i+1,playermoves[i].name,playermoves[i].movetype,playermoves[i].energy_gain))
            else:
                print("{}.{} {} ({} Energy)".format(i+1,playermoves[i].name,playermoves[i].movetype,playermoves[i].cost))

        print()
        playerChoice = input("What will {} do?".format(player.name))
        if playerChoice.isdigit() == True:
            playerChoice = int(playerChoice) - 1
            print()
            playermoves[playerChoice].use(player,enemy)
        else:
            print("Invalid move, skip one turn LOL")
        if player.health <= 0:
            winner = enemy
            loser = player
            break
        if enemy.health <= 0:
            winner = player
            loser = enemy
            break
        print()
        enemymoves = [enemy.move1,enemy.move2,enemy.move3,enemy.move4]
        enemyChoice = random.randint(0,3)
        print()
        enemymoves[enemyChoice].use(enemy,player)

        if player.health <= 0:
            winner = enemy
            loser = player
            break
        if enemy.health <= 0:
            winner = player
            loser = enemy
            break
    print()
    print("{} wins!".format(winner.name))
    print()
    print(winner.win)
    print()
    print(loser.loss)
    print()
    reset(player)
    reset(enemy)


# Tester fighter. Change accordingly.
UMU = Fighter(
    name="UMU",
    health=1000000,
    move1=Move(movetype="Ultimate",name="Ult Test 1",damage=23000000,chant="Maximum Power Achieved. Rider Blast.",chant2="Charging power."),
    move2=Move(movetype="Attack",name="Randomised Blast",damage=random.randint(1000,24000),chant="import this you filthy causal"),
    move3=Move(movetype="Attack",name="Mind Crush",damage=50,chant="MIND CRUSH"),
    move4=Move(movetype="Heal",name="Cracked Regeneration",damage=5000,chant="I cracked the Regeneration code. I am now immortal."),
    debuff_value = 0,
    delay = 0,
    win="Test complete.",
    loss="Test complete (LOSS)",
    entry="Test Begin.",
    )

joe = Fighter(
    name="Sleepy Joe",
    health = 60,
    move1=Move(movetype='Attack',name="Debate Destruction",damage=5,chant="America is a country that can be definied in one word: awdefughasha"),
    move2=Move(movetype="Heal",name="Sleep",damage=10,chant="zzz...zzzz..."),
    move3=Move(movetype="Ultimate",name="Zone of Clarity: Biden Blast(Ultimate)",damage=40,chant="I will not falter! I own the finish line! BIDEN BLAST!",chant2="Sleepy Joe is awakening!"),
    move4=Move(movetype='Buff',name="Strength in Numbers",damage=2,chant="America... lend me your power!"),
    debuff_value = 2,
    delay = 1,
    win="Sleepy Joe: zzzz... oh! Did I win already?",
    loss="Sleepy Joe: America has fallen... Billions will perish...",
    entry="Sleepy Joe has enter the arena.",
    )
trump = Fighter(
    name="Donald Trump",
    health=50,
    move1=Move(movetype='Buff',name="Mcdonands Mcfeast",damage=1,chant="om nom nom... om nom"),
    move2=Move(movetype='Attack',name="Bleach Blast",damage=10,chant="This will cure your Covid!"),
    move3=Move(movetype="Ultimate",name="FAT Stomp",damage=30,chant="Alright...you've got me really mad!",chant2="om nomnomnom... hey! Stop! Let me eat!"),
    move4=Move(movetype='Heal',name="Cola Chug",damage=2,chant="Ahh... that hits the spot."),
    delay=0,
    win="Donald Trump:Thats right Sleepy Joe. I'll always be the strongest.",
    loss="Donald Trump:This fight was rigged! I want a rematch!",
    entry="Donald Trump: They say you're strong? That's fake news.",
    )
obama = Fighter(
    name="Barack Obama",
    health=70,
    move1=Move(movetype='Ultimate',name="Afghaistan Drone Strike",damage=50,chant="You'll be seeing Bin Laden soon... DRONE STRIKE!",chant2="Preparing the US Army..."),
    move2=Move(movetype="Attack",name="The Slap",damage=5,chant="You put my wifes name... out your goddamn mouth!"),
    move3=Move(movetype='Attack',name="Right Straight",damage=10,chant="Lemme show you why they call me 'Iron Obama'! "),
    move4=Move(movetype='Heal',name='Obamacare',damage=5,chant="Lemme patch myself up, real quick."),
    win="Obama: Oh yeah! I'm the strongest!",
    loss="Obama: Impossible... I'm supposed to be the strongest!",
    entry="Obama:Allow me to demostrate why I'm the president.",    
    delay=0,
    )
declanbasic = Fighter(
    name="Declan(Basic)",
    health=100,
    move1=Move(movetype="Attack",name="Basic Punch",damage=5),
    move2=Move(movetype="Heal",name="PT Delay",damage=1),
    move3=Move(movetype="Attack",name="Maimai Slap",damage=10),
    move4=Move(movetype="Ultimate",name="FULL COMBO",damage=40,chant="bing bang bang i hit maimai machine"),
    win="Declan: You were too weak... all skill!",
    loss="Declan: tryhard.",
    entry="Declan:Lets hurry this up, the Maimai cabinet is open.",
    delay=0,
)
sec1 = Fighter(
    name="Secondary 1 SST Student",
    health=50,
    move1=Move(movetype='Attack', name="Brainrot",damage=5,chant="YOU ARE NOT SKIBIDI SIGMA OHIO GYATT KAI CENAT BABY GRONK LEVEL 100 GYATT"),
    move2=Move(movetype="Debuff",name="The Consuming Rot",damage=1,chant='The rot consumes'),
    move3=Move(movetype="Attack",name='Sin of Ignorance',damage=10),
    move4=Move(movetype="Heal",name="Watch Skibidi Toilet",damage=2,chant="BRRR SKIBIDI DOP DOP DOP YES YES"),
    win="Sec 1: BRRR SKIBIDI SKIBIDI",
    loss="The Sec 1 has been evaporated.",
    delay=0,
    entry="A Sec 1 has appeared!"
    )
sec2 = Fighter(
    name="Secondary 2 SST Student (Elite)",
    health=200,
    move1=Move(movetype='Ultimate',name="Unlimited Slacker Works",damage=40,chant2="yeah ill do work...",chant="I am the bane of my teammate's existence, ethereal is my body and laziness is my blood, I have thrown over a thousand courseworks. Unaware of A1s, nor known to women. So as I pray, Unlimited Slacker Works."),
    move2=Move(movetype="Attack",name="Cutting Edge(lords)",damage=10,chant=":skull"),
    move3=Move(movetype='Debuff',name="Curse of Arrogance",damage=2),
    move4=Move(movetype='Attack',name="Basic Punch",damage=5),
    delay=0,
    win="Sec 2: I win!",
    loss="Sec 2: Impossible!",
    entry="A Sec 2 has appeared!"
    )

kaydenbasic = Fighter(
    name='Kayden(Basic)',
    health=150,
    move1=Move(movetype='Buff',name='vague_reference',damage=10,chant='hey guys... (vague reference)'),
    move2=Move(movetype=['Heal','Charge'],name='Sleep',damage=20,chant="kr mimimimimi"),
    move3=Move(movetype='Ultimate',name='Unlimited Rulebook',damage=70,chant="アンリミテッドルールブック, a rule book filled with mostly exceptions."),
    move4=Move(movetype="Debuff",name="Complain",damage=10,chant="YAP YAP YAP YAP YAP"),
    delay=0,
    entry="Kayden: hello",
    win="Kayden: f*ck you",
    loss='Kayden: owie'
    )

# Battle function, select your fighters
Battle(kaydenbasic,sec2)
