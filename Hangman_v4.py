import random
import time
import sys

Animals = ["albatross", "alligator", "ant", "anteater", "armadillo", "baboon", "bat", "bear", "beaver", "bird", "boar", "buffalo", "bull", "camel", "cat", "chameleon", "cheetah", "chicken", "chimpanzee", "chipmunk", "cow", "crab", "crocodile", "deer", "dog", "dolphin", "donkey", "duck", "eagle", "elephant", "fish", "flamingo", "fox", "frog", "giraffe", "goat", "goose", "gorilla", "greyhound", "hamster", "hare", "hedgehog", "hippo", "horse", "hyena", "insect", "jaguar", "jellyfish", "kangaroo", "kiwi", "koala", "leopard", "lion", "lizard", "llama", "lynx", "mole", "monkey", "moose", "mouse", "octopus", "ostrich", "otter", "owl", "panther", "parrot", "pelican", "pig", "puma", "rabbit", "raccoon", "rat", "reindeer", "rhino", "seal", "shark", "sheep", "skunk", "snail", "snake", "squirrel", "swan", "tiger", "turkey", "turtle", "walrus", "whale", "wolf", "wombat", "zebra"]

def slowprint(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)
    print("")

time.sleep(.2)
slowprint("WELCOME TO HANGMAN!")

while True:
    time.sleep(.5)
    print("Choose a category:")
    time.sleep(.5)
    print("The only option is Animals. (Because of the singlefile thing.)")

    while True:
        category = input().lower()
        if category == "animals":
            File = Animals
            break
        else:
            time.sleep(.5)
            print("Sadly that isn't a category. The only option is Animals.")

    List = File
    OldWord = random.choice(List)
    TheWord = OldWord
    Lives = 10
    PositionsList = []
    ExtraPositionPoints = 0
    Again = 0
    Quit = 0
    Letters_Left_Default = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    Letters_Left = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    Underscores = len(TheWord)*"_"
    indexes = []
    indexes_left = []
    for z in range(len(OldWord)):
        indexes_left.append(z + 1)

    time.sleep(.5)
    print("The word:")
    print("")
    time.sleep(.5)
    for Character in Underscores:
        print("", Character, end="")
    print("\n")

    while True:
        if TheWord == "":
            time.sleep(.5)
            print("Congratulations, you won!")
            break
        time.sleep(.5)
        print("Guess a letter:")
        Letter = input().lower()
        if Letter not in Letters_Left:
            if Letter not in Letters_Left_Default:
                time.sleep(.5)
                print("That is an invalid character.")
                continue
            else:
                time.sleep(.5)
                print("You've already guessed that letter!")
                continue
        if TheWord.find(Letter) != -1:
            NewWord = OldWord
            ExtraPositionPoints = 0
            PositionsList = []
            while True:
                if NewWord.find(Letter) == -1:
                    break
                ExtraPositionPoints += 1
                Position = NewWord.find(Letter) + ExtraPositionPoints
                PositionsList.append(Position)
                NewWord = NewWord.replace(Letter, "", 1)
            for y in PositionsList:
                if y in indexes_left:
                    indexes.append(y - 1)
                    indexes_left.remove(y)
            new_character = Letter
            for i in indexes:
                Underscores = Underscores[:i] + new_character + Underscores[i+1:]
            time.sleep(.5)
            print("")
            for character in Underscores:
                print("", character.upper(), end="")
            print("\n")
            Letters_Left.remove(Letter)
            TheWord = TheWord.replace(Letter, "")
            indexes = []
        else:
            Lives -= 1
            Letters_Left.remove(Letter)
            if Lives == 9:
                time.sleep(.5)
                print("         \n"
                    "  |        \n"
                    "  |        \n"
                    "  |        \n"
                    "  |        \n"
                    "  |        \n"
                    "  |        \n"
                    "============ ")
                print("")
                time.sleep(.5)
                for character in Underscores:
                    print("", character.upper(), end="")
                print("\n")
            elif Lives == 8:
                time.sleep(.5)
                print("         \n"
                    "  |        \n"
                    "  |        \n"
                    "  |        \n"
                    "  |        \n"
                    "  |        \n"
                    " /|\       \n"
                    "============ ")
                print("")
                time.sleep(.5)
                for character in Underscores:
                    print("", character.upper(), end="")
                print("\n")
            elif Lives == 7:
                time.sleep(.5)
                print("         \n"
                    "  |------  \n"
                    "  |        \n"
                    "  |        \n"
                    "  |        \n"
                    "  |        \n"
                    " /|\       \n"
                    "============ ")
                print("")
                time.sleep(.5)
                for character in Underscores:
                    print("", character.upper(), end="")
                print("\n")
            elif Lives == 6:
                time.sleep(.5)
                print("         \n"
                    "  |------  \n"
                    "  |     |  \n"
                    "  |        \n"
                    "  |        \n"
                    "  |        \n"
                    " /|\       \n"
                    "============ ")
                print("")
                time.sleep(.5)
                for character in Underscores:
                    print("", character.upper(), end="")
                print("\n")
            elif Lives == 5:
                time.sleep(.5)
                print("         \n"
                    "  |------  \n"
                    "  |     |  \n"
                    "  |     O  \n"
                    "  |        \n"
                    "  |        \n"
                    " /|\       \n"
                    "============ ")
                print("")
                time.sleep(.5)
                for character in Underscores:
                    print("", character.upper(), end="")
                print("\n")
            elif Lives == 4:
                time.sleep(.5)
                print("         \n"
                    "  |------  \n"
                    "  |     |  \n"
                    "  |     O  \n"
                    "  |      \ \n"
                    "  |        \n"
                    " /|\       \n"
                    "============ ")
                print("")
                time.sleep(.5)
                for character in Underscores:
                    print("", character.upper(), end="")
                print("\n")
            elif Lives == 3:
                time.sleep(.5)
                print("         \n"
                    "  |------  \n"
                    "  |     |  \n"
                    "  |     O  \n"
                    "  |     |\ \n"
                    "  |        \n"
                    " /|\       \n"
                    "============ ")
                print("")
                time.sleep(.5)
                for character in Underscores:
                    print("", character.upper(), end="")
                print("\n")
            elif Lives == 2:
                time.sleep(.5)
                print("         \n"
                    "  |------  \n"
                    "  |     |  \n"
                    "  |     O  \n"
                    "  |    /|\ \n"
                    "  |        \n"
                    " /|\       \n"
                    "============ ")
                print("")
                time.sleep(.5)
                for character in Underscores:
                    print("", character.upper(), end="")
                print("\n")
            elif Lives == 1:
                time.sleep(.5)
                print("         \n"
                    "  |------  \n"
                    "  |     |  \n"
                    "  |     O  \n"
                    "  |    /|\ \n"
                    "  |      \ \n"
                    " /|\       \n"
                    "============ ")
                print("")
                time.sleep(.5)
                for character in Underscores:
                    print("", character.upper(), end="")
                print("\n")
            else:
                time.sleep(.5)
                print("         \n"
                    "  |------  \n"
                    "  |     |  \n"
                    "  |     O  \n"
                    "  |    /|\ \n"
                    "  |    / \ \n"
                    " /|\       \n"
                    "============ ")
                time.sleep(.5)
                slowprint("GAME OVER!")
                time.sleep(.5)
                print("The word was ", end="")
                for char in  OldWord:
                    print(char.upper(), end="")
                print(".")
                time.sleep(.5)
                break
    
    time.sleep(.5)
    print("Type A to play again, or E to exit.")

    while True:
        Again_Question = input().lower()
        if Again_Question == "a":
            Again = 1
            break
        elif Again_Question == "e":
            Again = 0
            break
        else:
            time.sleep(.5)
            print("A or E...")
            continue

    if Again != 1:
        time.sleep(.5)
        print("Ok, bye...")
        time.sleep(1)
        break
    elif Again == 1:
        continue