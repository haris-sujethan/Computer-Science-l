#Question Six

def powerHalf(x, n):
    if n%2 !=0:
        return None 
    else:
        global countcalls
        countcalls+=1
        return x**(n/2)**2
    
countcalls = 0
