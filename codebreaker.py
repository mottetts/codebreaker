from random import randint
from sys import argv

script, difficulty = argv

combo = f"{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}"
loot = ['Portuguese Cruzeiros', 'Hungarian Forints', 'Thai Baht', 'Dutch Guilders',
        'silver ducats', 'rusty farthings', 'Gaulish Francs', 'Siamese Guineas']
amt = randint(100,100000)
bounty = f"{amt} {loot[randint(0,len(loot)-1)]}"

easy_mode = """
With your trusty safe decoder you can discern which digits
in the combination that you guess are correct.
"""
hard_mode = """
Your safe reading tool cannot tell you the combo, but it can give you a
hint as to how many digits in your guess are in the right place.
"""

print("""
While searching the ruins of an abandoned city you stumble across an
elegant bank building and find a tightly locked safe underground.
You must guess the four-digit combination to open the safe and
secure the riches.
""")
if difficulty == "easy":
    print(easy_mode)
elif difficulty == "hard":
    print(hard_mode)
print("""
But beware! If you don't guess the combination in ten tries,
the keypad will destruct and the goods will be locked away forever.

Good luck!
""")

print("Enter a four-digit combination to guess.")
guess = input("> ")
num_guesses = 0

while guess != combo and num_guesses < 9:
    if len(guess) == 4:
        print("BUZZ! INCORRECT GUESS!")
        print("Your guess:\n")
        print(guess[0], guess[1], guess[2], guess[3])
        if difficulty == "easy":
            i = 0
            while i < 4:
                if combo[i] == guess[i]:
                    print("^", end=' ')
                else:
                    print(" ", end=' ')
                i += 1
        elif difficulty == "hard":
            j = 0
            korrect = 0
            while j < 4:
                if combo[j] == guess[j]:
                    korrect += 1
                j += 1
            print("Number of digits in the right place:", korrect)
    else:
        print("BLEEP BLOOP! INVALID ENTRY!")

    if num_guesses == 8:
        print("\nLast guess! Choose wisely.")
    else:
        print("\n", 9 - num_guesses, "guesses left.")
    num_guesses += 1
    guess = input("> ")

if guess == combo:
    print("CLICK! The safe unlocks! Inside are", bounty+".")
    print("The money is yours. Well done!")
else:
    print("The keypad beeps a cacophony of beeps and self-destructs.")
    print("The gold is forever lost.")
    print(f"(FYI, it was {combo}. Too bad! Better luck next time.)")


#def GetDifficulty():
#   try:
#   except:
#dif_level = GetDifficulty()
#Play(dif_level)
#
