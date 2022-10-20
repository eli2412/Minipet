import random
class MiniPet:
    reduced_happiness = 3
    happiness_max = 10
    sad_warning = 3
    food_reduction = 3
    full_belly = 10
    starving_warning = 3
    talk = ["'WRUFF!!'"] 

    def __init__(self, name, type_animal):
        self.name = name
        self.type_animal = type_animal
        self.food = random.randrange(self.full_belly)
        self.happy = random.randrange(self.happiness_max)
        self.talk = self.talk[:]

    def __timer(self):
        self.food -= 1
        self.happy -= 1

    @property
    def mood(self):
        if self.food > self.starving_warning and self.happy > self.sad_warning:
            return "HAPPY DAPPY!!! "
        elif self.food < self.starving_warning:
            return "HUNGRY!! ;_;"
        else:
            return "BORED :("

    def __repr__(self):
        return f"I'm {self.name}, I feel {self.mood}.\n"

    def learn(self, new_word):
        self.talk.append(new_word)
        print(f"{new_word}..., {new_word}..., {new_word}!!!\n")
        self.__timer()

    def bio(self):
        print(f"I am a {self.type_animal}, named {self.name}. I feel {self.mood}\n")
        self.__timer()

    def feed(self):
        print("Munch, munch, munch... :3\n")
        meal = random.randrange(self.food, self.full_belly)
        self.food += meal
        if self.food < 0:
            self.food = 0
            print("I'm so hungry :(\n")
        elif self.food > self.full_belly:
            self.food = self.full_belly
            print("I'm STUFFED, NO MORE FOOD!\n")
        self.__timer()

    def play(self):
        print("PLAAAAAAAAAAY\n")
        play_time = random.randrange(self.happy, self.happiness_max)
        self.happy += play_time
        if self.happy < 0:
            self.happy = 0
            print("I am BOOOOOOOOREED\n")
        elif self.happy > self.happiness_max:
            self.happy = self.happiness_max
            print("YAAY, SO FUN, I'm getting tired though...\n")
        self.__timer()

def user():
    user_name = input("What is your name? ")
    pet_name = input("What would you like to name your pet? ")
    pet_type = input("What would kind of pet would you like? ")

    my_pet = MiniPet(pet_name, pet_type)

    input(f"Hello!! I'm {my_pet.name}, the {my_pet.type_animal}!. Press enter to start!")

    while True:
        choice = int(input("What would you like to do? \n 1 - Feed your pet \n 2 - Talk with your pet \n 3 - Teach your pet a new word \n 4 - Play with your pet \n 0 - Quit "))
        if choice == 0:
            print(f"Goodbye {user_name}! Till next time.'Dies because of lack of attention'")
            break
        elif choice == 1:
            my_pet.feed()
        elif choice == 2:
            my_pet.bio()
        elif choice == 3:
            new_word = input("what word would you like to teach your pet? ")
            my_pet.learn(new_word)
        elif choice == 4:
            my_pet.play()
        else:
            return "Sorry, I don't know what that is :/"

user()
