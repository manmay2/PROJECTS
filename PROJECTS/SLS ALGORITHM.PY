paas=input("ENTER THE PASSWORD: ")#Abc%14312$3
li_paas=list()
num_str=['4','3','1','9','0','2','7','5','6','8']
sym_str=['!','@','#','$','%','^','&','*','(',')']
sym2_str=['~','`','_','-','+','"','=','?','/',',']
sym3_str=['<','>','.']
for i in paas:
    if(i not in num_str and i not in sym_str and i not in sym2_str):
        k=str(ord(i))
        li_paas.append(k)
    elif (i in sym_str):
        li_paas.append(num_str[(sym_str.index(i))])
    elif (i in sym2_str):
        li_paas.append(num_str[(sym2_str.index(i))])
    elif (i in sym3_str):
        li_paas.append(num_str[(sym3_str.index(i))])
    else:
        li_paas.append(i)
step1='' 
for j in li_paas:
    step1+=j
step2=''
pow=len(step1)+1
st=''
for g in step1:
    pow=pow-1
    st=st+str(int(i)**pow)
for jk in st:
    if(jk in num_str):
        step2=step2+jk
step1=int(step1)
step2=int(step2)
final_step=((step2//step1)*(step2-step1)-(step1+step2))*4319027568
print(final_step)
print(len(str(final_step)))






    




