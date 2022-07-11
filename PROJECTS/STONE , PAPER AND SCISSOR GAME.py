import random
def game(user,comp):
    if(user=="R" and comp=="P"):
        return False
    elif(user=="P" and comp=="S"):
        return False
    elif(user=="S" and comp=="R"):
        return False
    elif(user=="P" and comp=="R"):
        return True
    elif(user=="S" and comp=="P"):
        return True
    elif(user=="R" and comp=="S"):
        return True
user=input("please enter any one of the following:- R(ROCK), P(PAPER) AND S(SCISSOR)")
r=random.randint(1,3)
if(r==1):
    comp="R"
elif(r==2):
    comp="P"
elif(r==3):
    comp="S"
print("You have choosen",user)
print("computer have choosen",comp)
game(user,comp)
if(game(user,comp)==True):
    print("YOU WIN, COMPURTER LOSE")
elif(game(user,comp)==False):
    print("YOU LOSE, COMPURTER WINS")
elif(game(user,comp)==None):
    print("THIS MATCH IS A TIE ONE")
