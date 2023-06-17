import pinyin
import pyperclip as cb

s=' '
k=0
r=[]
while s !='':
    
    s=input('Input:')

    if s !='':
        z=[]
        f2=open('b.txt','r')
        num=1
        page=1
        print('Page',page)
        for i in f2.read():
            a = pinyin.get(i, format='strip', delimiter=" ")
            if a==s:
                print('  ',num,i,end='')
                z.append(i)
                num+=1
            if(num>7):
                page+=1
                num=1
                print('\nPage',page)
        print('\n')
        p,n=map(int,input('Page & Number:').split())
        print('Result:',z[(p-1)*7+n-1])
        r.append(z[(p-1)*7+n-1])
    print('-'*25)

ch=''
for i in r:
    print(i,end='')
    ch+=i

print('\n')
cb.copy(ch)
print('Copied to clipboard')
    
while True:
    pass
