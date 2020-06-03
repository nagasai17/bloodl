s=list(input())
p=0
for i in range(0,len(s)//2):
    if(s[i]!=s[-i-1]):
        p=1
if(p==0):
    print(True)
else:
    print(False)
