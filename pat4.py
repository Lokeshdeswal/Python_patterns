n = 4
i=1
while i<=n:
    j=1
    s=chr(ord('A')+i- 1)
    while j<=n:
        charp=chr(ord(s )+j-1)
        print(charp,end='')
        j +=1
        
    print()
    i+=1
