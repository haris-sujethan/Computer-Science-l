#Question Seven

f = open('kdpF.txt') 
line = f.readline() 
print(line)
seq = ''
for line in f : 
 seq = seq + line
seq = seq.replace('\n', '') 
seq = seq.upper()
print(seq)

def gcContent(seq):
    x=seq.count('G')
    y=seq.count('C')
    T=len(seq)
    print("The Percent of G's and C's in the sequence is",x+y/T,"%") 


