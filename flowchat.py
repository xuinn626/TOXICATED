stuBmi = (int(input( "Enter value of your bmi")))
if stuBmi <16:
    print ("you cant take the ride")
else:
    print ("you can take the ride")
    distance = int(input("enter value between 21 - 24"))
    if stuBmi == 21:
        print ("you can take a ride to 28m")
    if stuBmi == 22:
        print ("you can take a ride to 30m")
        if stuBmi == 24:
            print ("you can take a ride to 80m")

