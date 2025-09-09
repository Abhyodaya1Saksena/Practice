import random
a=random.randint(0,100)
guess=0
i=0
while(i<=100):
    i=int(input("Enter your guess:"))
    if(i<a):
        print("higher number")
        guess+=1
    if(i>a):
        print("lower number")
        guess+=1
    if(i==a):
        break

print(f"you guessed the number correctly:{a}")
print(f"the number of guesses:{guess}")       
