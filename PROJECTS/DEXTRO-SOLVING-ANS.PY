# welcome to the world of QUESTION/ANSWERS/..
#HERE YOU MAY ABLE TO TEST YOUR CAPABLTIES OF SOLVING MCQ'S..
#HOPE IT BENEFITS YOU A LOT..
ans="yes"
d=dict()
Q=0
while True:
    Q+=1
    print()
    print()
    print()
    print("QUESTION NO. : ",Q)
    d[Q]=input("ENTER THE CORRECT OPTION LIKE:  A/B/C/D: ")
    print()
    print()
    print()
    print("PRESS YES  TO PROCEED TO THE NEXT QUESTION")
    print("OR PRESS BACK TO PROCEED TO A PARTICULAR QUESTION..YOU WANNA CHANGE")
    print("PRESS NO TO STOP/EXIT")
    ans=input("ENTER YOUR CHOICE PLEASE: ")
    if ans=="yes":
        continue
    elif(ans=="back"):
        q=int(input("ENTER THE QUESTION NUMBER SO THAT YOU MAY CHANGE THE ANSWER: "))
        d[q]=input("ENTER THE CORRECT OPTION LIKE:  A/B/C/D: ")
    else:
        break
    
print()
print()
print()
print("______________________________________________")
print("........# TIME TO CHECK YOURSELF........#")
ct_score=0
for i in d:
    print("QUESTION NUMBER IS: ",i,"AND YOU HAVE OPTED",d[i])
    if(input("ENTER WHETHER THE OPTION YOU HAVE OPTED IS CORRECT OR WRONG")=="correct"):
        ct_score+=1

print()
print()
print()
print("__________________________________________________")
print("TOTAL QUESTION YOU DID CORRECTLY IS: ",ct_score)
print("INCORRECT QUESTIONS YOU DID INCORRECTLY IS: ",Q-ct_score)    
        
    

