N, M = map(int, input().split())
Edges = []
for i in range(M):
    start, end, weight = map(int, input().split())
    Edges.append([weight, start, end])
print(Edges)
Edges.sort()
print(Edges)
Comp = [i for i in range(N+1)]
Ans = 0
for weight, start, end in Edges:
    if Comp[start] != Comp[end]:
        Ans += weight
        a = Comp[start]
        b = Comp[end]
        for i in range(N):
            if Comp[i] == b:
                Comp[i] = a
print(Ans)