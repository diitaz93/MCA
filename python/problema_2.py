filein=open("hamlet.txt","r")
texto= filein.readlines()
p4=[]
n_lines=len(texto)
for i in range(n_lines):
    line=texto[i]
    palabras=line.split()
    for p in palabras:
        if len(p)>4:
            p4.append(p)
#print p4
max=0
for i in set(p4):
    n=p4.count(i)
    if n>max:
        max=n
        pal=i
print i
print n
    
            
