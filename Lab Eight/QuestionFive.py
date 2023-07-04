#Question Five

def power(x, n):
    if n ==0:
        return 1 
    else:
        
        global countcalls
        
        countcalls+=1
        
        return x*x**(n-1)
    
countcalls = 0




    


