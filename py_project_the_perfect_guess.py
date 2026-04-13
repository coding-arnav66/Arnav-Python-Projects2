import random

cno = random.randint(1, 100)

uno = -1
guesses = 1

while(uno != cno):
    uno = int(input("enter your guess between 1 to 100: "))
    if (uno > cno):
        print("smaller no please")
        guesses +=1
    elif (cno > uno):
        print("larger no please")
        guesses +=1
print(f"you have successfuly guessed the no {cno} in {guesses} attempt")    