my_dict={}
my_dict[1]="Integer"
my_dict['a']="String"
my_dict[(1,2,3)]="Tuple"

print(my_dict)
try:
    my_dict[[1,2,3]]="List"
except TypeError:
    print("list는 Dictionary의 Key가 될 수 없습니다.")