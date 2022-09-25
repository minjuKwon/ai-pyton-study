def perceptron(w,x):
    
    output=w[1]*x[0]+w[2]*x[1]+w[3]*x[2]+w[4]*x[3]+w[0]
    
    if output>=0:
        y=1
    else:
        y=0        
    return y,output

x=[1,2,3,4]
w=[2,-1,1,3,-2]

y,output=perceptron(w,x) 

print('output : ',output)
print('y : ',y)    