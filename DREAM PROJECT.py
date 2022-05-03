import frontyer
while True:
    userInp = input("frontyer> ")
    if(userInp == "exit();"):
        break
    else:
        symbol="+-*/"
        mid_sym=''
        for i in userInp:
            for j in symbol:
                if(i==j):
                    mid_sym=j
                    break
                else:
                    continue
        if(mid_sym==''):
            frontyer.run("ERROR! OPERATOR NOT FOUND!!")
            break
        class Assign_Op:
            def add(self):
                return (self.a+self.b)
            def sub(self):
                return (self.a-self.b)
            def mul(self):
                return (self.a*self.b)
            def div(self):
                return (self.a/self.b)
        num=Assign_Op()
        li_split=userInp.split(mid_sym)
        if(li_split[1]!="" and li_split[0]!=""):
            if(len(li_split)==2):
                num.a=int(li_split[0])
                num.b=int(li_split[1])
                if(mid_sym=="+"):
                    frontyer.run(num.add())
                elif(mid_sym=="-"):
                    frontyer.run(num.sub())
                elif(mid_sym=="*"):
                    frontyer.run(num.mul())
                elif(mid_sym=="/"):
                    frontyer.run(num.div())
        else:
            if(len(li_split)==2):
                if(li_split[0]=="" and li_split[1]==""):
                    frontyer.run("NO VALUE HAS BEEN ENTERED!!ONLY OPERATOR ENTERED!!")
                elif((li_split[0]!="" and li_split[1]=="") or (li_split[0]=="" and li_split[1]!="")):
                    frontyer.run("ONE VALUE IS MISSING!!!!")
            elif(len(li_split)==0):
                frontyer.run("ERROR VALUES NOT FOUND FOR THE OPERATION")
            
                
    
