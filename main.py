n = int(input())
list = list(map(int, input().split()))
list.sort()
arr = []
result = 0
for i in range(1, n+1):
    m = sum(list[0 : i])
    arr.append(m)

print(sum(arr))