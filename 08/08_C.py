alf=[0]*26
while True:
    try:
        str=input().lower()
    except:
        break
    for ch in str:
        if 'a'<=ch and ch<='z':
            alf[ord(ch)-ord('a')]+=1

for i in range(26):
    print(chr(ord("a")+i),":",alf[i])
