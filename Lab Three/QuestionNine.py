#Question Nine

typet= input('What Type of Temperature? (C for Celsius or F for Fahrenheit)')
typea= int(input('What is the Temperature Value?'))

if typet == 'C' or typet == 'c':
    if typea<=0:
        print('Solid')
    elif typea>0 and typea<100:
        print('Liquid')
    elif typea>=100:
        print('Gaseous')

if typet == 'F' or typet == 'f':
    if typea<=32:
        print('Solid')
    elif typea>32 and typea<212:
        print('Liquid')
    elif typea>=212:
        print('Gaseous')