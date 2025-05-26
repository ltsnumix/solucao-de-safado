d = int(input())

resto = (d-3)%8

if resto <= 2:
    print(2)
elif resto <= 3:
    print(1)
elif resto <= 5:
    print(3)

