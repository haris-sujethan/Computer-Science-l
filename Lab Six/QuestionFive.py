#Question Five

L= [(i) for i in range(1,101)]
print(L)

L_2=[i for i in range(1,102) if i%2!=0]
print(L_2)

L_3=[i**2 for i in range(1,50)]
print(L_3)

import random
L_4=[(random.randrange(0, 50)) for i in range(0,60)]
print(L_4)

L_5=[(0) for i in range(1,51)] 
print(L_5)
