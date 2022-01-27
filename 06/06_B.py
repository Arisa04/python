n=int(input())
cards = [[False for i in range(13)] for j in range(4)]

for i in range(n) :
    pattern, rank = input().split()
    if pattern=="S":
        pattern=0
    if pattern=="H":
        pattern=1
    if pattern=="C":
        pattern=2
    if pattern=="D":
        pattern=3
    cards[pattern][int(rank)-1] = True
for j in range(4) :
    for i in range(13) :
        if cards[j][i] == False:
            if j==0:
                print("S", i+1)
            if j==1:
                print("H", i+1)
            if j==2:
                print("C", i+1)
            if j==3:
                print("D", i+1)
