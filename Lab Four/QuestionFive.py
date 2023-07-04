#Question Five 
print('Enter an Intger')

list = []
odds = False

for i in range(1,11):
    i = int(input('Number: ')) 
    list.append(i)
    

list = sorted(list, reverse = True)

for x in list:
    if x%2 == 1:
        print('The largest odd number is', x)
        odds = True
        break

if odds == False:
    print('No odd number Entered')