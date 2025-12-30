def split_even_odd(l):
    e = []
    o = []
    for i in l:
        i = int(i)
        if i%2 == 0:
            e.append(i)
        else:
            o.append(i)  
    print("even no:",e) 
    print("odd no:",o)         
    return e,o

l = input("enter list :").split()
split_even_odd(l)


'''OR'''

def split_even_odd(l):
    e = []
    o = []
    for i in l:
        i = int(i)
        if i % 2 == 0:
            e.append(i)
        else:
            o.append(i)    
    return e, o
l = input("Enter list of numbers separated by space: ").split()
even_list, odd_list = split_even_odd(l)

print("Even numbers:", even_list)
print("Odd numbers:", odd_list)




'''decorator aik special type ka higher order function hai jo as a argument function leta h aur function hi  return krta hai'''

'''iterator python ka aik object h jo at a time(aik tym pe ) sigle element ko memory assign krta hai'''

'''generator aik type ka iterator h  at a time(aik tym pe ) sigle element ko memory assign krta hai'''

''' diff between iterator nd generator dekhna hai'''
''' diff between yield nd return'''