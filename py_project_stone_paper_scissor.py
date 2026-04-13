#stone 1
#papaer 2
#scissor 3
while True:
    import random

    comp = random.choice([1, 2 ,3])
    youstr = input("enter your choice(stone/paper/scissor): ")
    youdict = {
                "stone" : 1,
            "paper" : 2,
                "scissor" : 3
    }
    you = youdict[youstr]

    if(you == comp):
        print("computer chose the same, \n draw")
    else:
        if(comp == 1 and you == 2):
            print("computer chose stone\nyou win ")
        elif(comp == 1 and you == 3):
            print("computer chose stone\nyou loose")
        elif(comp == 2 and you == 1):
            print("computer chose paper\nyou loose")
        elif(comp == 2 and you == 3):
            print("computer chose paper\nyou win")
        elif(comp == 3 and you == 1):
            print("computer chose scissor\nyou win")
        elif(comp ==3 and you == 2):
            print("computer chose scissor\nyou loose")