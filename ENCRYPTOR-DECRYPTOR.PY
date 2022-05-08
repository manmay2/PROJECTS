#WELCOME TO THE WORLD OF ENCRYPTOR AND DECRYPTOR WORLD....
# USER WILL BE ENTERING ANY STRING OR NUMBER AND CHARACTER ON ITS OWN AND THIS ECRYPTOR AND DECRYPTOR WILL CONVERT WITH IT'S HASH ALGORITHM.
import random
global li
li=["!","@","#","$","%","^","&","*","(",")","_","+","=","'",":","{","}","]","[","<",">","?","~","*"]
def encrypt(pas):
    l=len(li)
    ct=0
    s1=''
    for i in pas:
        if(i==' '):
            pass
        else:
            q=random.randint(1,4)
            r=random.randint(1,l-1)
            if(r%2==0):
                i=i.upper()
            else:
                i=i.lower()
            r1=random.randint(1,l-1)
            r2=random.randint(1,l-1)
            r3=random.randint(1,l-1)
            m=random.randint(1,4)
            m1=random.randint(1,4)
            m2=random.randint(1,4)
            m3=random.randint(1,4)
            s1=s1+i
            ct=ct+1
            if(ct==q):
                s1=s1+(li[r]*m)+(li[r1]*m1)+(li[r2]*m2)+(li[r3]*m3)
                ct=0
    return s1

def decrypt(w):
    return w


pas=input("ENTER THE PASSWORD: ")
w=pas
print("THE PASSWORD AFTER APPLYING HASH ALGORITHM IS: ")
print(encrypt(pas))
print("  ")
print("  ")
print("ORIGINAL TYPED PASSWORD IS: ")
print(decrypt(w))

