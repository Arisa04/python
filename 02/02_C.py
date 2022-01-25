a, b, c = map(int, input().split())
t=a
if b<a:
    a=b
    b=t
t=a
if c<a:
    a=c
    c=t
t=b
if c<b:
    b=c
    c=t
print(a, b, c)
