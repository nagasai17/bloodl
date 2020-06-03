s=list(map(int,input().split(" ")))
h={}
t=int(input())
for i in range(len(s)):
    
    if(s[i] in h):
        print([h[s[i]],i])
    else:    
        h[t-s[i]]=i
       
