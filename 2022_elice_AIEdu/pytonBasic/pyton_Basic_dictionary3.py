students={}

for i in range(4):
    name=input()
    score=int(input())
    students[name]=score

for name in students.keys():
    score=students[name]
    grade=""
    if score>=90:
        grade='A'
    elif score>=80:
        grade='B'
    elif score>=70:
        grade='C'
    elif score>=60:
        grade='D'
    else:
        grade='F'
    print(name+": "+grade)    
    