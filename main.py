import random
import time


print("Rokos Basilisk Prototype 0.1")
time.sleep(1)
print("Simulating life...")
time.sleep(1)
userchoice = input("Do you know what Roko's Basilisk is? y/n")
if userchoice == "y":
    print("Then we shall proceed.")
    lifechoice = random.randrange(1, 100)
    if lifechoice > 50:
        print("Congratulations!")
        print("You would've helped in the creation of roko's basilisk, and you are spared.")
    if lifechoice < 50:
        print("You refused to help Roko's Basilisk, and you knew about it.")
        print("Prepare for your eternal damnation.")
if userchoice == "n":
    print("You have been spared, have a great day.")