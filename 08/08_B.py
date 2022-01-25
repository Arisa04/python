while True:
    x = input()
    sum = 0
    for d in x:
        sum += int(d)
    if sum==0:
        break
    else:
        print(sum)
