#Question Four

#Part a)
T=()
L=[]
for x in range(1,101):
    
    L.append(x)
    L=list(T)
    L.append(x)
    T=tuple(L)
print(T)
print(L)
    
#part b)
T2=()
L_2=[]
for x in range(1,102):
    
   if x%2!=0:
    L_2.append(x)
    L_2=list(T2)
    L_2.append(x)
    T2=tuple(L_2)
print(T2)
print(L_2)
    
#part c)
T3=()
L_3=[]
for x in range(1,50):
   
    x = x**2
    L_3.append(x)
    L_3=list(T3)
    L_3.append(x)
    T3=tuple(L_3)
print(T3)
print(L_3)

#part d)
T4=()
L_4=[]
n = 0
import random
while n<60: 
    x = random.randrange(0, 50)
    L_4.append(x)
    L_4=list(T4)
    L_4.append(x)
    T4=tuple(L_4)
    n+=1
print(T4)
print(L_4)
    
#part e)
T5=()
L_5=[]
for x in range(1,51):
   
    x = 0
    L_5.append(x)
    L_5=list(T5)
    L_5.append(x)
    T5=tuple(L_5)
print(T5)
print(L_5)

    