import pandas as pd

def binary_tree(data,threshold):
    
    yes=[]
    no=[]
    
    for wind in data['풍속']:
        if wind>threshold:
            yes.append(wind)
        else:
            no.append(wind)    
            
    data_yes=pd.DataFrame({'풍속' : yes, '예상 지연 여부' : ['Yes']*len(yes)}) 
    data_no=pd.DataFrame({'풍속' : no, '예상 지연 여부' : ['No']*len(no)}) 
    
    return data_no.append(data_yes,ignore_index=True) 

Wind=[1,1.5,2.5,5,5.5,6.5]
Delay=['No','No','No','Yes','Yes','Yes']

data=pd.DataFrame({'풍속':Wind,'지연 여부':Delay})
print(data,'\n')

data_pred=binary_tree(data,threshold=5)
print(data_pred,'\n')

     