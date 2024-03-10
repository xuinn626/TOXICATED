alphabet= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
x = alphabet.index("z")

print(x)
userinput = input("Enter your message you want to encode:")
shift = int(input("Enter the sift number"))
def encrypt(plane_text , shift_amount):
    encryptedtext = ""
    for _ in plane_text:
        if _ in alphabet:
            position = alphabet.index(_)
            print("position")
            newposition = position + shift_amount
            new= alphabet[newposition]
            encryptedtext += new
    print(encryptedtext)
encrypt(plane_text=userinput,shift_amount=shift)

