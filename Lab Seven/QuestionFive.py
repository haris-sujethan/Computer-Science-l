#Question Five


def isPal(L):
    
    R = L.copy()
    R.reverse()    
    
    if L==R:
        return True
    else:
        return False
