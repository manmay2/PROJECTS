# welcome to the world of QUESTION/ANSWERS/..
#HERE YOU MAY ABLE TO TEST YOUR CAPABLTIES OF SOLVING MCQ'S..
#HOPE IT BENEFITS YOU A LOT..
ans="yes"
d=dict()
Q=0
while ans=="yes":
    Q+=1
    print("QUESTION NO. : ",Q)
    d[Q]=input("ENER YOUR DESIRE OPTION LIKE:  A/B/C/D: ")
    ans=input("WANNA CONTINUE....PLEASE ENTER YES OR NO: ")
print(d)
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
        
    

