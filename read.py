import os

def ifin(x):
    for y in a:
        if y==i:
            return True
            break
    return False
f2=open("a.txt",'r',encoding= 'UTF-8')
file=open("b.txt","w+")
file.close()
n=0
a=[]
for i in f2.read():
    #print(i,end = '')
    if i !=' ' and i != '\n':
        if not 'a' <= i <= 'z' and (not(ifin)):
            file=open("b.txt",'a')
            file.write(i)
            file.close()
            a.append(i)
            n+=1
print(type(f2.read()))
print(f2.read())
