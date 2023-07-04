#Question One

x=int(input('Enter an integer: '))
y = 0

while y**4 < abs(x):
    y = y + 1
if y**4 != abs(x):
    print (x, 'is not a fourth root')
else:
    if x < 0:
        y = -y
    print ('fourth root of ' + str(x) + ' is ' + str(y))