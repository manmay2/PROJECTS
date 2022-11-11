def ADD(L):
    sum=0
    for i in range(len(L)):
        for j in range(len(L)):
            if((i==0 and j==2) or (i==1 and j==1) or (i==2 and j==0)):
                sum+=L[i][j]
    print("THE SUM OF THE 2ND DIAGONAL IS: ")
    print(sum)
ADD([[1,2,3],[4,5,6],[7,8,9]])