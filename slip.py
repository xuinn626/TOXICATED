import random
Letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
special_characters = ["!","@","#","$","%","^","&"]
print("welcom to password generator")
userLetter = int(input("how many letters do you like as your password:"))
usernumber = int(input("how many numbers do you like as your password:"))
userchar = int(input("how many special characters do you like as your pasword:"))
password = ""
for char in range (1,userLetter +1):
      password += random.choice(Letters)
      print(password)
for char in range (1,usernumber +1):
      password += random.choice(numbers)
      print(password)
for char in range (1,userchar +1):
      password += random.choice(special_characters)
      print(password)
      