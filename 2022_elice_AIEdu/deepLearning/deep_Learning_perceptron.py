def Perceptron(x_1,x_2):
    
    w_0=-5
    w_1=-1
    w_2=5
    
    output=w_0+w_1*x_1+w_2*x_2
    
    if output<0:
        y=0
    else:
        y=1
    return y,output

x_1=0
x_2=2
result,go_out=Perceptron(x_1,x_2)    
print("신호의 총합 : %d" %go_out)

if go_out>0:
    print("학습 여부 : %d\n ==> 학습한다" %result)
else:
    print("학습 여부 : $d\n ==> 학습하지 않는다" %result)