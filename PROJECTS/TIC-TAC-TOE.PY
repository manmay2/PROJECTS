#WELCOME TO THE WORLD OF GAMING AND THIS GAME IS OF TIC-TAC-TOE.
def check_Win(x,z):
    win=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in win:
        if(sum(x[i[0]],x[i[1]],x[i[2]])==3):
            print("........X HAS WON THE MATCH........")
            return 1
        elif(sum(z[i[0]],z[i[1]],z[i[2]])==3):
            print("........O HAS WON THE MATCH!! BETTER LUCK NEXT TIME........")
            return 0
        return -1
def main(x,z):
    zero="X" if x[0] else ('O' if z[0] else 0)
    one="X" if x[1] else ('O' if z[1] else 1)
    two="X" if x[2] else ('O' if z[2] else 2)
    three="X" if x[3] else ('O' if z[3] else 3)
    four="X" if x[4] else ('O' if z[4] else 4)
    five="X" if x[5] else ('O' if z[5] else 5)
    six="X" if x[6] else ('O' if z[6] else 6)
    seven="X" if x[7] else ('O' if z[7] else 7)
    eight="X" if x[8] else ('O' if z[8] else 8)
    print(f"{zero} | {one} | {two} ")
    print("--|---|---")
    print(f"{three} | {four} | {five} ")
    print("--|---|---")
    print(f"{six} | {seven} | {eight} ")
def sum(a,b,c):
    return a+b+c
x=[0,0,0,0,0,0,0,0,0]
z=[0,0,0,0,0,0,0,0,0]
t=1
print("RULES ARE AS FOLLOWS: 1 FOR X's TURN AND 0 FOR O's TURN")
while(1):
    main(x,z)
    if(t==1):
        print("CHANCE IS: X")
        v=int(input("ENTER THE VALUE: "))
        x[v]=1
    else:
        print("CHANCE IS: O")
        v=int(input("ENTER THE VALUE: "))
        z[v]=1
    winner=check_Win(x,z)
    if(winner!=-1):
        print("MATCH IS OVER........")
        break
    t=1-t
