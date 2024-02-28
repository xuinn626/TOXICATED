import random
FootballTeams = ["Barcelona""Real madrid","chelsea","Arsenal","Liverpool","manchester city","Manchester United"]
chosenword = random.choice(FootballTeams)
wordlength = len(chosenword)
print(f"chosen word is",chosenword)
diplay = []

for _ in range(wordlength):
   display += "_"
#print(diplay) 
endOfGame = False
while not endOfGame :
    guess = input("guess a word")

    for position in range(wordlenght): 
    letter = chosenword[position]
    if letter == guess:
        display[position] = letter

    print(display)
