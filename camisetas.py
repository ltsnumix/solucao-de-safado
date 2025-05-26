N = int(input())
tamanhos = list(map(int, input().split()))
P = int(input())
M = int(input())

qp = tamanhos.count(1)
qm = tamanhos.count(2)

if N == P+M and qp == P and qm == M:
    print("S")
else:
    print("N")
