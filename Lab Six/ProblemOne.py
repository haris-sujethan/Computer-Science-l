#Question One

List1=[]
x=0
y=10
while x<y:
    element=input("Please Enter A String: ")
    List1.append(element)
    x+=1
    
print("\n")
print("In Order")
print("\n")
for i in range(len(List1)):
    print(i,"/10""\t",List1[i])

print("\n")

print("In Reverse")
print("\n") 
for i in range(len(List1)-1,-1,-1):
    print(i,"/10""\t",List1[i])



