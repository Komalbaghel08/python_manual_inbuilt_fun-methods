def common_elements(l1,l2):
    result=[]
    for i in l1:
        for j in l2:
            if i == j :
                if i not in result:
                    result.append(i)
    return result
l1 = [1,22,43,1,2]
l2 = [2,33,22,1]       
print("common elements: ",common_elements(l1,l2))         