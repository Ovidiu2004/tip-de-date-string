s=input('introduceti CNP-ul: ')
n=0
if (len(s)<13)or(len(s)>13):
    print('CNP este fals')
else:
    for i in s:
        if ord(i) in range(48,58):
            n+=1
    if n==13:
        print('CNP-ul este adevarat')
    else:
        print('CNP-ul este fals') 