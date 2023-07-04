#Question Three

def longest(L):
    
    x=0
    for i in L:
        
        if x==0:
            largestyet=i
            x=1 
        else:
            if len(largestyet)<len(i):
                largestyet=i
    return largestyet