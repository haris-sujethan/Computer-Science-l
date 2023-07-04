#num = int(input("Enter a Number"))
#result = ""
#Neg = ""

#if num <0:
    #Neg = True
    #num = abs(num)
#else:
    #Neg=False
    
#if num == 0:
    #result = '0'

#while num>0:
    #result = str(num%2) + result
   # num = num//2

#if Neg == True:
    #print('-'+result) 

#else:
    #print(result)
    
epsilon = 0.01
y = 24.0
guess = y/2.0
numGuess = 0 

while abs(guess*guess - y) >= epsilon:
    numGuess+=1
    guess = guess -(((guess**2)-y)/(2*guess))
print('Number of Guess', numGuess)
print('square root of',y, 'is about',guess)
