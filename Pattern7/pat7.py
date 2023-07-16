n=4
i=1
p=1
while i<=n:
    j=1
    
    while j<=i:
        if i==1:
            print('1',end='')
        elif j==1:
            print('1',end='')
        elif i==j:
            print('1',end='')
        else:
            print('2',end='')
        j+=1
    print()
    i+=1
        
        
