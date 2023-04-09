import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="",database="project")
cursor=mycon.cursor()
print("_______________________________NUEMANN'S INSTITUTE OF TECHNOLOGY_______________________________")
print("_______________________________WELCOME TO OUR INSTITUTE________________________________________________________")
print("_______________________________________REPORT CARD PRESENTATION_____________________________________________________________")
print("PLEASE SELECT WHAT YOU WANT")
print("__________________________")
print("1. INSERT A STUDENT'S MARKS")
print("2. TO SEE AN INDIVIDUAL STUDENT'S REPORT")
print("3. TO UPDATE/CHANGE A STUDENTS SPECIFIC RECORD")
print("4. TO DELETE A PARTICULAR STUDENT'S WHOLE REPORT CARD")
ch=int(input("ENTER YOUR DESIRE THING WHICH YOU WANNA PROCEED..."))
#1..
if(ch>=1 and ch<=4):
    if(ch==1):
        roll=int(input("ENTER THE ROLL NO. OF THE STUDENT: "))
        name=input("ENTER THE NAME OF THE STUDENT: ")
        cls=input("ENTER THE CLASS IN WHICH THE STUDENT IS STUDYING: ")
        f_name=input("ENTER THE FATHER'S NAME OF THE STUDENT: ")
        m_name=input("ENTER THE MOTHER'S NAME OF THE STUDENT: ")
        dob=input("ENTER THE DATE OF BIRTH OF THE STUDENT IN THE FORMAT YYYY-MM-DD: ")
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
        query="create table if not exists {} (Name varchar(30),Class varchar(5),Father_Name varchar(30),Mother_Name varchar(30),DOB Date,English decimal(10,1),Hindi decimal(10,1),Science decimal(10,1),Social_Science decimal(10,1),Mathematics decimal(10,1),Total_Marks decimal(10,1),Percentage decimal(10,1),Overall_Grade varchar(2));".format(table_name)
        cursor.execute(query)
        query="insert into {} values('{}','{}','{}','{}','{}',{},{},{},{},{},{},{},'{}');".format(table_name,name,cls,f_name,m_name,dob,eng,hin,sci,sst,math,total_marks,per,g)
        cursor.execute(query)    
        mycon.commit()
    elif(ch==2):
        r=int(input("Enter the roll no. of that student:  "))
        c=input("Enter the class:  ")
        t_name=str(r)+c
        cursor.execute("show tables;")
        data=cursor.fetchall()
        for i in data:
            if(i[0]==t_name):
                cursor.execute("select * from {};".format(t_name))
                data1=cursor.fetchall()
                li=["Name","Class","Father's_Name","Mother's_Name","Date_Of_Birth","English","Hindi","Science","Social_Science","Mathematics","Total_Marks","Percentage%","Grade"]
                for i in data1:
                    for j in range(0,len(i)):
                        print(li[j]," : ",data1[0][j])
    elif(ch==3):
        ro=int(input("Enter the Roll No.: "))
        cls=input("Enter the class of the student")
        t_NAME=str(ro)+cls
        cursor.execute("show tables;")
        data2=cursor.fetchall()
        for i in data2:
            if(i[0]== t_NAME):
                print("PLEASE SELECT WHAT THINGS YOU WANT TO CHANGE/UPDATE")
                print("___________________________________________________")
                print("1. NAME OF THE STUDENT")
                print("2. MARKS")
                print("3. CHANGE IN PARENT'S NAME")
                print("4.CHANGE IN DATE OF BIRTH(DOB)")
                choice=int(input("Enter the your choice: "))
                if(choice==1):
                    nam=input("ENTER THE NEW/CORRECTED NAME: ")
                    cursor.execute("update {} set Name='{}'".format(t_NAME,nam))
                    mycon.commit()
                    print("NAME UPDATED SUCCESSFULLY")
                elif(choice==2):
                    print("PLEASE CHOOSE YOUR SUBJECT NAME")
                    print("1.ENGLISH")
                    print("2.HINDI")
                    print("3.SCIENCE")
                    print("4.SOCIAL SOCIAL")
                    print("5.MATHEMATICS")
                    CHOICE=int(input("Enter the number according to which you wanna change: "))
                    if CHOICE==1:
                        ROLL_1=int(input("Enter the roll no. of the student: "))
                        CLASS_1=input("Enter the student's class in which he/she is reading: ")
                        TAB_N=str(ROLL_1)+CLASS_1
                        cursor.execute("show tables;")
                        data_2=cursor.fetchall()
                        for i in data2:
                            if(i[0]==TAB_N):
                                marks=float(input("Enter the updated marks: "))
                                cursor.execute("update English from {} where English={}".format(TAB_N,marks))
                                mycon.commit()
                                print("MARKS UPDATED SUCCESSFULLY")
                        else:
                            print("PLEASE ENTER ALL  THE THINGS CAREFULLY SPECIALLY ROLL AND CLASS OF THE STUDENT....TRY AGAIN LATER")
                    elif CHOICE==2:
                        ROLL_1=int(input("Enter the roll no. of the student: "))
                        CLASS_1=input("Enter the student's class in which he/she is reading: ")
                        TAB_N=str(ROLL_1)+CLASS_1
                        cursor.execute("show tables;")
                        data_2=cursor.fetchall()
                        for i in data2:
                            if(i[0]==TAB_N):
                                marks=float(input("Enter the updated marks: "))
                                cursor.execute("update Hindi from {} where Hindi={}".format(TAB_N,marks))
                                mycon.commit()
                                print("MARKS UPDATED SUCCESSFULLY")
                        else:
                            print("PLEASE ENTER ALL  THE THINGS CAREFULLY SPECIALLY ROLL AND CLASS OF THE STUDENT....TRY AGAIN LATER")
                    elif CHOICE==3:
                        ROLL_1=int(input("Enter the roll no. of the student: "))
                        CLASS_1=input("Enter the student's class in which he/she is reading: ")
                        TAB_N=str(ROLL_1)+CLASS_1
                        cursor.execute("show tables;")
                        data_2=cursor.fetchall()
                        for i in data2:
                            if(i[0]==TAB_N):
                                marks=float(input("Enter the updated marks: "))
                                cursor.execute("update Science from {} where Science={}".format(TAB_N,marks))
                                mycon.commit()
                                print("MARKS UPDATED SUCCESSFULLY")
                        else:
                            print("PLEASE ENTER ALL  THE THINGS CAREFULLY SPECIALLY ROLL AND CLASS OF THE STUDENT....TRY AGAIN LATER")
                    elif CHOICE==4:
                        ROLL_1=int(input("Enter the roll no. of the student: "))
                        CLASS_1=input("Enter the student's class in which he/she is reading: ")
                        TAB_N=str(ROLL_1)+CLASS_1
                        cursor.execute("show tables;")
                        data_2=cursor.fetchall()
                        for i in data2:
                            if(i[0]==TAB_N):
                                marks=float(input("Enter the updated marks: "))
                                cursor.execute("update Social_Science from {} where Social_Science={}".format(TAB_N,marks))
                                mycon.commit()
                                print("MARKS UPDATED SUCCESSFULLY")
                        else:
                            print("PLEASE ENTER ALL  THE THINGS CAREFULLY SPECIALLY ROLL AND CLASS OF THE STUDENT....TRY AGAIN LATER")
                    elif CHOICE==5:
                        ROLL_1=int(input("Enter the roll no. of the student: "))
                        CLASS_1=input("Enter the student's class in which he/she is reading: ")
                        TAB_N=str(ROLL_1)+CLASS_1
                        cursor.execute("show tables;")
                        data_2=cursor.fetchall()
                        for i in data2:
                            if(i[0]==TAB_N):
                                marks=float(input("Enter the updated marks: "))
                                cursor.execute("update Mathematics from {} where Mathematics={}".format(TAB_N,marks))
                                mycon.commit()
                                print("MARKS UPDATED SUCCESSFULLY")
                        else:
                            print("PLEASE ENTER ALL  THE THINGS CAREFULLY SPECIALLY ROLL AND CLASS OF THE STUDENT....TRY AGAIN LATER")
                    else:
                        print("Please enter a valid number from 1 to 5....")
                elif(choice==3):
                    # change in parent's name
                    print("1.WANNA CHANGE FATHER'S NAME")
                    print("2. WANNA CHANGE MOTHER'S NAME")
                    c=int(input("Enter your choice: "))
                    if(c==1):
                        cursor.execute("update {} set Father_Name='{}'".format(t_NAME,input("Enter the updated father's name")))
                        mycon.commit()
                        print("NAME UPDATED SUCCESSFULLY")
                    elif(c==2):
                        cursor.execute("update {} set Mother_Name='{}'".format(t_NAME,input("Enter the updated mother's name")))
                        mycon.commit()
                        print("NAME UPDATED SUCCESSFULLY")
                                
                    
                elif(choice==4):
                    # change in DOB
                        birth=float(input("Enter the UPDATED DATE OF BIRTH: "))
                        cursor.execute("update {} where DOB='{}'".format(t_NAME,birth))
                        mycon.commit()
                        print("DOB UPDATED SUCCESSFULLY")
                else:
                    print("PLEASE ENTER ALL  THE THINGS CAREFULLY SPECIALLY ROLL AND CLASS OF THE STUDENT....TRY AGAIN LATER")
    else:
        # delete a whole report card
        ROLL_1=int(input("Enter the roll no. of the student: "))
        CLASS_1=input("Enter the student's class in which he/she is reading: ")
        TAB_N=str(ROLL_1)+CLASS_1
        cursor.execute("show tables;")
        data2=cursor.fetchall()
        data_2=cursor.fetchall()
        for i in data2:
            if(i[0]==TAB_N):
                cursor.execute("drop table {}".format(TAB_N))
                mycon.commit()
                print("REPORT CARD DELETED SUCCESSFULLY")
else:
    print("PLEASE ENTER A VALID NUMBER FROM 1 TO 4")
        
                    
                            

                            

                            

                            
                    
                    
                        
