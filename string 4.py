a=str(input('primul cuvant e: '))
b=str(input('al doilea cuvant e: '))
c=str(input('al treilea cuvant e: '))
d=str(input('al patrulea cuvant e '))
if ((len(a)<3) or (len(b)<3) or (len(c)<3) or (len(d)<3)):
    print('nu corespunde conditiei')
else:
    x=a[:2]
    y=b[:1]
    z=c[:3]
    len1=((len(d))//2)
    len2=len1
    w=d[:len2]

    print('primul cuvant citit e: ',a)
    print('al doilea cuvant citit e: ',b)
    print('al treilea cuvant citit e: ',c)
    print('al patrulea cuvant citit e: ',d)
    cuvantul=x+y+z+w
    print('cuvantul format e = ',cuvantul)