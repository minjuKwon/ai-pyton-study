def perceptron(w,x):
    
    output=w[1]*x[0]+w[2]*x[1]+w[0]
    
    if output>=0:
        y=1
    else:
        y=0
    return y

X=[[0,0],[0,1],[1,0],[1,1]]
w=[-2,1,1]

print('perceptron 출력')

for x in X:
    print('Input : ',x[0],x[1],', Ouput : ',perceptron(w,x))    