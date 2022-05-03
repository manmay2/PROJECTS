import random
def game(user,comp):
    if(user=="s" and comp=="w"):
        return True
    elif(user=="w" and comp=="g"):
        return True
    elif(user=="s" and comp=="g"):
        return False
    elif(user=="w" and comp=="s"):
        return False
    elif(user=="g" and comp=="w"):
        return False
    elif(user=="g" and comp=="s"):
        return True
user=input("choose any one of this s(snake) or w(water) or g(gun)")
rand=random.randint(1,3)
if(rand==1):
    comp="s"
elif(rand==2):
    comp="w"
elif(rand==3):
    comp="g"
print("you has choosen",user)
print("computer has choosen",comp)
if(game(user,comp)==None):
    print("MATCH HAS BEEN A TIE")
elif(game(user,comp)==True):
    print("YOU WIN, COMPUTER LOSE")
if(game(user,comp)==False):
    print("YOU LOSE, COMPUTER WIN")
