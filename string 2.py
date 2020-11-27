  
s=str(input("dati sirul:"))
n=0
nC=0
nm=0
for i in s:
    if ((ord(i))>=65) and ((ord(i))<=90):
        n+=1

print ("numarul de majuscule este",n)
for i in s:
    if (ord(i)>=48) and (ord(i)<=57):
        nC+=1

print("numarul de cifre este:",nC)
for i in s:
    if (ord(i)>=97) and (ord(i)<=122):
        nm+=1

print("numarul de minuscule este:",nm)