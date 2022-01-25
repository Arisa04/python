x=0
while x<3000:
    a, b = map(int, input().split())
    t=a
    if b<a:
        a=b
        b=t
    if a==0 and b==0:
        break
    print(a, b)
    x=x+1
