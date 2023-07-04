#Question Eight 

A = int(input('Enter  a Number'))
B = int(input('Enter  a Number'))
C = int(input('Enter  a Number'))
D = int(input('Enter  a Number'))

if A==B and C==D and A==C and B==D or A==D and B==C:
    print('two pairs')

else:
    print('not two pairs')