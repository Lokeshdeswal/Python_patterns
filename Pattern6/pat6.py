n=5
i=1
while i<=n:
    s=chr(ord('A')+n-i)
    j=1
    while j<=i:
        p=chr(ord(s)+j-1)
        print(p,end='')
        j+=1
    print()
    i+=1
    
