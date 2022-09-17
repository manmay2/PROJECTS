import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="2%0*2)0$Happy",database="project")
ans="yes"
cursor=mycon.cursor()
ans=input("DO YOU WANT TO ENTER FOR STUDENTS GRADE: YES/NO ??????").lower()
while ans=="yes":
    roll=int(input("ENTER THE ROLL NO. OF THE STUDENT: "))
    name=input("ENTER THE NAME OF THE STUDENT: ")
    cls=input("ENTER THE CLASS IN WHICH THE STUDENT IS STUDYING: ")
    f_name=input("ENTER THE FATHER'S NAME OF THE STUDENT: ")
    m_name=input("ENTER THE MOTHER'S NAME OF THE STUDENT: ")
    dob=input("ENTER THE DATE OF BIRTH OF THE STUDENT: ")
    eng=float(input("ENTER THE MARKS IN ENGLISH: "))
    hin=float(input("ENTER THE MARKS IN HINDI: "))
    sci=float(input("ENTER THE MARKS IN SCIENCE: "))
    sst=float(input("ENTER THE MARKS IN SOCIAL SCIENCE: "))
    math=float(input("ENTER THE MARKS IN MATHEMATICS: "))
    total_marks=eng+hin+sci+sst+math
    per=(total_marks*100)/500
    if(per>90):
        g="A+"
    elif(per>80 and per<=90):
        g="A"
    elif(per>70 and per<=80):
        g="B+"
    elif(per>60 and per<=70):
        g="B"
    elif(per>50 and per<=60):
        g="C+"
    elif(per>40 and per<=90):
        g="C"
    elif(per<40):
        g="D"
    table_name=str(roll)+cls
    query="create table {} (Name varchar(30),Class varchar(3),Father_Name varchar(30),Mother_Name varchar(30),DOB Date,English decimal(10,1),Hindi decimal(10,1),Science decimal(10,1),Social_Science decimal(10,1),Mathematics decimal(10,1),Total_Marks decimal(10,1),Percentage decimal(10,1),Overall_Grade varchar(2));".format(table_name)
    cursor.execute(query)
    query="insert into {} values('{}','{}','{}','{}','{}',{},{},{},{},{},{},{},'{}');".format(table_name,name,cls,f_name,m_name,dob,eng,hin,sci,sst,math,total_marks,per,g)
    cursor.execute(query)    
    mycon.commit()
    ans=input("DO YOU WANT TO ENTER FOR MORE STUDENTS: YES/NO ??????").lower()
a=input("WANNA SEE THE RESULTS OF A PARTICULAR STUDENT...YES/NO????").lower()
if(a=="yes"):
    r=int(input("Enter the roll no. of that student:  "))
    c=input("Enter the class:  ")
    t_name=str(r)+c
    cursor.execute("show tables;")
    data=cursor.fetchall()
    for i in data:
        if(i[0]==t_name):
            cursor.execute("select * from {};".format(t_name))
            data1=cursor.fetchall()
            print("_______________________________NUEMANN'S INSTITUTE OF TECHNOLOGY_______________________________")
            print("_______________________________WELCOME TO OUR INSTITUTE_______________________________")
            print("_______________________________________REPORT CARD___________________________________________________________________________________")
            li=["Name","Class","Father's_Name","Mother's_Name","Date_Of_Birth","English","Hindi","Science","Social_Science","Mathematics","Total_Marks","Percentage%","Grade"]
            for i in data1:
                for j in range(0,len(i)):
                    print(li[j]," : ",data1[0][j])


