# write the function definition and import all the necessary module
def printvals(n):
    i = 1
    l=[]
    while i !=n+1:
        if i %15 == 0:
            l.append('AB')
        elif i %3==0:
            l.append('A')
        elif i%5==0:
            l.append('B')
        else:
            l.append(i)
        i+=1
    l2 = l[::-1]
    length = len(l2)
    return l

print (printvals(15))