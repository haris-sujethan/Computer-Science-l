#Question Seven 

x = input('Enter Decimal Numbers Seperated by Commas: ')
y = ''
total = 0
for c in x:
    y = y + c
    if c == ',':
        total = total + float(y[0:len(y)-1])
        y = ''
total = total + float(y) 
print ('The sum is', total)