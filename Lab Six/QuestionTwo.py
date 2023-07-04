#Question Two

def max(L):
    
    i = 0
    for a in L:
        if type(a)==float:
         if i==0:
             x=a
             i=1
         else:
             if x<a:
                 x=a
    if i==0:
       
        return 'None'
    
    return 'the largest object of type float is',x
        
