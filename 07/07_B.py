while True:
    n,x = map(int, input().split())
    y=0
    if n==0 and x==0:
        break
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i+j+k+3==x and i<j and j<k:
                    y=y+1
    print(y)   
