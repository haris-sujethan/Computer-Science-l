#Question Three

x = int(input('Enter a Number'))

if x<0:
    x=x*-1 

if x>1000000:
    print('lots')

elif x==1000000:
    print('7 digits')

elif x>=100000:
    print('6 digits')

elif x>=10000:
    print('5 digits')
    
elif x>=1000:
    print('4 digits')

elif x>=100:
    print('3 digits')
    
elif x>=10:
    print('2 digits')

elif x>=1:
    print('1 digit')