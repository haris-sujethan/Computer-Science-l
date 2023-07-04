#Question Two

def log2(x): 

    if x <= 1: 
        return 0
    else:
        return log2(x/2) + 1