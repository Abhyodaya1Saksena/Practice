''' 1 is for snake
-1 is for water
0 is for gun'''
import random

computer= random.choice([0,-1,1])
youstr=input("Enter your choice:")

youdict={"s":1,"w":-1,"g":0}
you=youdict[youstr]
reversedict={1:"snake",-1:"water",0:"gun"}
print(f"you chose {reversedict[you]}")
print(f"computer chose {reversedict[computer]}")


if(you==computer):
    print("its a draw")
else:
    if(you==1 and computer==-1):
        print("You win!")
    elif(you==0 and computer==-1):
        print("You lose!")
    elif(you==1 and computer==0):
        print("You lose!")
    elif(you==-1 and computer==0):
        print("You win!")
    elif(you==0 and computer==1):
        print("You win!")
    elif(you==-1 and computer==1):
        print("You loose!")
    else:
        print("Something went wrong")