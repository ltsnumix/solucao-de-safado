s = int(input())
a = int(input())
b = int(input())

contagem = 0

for num in range(a, b+1):
    if sum(int(d) for d in str(num)) == s:
        contagem+=1

print(contagem)
