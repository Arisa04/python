n=int(input())
count = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]
for i in range(n) :
    b, f, r, v=input().split()
    count[int(b)-1][int(f)-1][int(r)-1]+=int(v)
for i in range(4):
    if i != 0:
        print('####################')
    for j in range(3):
        for k in range(10):
            print(' ', count[i][j][k], end='', sep='')
        print()
