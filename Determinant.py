import numpy as np
import random
from datetime import datetime
import copy 
import time
def InputMatrix(X): # Getting data from user 
    n = len(X[0])
    for i in range(0,n):  
        for j in range(0,n):
            X[i][j] = int(input("Enter A["+ str(i) + "][" + str(j) + "] : "))  # get matrix

def PrintMatrix(X,name): # just very simple printing of matrix
    print(name)
    np.set_printoptions(precision=3)
    print('\n'.join(['        '.join(['{:10.5}'.format(item) for item in row]) for row in X])) # Printing matrice 
# [ 0.07837821  0.48002108  0.41274116  0.82993414  0.77610352  0.1023732
#   0.51303098  0.4617183   0.33487207  0.71162095]

def DeclareMatrix(n): # for allocation memory to matrix X 
    X = [[ 0 for x in range(n)] for y in range(n)] # creating a list n*n  and set all elemnts 0
    return X

def Det3(A):
    a=A[0][0];b=A[0][1];c=A[0][2];d=A[1][0];e=A[1][1];f=A[1][2];g=A[2][0];h=A[2][1];i=A[2][2];
    return(a*e*i + b*f*g + c*d*h - c*e*g - b*d*i - a*f*h)

def DetRecursive(a): # main function with the new formula
    det = 0
    n = len(a[0])
    for c0j in range(0,n):
        if(n==3):
            return(Det3(a))
        else:
            a0j = a[0][c0j]
            B = DeclareMatrix(n-1)
            row = 0
            col = 0
            for r in range(1,n):
                for s in range(0,n):
                    if(s!=c0j):
                        B[row][col] = a[r][s]
                        col += 1
                col = 0
                row += 1
        co = ((-1) ** c0j)
        det += co * a0j * DetRecursive(B)
    return (det)


def DetNew(matrix): # main function with the new formula
    n = len(matrix[0]) # get n as our matrix dimension nxn 
    det =1
    a = copy.deepcopy(matrix) # we copy data to new matrix to not effect our intial data
    for k in range(0,n):  
        if a[k][k] == 0 : # if any elemnt in diagnoal is 0 , we have change the column 
            ok = False;
            for j in range(k,n): # we check next rows of column k , if there is at least one elemnt not 0
                ajk = a[j][k]
                if (ajk != 0) :
                    ok = True
            if (ok == False): # it means we are not allowed to exchange the column because of all are 0 
                return 0
            for i in range(k,n):
                temp = a[i][j]
                a[i][j] = copy.deepcopy(a[i][k])
                a[i][k] = copy.deepcopy(temp)
            det = -det;

        det *= a[k][k] # here and next lines : formula for calculate determin 
        if ( k + 1 < n ): # its deficult for me to explain here , 
            for i in range(k + 1,n):
                for j in range(k+1,n):
                    temp = a[i][j] 
                    if(a[k][k]==0):
                        return(0)
                    a[i][j] = a[i][j] - (a[i][k] * a[k][j] / a[k][k])

    return det

def RandomEnteryMatrix(X):
    n = len(X[0])
    for i in range(0,n):  
        for j in range(0,n):
            X[i][j] = random.uniform(-5.00,5.00)
    


FMT = '%H:%M:%S.%f'
for tt in range(0,10):
    n = int(input('\n\n             Enter n as nxn : ')) 
    a =  DeclareMatrix(n) 
    RandomEnteryMatrix(a)



    t1 = datetime.now().strftime(FMT)
    det = DetRecursive(a) 
    t2 = datetime.now().strftime(FMT)
    PrintMatrix (a,'DetRecursive matrix = ' + str(det))# just printing the result
    trec = datetime.strptime(t2, FMT) - datetime.strptime(t1, FMT)
    print(t1,'   to   ',t2,'    DetRecursive Performed in = ',trec,'\n\n\n')

    t3 = datetime.now().strftime(FMT)
    det = DetNew(a) 
    t4 = datetime.now().strftime(FMT)
    PrintMatrix (a,'DetNew matrix = ' + str(det))# just printing the result
    tnew = datetime.strptime(t4, FMT) - datetime.strptime(t3, FMT)
    print(t3,'   to   ',t4,'    DetRecursive Performed in = ',tnew,'\n\n\n')
    #tduration = trec - tnew;
    #tduration = datetime.strptime(trec, FMT) - datetime.strptime(tnew, FMT)
    #print('diffrence is  = ',tnew)

      
