def intersection(lst1, lst2):  
    temp = set(lst2) 
    lst3 = [value for value in lst1 if value in temp] 
    if(len(lst3)>0):
    	return 1
    else:
    	return 0

def subtract(x,y):
	return [item for item in x if item not in y]