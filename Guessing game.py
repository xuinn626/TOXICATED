word = "CANADA"
allowed_errors = 8
Gusses = []
done = False
while not done:
    print("Hidden word:")
    
    for letter in word:
        if letter.lower in Gusses:
            print(letter,end="")
            break
else:
    print("_",end="")
    Gusses = input("errors left(allowed_errors)\n Enter a letter..........\n")
    Gusses.append(Gusses.Lower())
if Gusses.Lower()not in word.Lower():
      allowed_errors -= 1
if allowed_errors == 0:
        
  done =True
for letter in word:
    if letter.lower()not in Gusses:
        done = False

    if done :
            print("You are a winner:\n You gussed the word \n>>>(word)<<<")
    else:
            print("GAME OVER:\n the hidden word is\n>>>(CANADA)<<<")