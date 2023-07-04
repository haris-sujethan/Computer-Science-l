#x = int(input("Enter a Number"))
#y = 0 

#while y**3 <x:
    #y+=1
    
#if y**3 !=x :
    #print("Nah")

#else:
    #print("Ye", y)




#s = 'absdejkfdsngjlsdhfgnku'

#for char in s:
    #if char =='i' or char =='u':
        #print("Has i or u")
        
        
        
        
#cube = 27
#epslion=0.01
#guess = 0.0
#increment = 0.0001
#numgues= 0

#while abs(guess**3 - cube)>=epslion and guess<=cube:
    #guess+=increment
    #numgues+=1
    
#print('Number of Guess ',numgues)

#if abs(guess**3-cube) >=epslion:
    #print('failed')    
    
#else:
    #print(guess," is close to",cube)
    
    
    
x =25
eplsion= 0.01
numguess=0
low=0.0
high=x
ans = (high + low)/2.0

while abs(ans**2 -x) >=eplsion:
    print('low= ',low,' high=',high, ans)
    numguess+=1
    if ans**2 < x:
        low = ans
    else:
        high = ans 
    ans = (high + low)/2.0
print('Number of Guess', numguess)
print(ans,'is close to the square root of',x)
    
