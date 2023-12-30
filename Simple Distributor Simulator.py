import time as tm
import random as rm

typein = ["Distribute", "Work", "Distribute 1km", "I love distributing", "Work Hard", "Distributing 8km away", "Distributing 2km away", "Distributing 7km away"]

def Menu():
    print("Distributor Simulator")
    print("1. Play Game")
    print("2. About this Game")
    print("3. Exit Game")
    
def About():
    print("This game was created by a person on Internet with nickname Nuno337 and this is an open source text based game")

money = 100

pkglist = ["1Kg Apple", "1Kg Banana", "1Kg Avocado", "1 Box Instant Mie", "1 Box Music Disc", "1Kg Beef", "2 TV"]

pkg = {"1Kg Apple" : 100, "1Kg Banana" : 85, "1Kg Avocado" : 115, "1 Box Instant Mie" : 127, "1 Box Music Disc" : 195, "1Kg Beef" : 150, "2 TV" : 200}
    
while True:
    try:
        Menu()
        chc1 = int(input("Please input your choice 1/2/3: "))
        if chc1 == 3:
            print("Leaving the game...")
            tm.sleep(0.9)
            print("Success")
            break
        elif chc1 == 2:
            About()
        elif chc1 == 1:
            while True:
                typeinran = rm.choice(typein)
                print("Your money: ", money)
                task = str(input("Press Enter to see your task: ")).lower()
                if task.lower() != "leave":    
                    pkgdis = rm.choice(pkglist)
                    print("Your task is to deliver: ", pkgdis)
                    while True:
                        print("Please type", typeinran, "To distribute (Capital Letters Matter)")
                        dis = str(input("Input: "))
                        if dis == typeinran:
                            print("Successfully Distributed")
                            money += pkg[pkgdis]
                            print("Money +", pkg[pkgdis])
                            print("Tips: If you want to leave just type leave when you have to press Enter to get into your task")
                            break
                        else:
                            print("Wrong!")
                else:
                    print("Leaving the game...")
                    tm.sleep(1)
                    break
    except ValueError:
        print("Please input a valid value")