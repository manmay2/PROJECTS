# program to create unique student id, for each student present in the class room.

# student id : SVM-0-MC-002-24


n=int(input("Enter the strength of the classroom : "))
stu_id=list()
for i in range(1,n+1):
    name=input("Enter the full name of the student  : ")
    r=input("Enter the roll number :")
    collg=input("Enter the name of the institution : ")
    year=input("Enter the current year : ")
    if(len(r)==1):
        roll="00"+r
    elif(len(r)==2):
        roll="0"+r
    elif(len(r)==3):
        roll=r

    id=collg.upper()+'0'+name[0]+name[name.find(" ")+1]+roll+year[-2]+year[-1]
    stu_id.append(id)


print(stu_id)
    
    

    

    