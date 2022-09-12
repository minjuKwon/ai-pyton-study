def get_students(N):
    students={}
    
    for i in range(N):
        name=input()
        score=int(input())
        students[name]=score
    
    return students   
 
def get_grade(s):
    if s>=90:
        grade='A'
    elif s>=80:
        grade='B'
    elif s>=70:
        grade='C'
    elif s>=60:
        grade="D"
    else:
        grade="F"
    return grade

N=int(input())
students=get_students(N)
for student_name in students.keys():
    print(student_name+": "+get_grade(students[student_name]))