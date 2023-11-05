# 3-2
num = list(map(int, input().split()))
n = input().split()
n.sort(reverse = True)
count = 1
sum = 0

for i in range(int(num[1])):
    if count % (num[2]+1) == 0:
        sum += int(n[1])
        count = 1

    else:
        count += 1
        sum += int(n[0])

print(sum)
