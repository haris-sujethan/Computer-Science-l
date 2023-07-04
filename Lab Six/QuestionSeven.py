#Question Seven

def permuatation(L):
    import random    
    P= []
    C= list(L)
    
    while(len(C)!=0):
        
        index = random.randrange(0, len(C))
        
        element = C.pop(index)
        
        P.append(element)
    
    return P

print(permuatation(range(0, 30)))
print(permuatation(range(0, 30)))
print("\n")
print(permuatation([19, 4, 3, 17]))
print(permuatation([19, 4, 3, 17]))
print("\n")
print(permuatation([(0, 0), (20, 0), (20, 10), (0, 10)]))
print(permuatation([(0, 0), (20, 0), (20, 10), (0, 10)]))

 




 
