#https://codereview.stackexchange.com/questions/100852/pok%C3%A9mon-style-battle-game
#https://repl.it/@JoshuaClark2/Tv-Show-Menu
# Battle simulator (simple) Pokemon Party

import random
a=1
while a<7:
  print("What Pokemon do you chose?")
  a=int(input("Enter the number of what pokemon you want to battle with! Options are 1 - eevee. 2 - charmander. 3 - pikachu. 4 - mewtwo. 5 - bulbasaur. 6 - squirtle. 7 - All Pokemons have been selected."))
  if 1==a:
    print("1 Great choice, you have chosen the character Eevee!")
  elif 2==a:
    print("2-Great choice, you have chosen the character Charmander!")
  elif 3==a:
    print("Great choice, you have chosen the character Pikachu!")
  elif 4==a:
    print("Great choice, you have chosen the character Metwo!")
  elif 5==a:
    print("Great choice, you have chosen the character Bulbasaur!")
  elif 6==a:
    print("Great choice, you have chosen the character squirtle!")
  elif 7==a:
    print("All Pokemons have been selected! Begin your battle!")
    
moves = {"flameburst": range(5, 18),
         "tackle": range(6, 13),
         "magicburst": range(5, 18),
         "heal": range(5, 10)}


class Character:
    """ Determines our normal character we base our player and enemy off """
    def __init__(self, health):
        self.health = health

    def attack(self, other):
        raise NotImplementedError


class charmander(Character):
    """ The player, they start with 50 health and have choices of three moves """
    def __init__(self, health=50):
      super().__init__(health)

    def attack(self, other):
        while True:
            choice = str.lower(input("\nWhat power move would you like to chose? (Flameburst, Tackle, or Heal)"))

            if choice == "heal":
                self.health += int(random.choice(moves[choice]))
                print("\nYour health is now {0.health}.".format(self))
                break
            if choice == "tackle" or choice == "flameburst":
                damage = int(random.choice(moves[choice]))
                other.health -= damage
                print("\nYou attack with {0}, dealing {1} damage.".format(choice, damage))
                break
            else:
                print("Not a real move, please try again!")

class eevee(Character):
    """ The enemy, also starts with 50 health and chooses moves at random times """
    def __init__(self, health=50):
        super().__init__(health)

    def attack(self, other):
        if self.health <= 12:
           # increasing probability of heal when under 12 health
            moves_1 = ["tackle", "magicburst", "heal", "heal", "heal", "heal", "heal"]
            cpu_choice = random.choice(moves_1)
        else:
            cpu_choice = random.choice(list(moves))
        if cpu_choice == "tackle" or cpu_choice == "magicburst":
            damage = int(random.choice(moves[cpu_choice]))
            other.health -= damage
            print("\nThe CPU attacks with {0}, dealing {1} damage.".format(cpu_choice, damage))
        if cpu_choice == "heal":
            self.health += int(random.choice(moves[cpu_choice]))
            print("\nThe CPU uses heal and its health is now {0.health}.".format(self))

def battle(charmander, eevee):
    print("An enemy CPU enters...")
    while charmander.health > 0 and eevee.health > 0:
        charmander.attack(eevee)
        if eevee.health <= 0:
            break
        print("\nThe health of the CPU is now {0.health}.".format(eevee))
        eevee.attack(charmander)
        if charmander.health <= 0:
            break
        print("\nYour health is now {0.health}.".format(charmander))
    if charmander.health > 0:
        print("You defeated the CPU!")
    if eevee.health > 0:
        print("You were defeated by the CPU!")

if __name__ == '__main__':
    battle(charmander(), eevee())