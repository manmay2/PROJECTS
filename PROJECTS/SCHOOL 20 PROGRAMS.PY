                                            # SCHOOL ASSIGNMENT : 20 PROGRAMS FROM PYTHON
                                            # CREATED BY : MANMAY 


#1. WRITE A  FUNCTION INDEX_LIST(L), WHERE L IS THE LIST OF ELEMENTS PASSED AS ARGUMENT TO THE FUNCTION.
#   tHE FUNCTION RETURN ANOTHER LIST NAMED 'indexList' THAT STORES THE INDICES OF ALL NON-ZERO ELEMENTS OF L.
def INDEX_LIST(L):
    ct=-1
    indexList=list()  
    for i in L:
        ct+=1
        if i!=0:
            indexList.append(ct)
    return indexList



#2. WRITE A FUNCTION ALT(L) THAT WILL DISPLAY THE ALTERNATIVE ELEMENT OF A LIST OF 5.
def ALT(L):
    L.append(L.pop(0))
    print(L)
L=eval(input("Enter the list of 5: "))
ALT(L)
    

#3. THE ELEMENT OF LIST L IS [1,2,3]. WRITE A FUNCTION DISPLAY(L) IN SUCH A WAY THAT IT WILL DISPLAY THE ELEMENT OF LIST LIKE 
#                       1
#                       1  2
#                       1  2  3  
def DISPLAY(L):
    for j in range(len(L)):
        for i in range(0,j+1):
            print(L[i],end=' ')        
        print()    
DISPLAY([1,2,3])                  


#4. WRITE A FUNCTION ADD(L) WHICH WILL DISPLAY THE SUM OF THE 2ND DIAGONAL ELEMENT OF 3 BY 3 LIST.
def ADD(L):
    sum=0
    for i in range(len(L)):
        for j in range(len(L)):
            if((i==0 and j==2) or (i==1 and j==1) or (i==2 and j==0)):
                sum+=L[i][j]
    print("THE SUM OF THE 2ND DIAGONAL IS: ")
    print(sum)
ADD([[1,2,3],[4,5,6],[7,8,9]])



#5. Write a function that reads a file and display the words separated with #
def hass():
    file=input("Enter the file name")
    with open(file) as f:
        li=f.read().split()
        for i in li:
            if(i!=li[len(li)-1]):
                print(i,end='#')
            else:
                print(i)
hass()        




#6. write a function named AMCount() that counts the occurence of A and M (including a and m) and display it.
def AMCount():
    f1=input("ENter any random file name you want")
    with open(f1,"w") as kh:
        str2=input("Enter the string you wanna enter")
        kh.write(str2)
    ct_m=ct_a=0
    with open(f1) as r:
        for i in r.read():
            if(i=="A" or i=="a"):
                ct_a+=1
            elif(i=="M" or i=="m"):
                ct_m+=1
        print("A or a: ",ct_a)
        print("M or m: ",ct_m)
AMCount()

#7. write a method/function DISPLAYWORDS() to read lines from any text file and display the words which are less  than 4
def DISPLAYWORDS():
    kf=input("ENter the file name which you wanna count the words: ")
    with open(kf,"r") as kgf:
        li=kgf.read().split()
        ct=0
        str3=" "
        for i in li:
            if(len(i)<4):
                str3+=i+" "
        return str3 
print(DISPLAYWORDS())






#8. create a function/method named count which will count the size of the file and display it's size in bytes.
def count():
    ct=0
    with open(input("Enter the size of the file which you wanna count the size: ")) as gf:
        for i in gf.read():
            if(i!=" "):
                ct+=1
    return ct
print("Size of the file is: ",count(),"Bytes")





#9. write a method/function that will take marks, name, roll from the user and append in the text file.
def append():
    with open(input("ENTER ANY FILE NAME: "),"w") as fj:
        for i in range(int(input("ENTER HOW MANY INPUTS"))):
            name=input("enter the name of the student: ")
            roll=int(input("ENTER THE ROLL NUMBER: "))
            marks=float(input("ENTER THE MARKS OF THE STUDENT: "))
            rec=name+roll+marks+"\n"
            fj.write(rec)
append()


#10. wap that will combine each line from first file with the corresponding line with the second line.
with open("poem1.txt") as f:
    with open("poem.txt") as g:
        str=''
        while str:
            str=f.readline()+g.readline()
            print(str)


#11. WAP THAT WILL MODIFY THE NAME OF THE ROLL NO. 12 AS GURNAM IN THE FILE Stu.dat.
import pickle 
stu={}
found=False
fin=open("Stu.dat",'rb+')
try:
    while True:
        rpos=fin.tell()
        stu=pickle.load(fin)
        if(stu['Rollno'==12]):
            stu['Name']=='Gurnam'
            fin.seek(rpos)
            pickle.dump(stu,fin)
            found=True
except EOFError:
    if found==False:
        print("Sorry, no matching record found")
    else:
        print("Record successfully updated")
    fin.close()


#12. write a program to open file Stu.dat and search for records with the roll no. as 12 or 14.
#    If found, display the records of that very roll no.
import pickle
stu={}
found=False
fin=open('Stu.dat','rb')
searchkeys=[12,14]
try:
    print("Searching in File Stu.dat...")
    while True:
        stu=pickle.load(fin)
        if stu["Rollno"] in searchkeys:
            print(stu)
            found=True
except EOFError:
    if found=False:
        print("No such records found in the file")
    else:
        print("Search Successful.")
    fin.close()



# 13. WAP that will read the records of this csv file and display them.
import csv
with open('hello.csv','r') as fsh:
    creader=csv.reader(fsh)
    for rec in creader:
        print(rec)

    
#14.  WAP that will display the first three rows fetched from student table of the mysql database 'test'.
import mysql.connector as sqltor
mycon=sqltor.connect(host="anker",user="learner",passwd="thehacker",database="test")
if mycon.is_connected()==False:
    print('Error connecting to MYSQL database....Try again later')
else:
    cursor=mycon.cursor()
    cursor.execute("select * from trial")
    data=cursor.fetchmany(3)
    count=cursor.rowcount
    for row in data:
        print(row)
mycon.close()


#15. WAP THAT WILL INSERT VALUES IN THE MYSQL DATABASE.....VIA CONNECTIVITY B/W PYTHON AND SQL.
import mysql.connector as sqltor
mycon=sqltor.connect(host='localhost',user='root',passwd='Happy',database='test')
if(mycon.is_connected==False):
    print("ERROR IN CONNECTING TO THE SQL DATABASE...PLEASE CHECK EVERYTHING AND TRY AGAIN LATER!!")
else:
    cursor=mycon.cursor()
    q="insert into todo values('{}','{}','{}','{}','{}','{}')".format("hello","world","of","pro","gram","ing")
    cursor.execute(q)
    mycon.commit()
    mycon.close()


#16. WAP THAT WILL UPDATE A PARTICULAR RECORD...IN A DATABASE TABLE...
import mysql.connector as p
mycon=p.connect(host="yup",user="root",passwd='hi',database="hello")
cursor=mycon.cursor()
q1="update todo set TASK_TITLE='{}'".format(" ")
cursor.execute(q1)
mycon.commit()
mycon.close()


#17. wap that will create a function of ASCII(str) which will convert all the strings with its corresponding ASCII////and display.
def ASCII(str1):
    for i in str1:
        if(i!=' '):
            print(ord(i),end='')
        elif(i==' '):
            print(' ',end=' ')
ASCII('TECHNICAL INSTITUTE OF MUNICH')


#18. write a program which will create 2 different function to count the number of vowels and consonant and also print them in a list.
def vowel(str1):
    v='AEIOUaeiou'
    vo=list()
    ct_v=0
    for i in str1:
        if(i in v):
            vo.append(i)
            ct_v+=1
    print("LIST OF THE VOWELS PRESENT IN THE STRING IS: ")
    print(vo)
    print('THE COUNT OF THE VOWELS IS: ')
    print(ct_v)
def conso(str1):
    v='AEIOUaeeiou'
    ct_c=0
    co=list()
    for i in str1:
        if(i not in v):
            ct_c+=1
            co.append(i)
    print("THE COUNT OF THE CONSONANT IS: ")
    print(ct_c)
    print("LIST OF ALL THE CONSONANT IS: ")
    print(co)
vowel('TECHNICAL INSTITUTE OF MUNICH')
conso('TECHNICAL INSTITUTE OF MUNICH')


# STACKS PROGRAMS NEED TO BE DONE ALONE......AS NOT STARTED..