# 3-1
N = input()
length = len(N)
count = 0
while length>=3:
    if int(N)>=500:
        count+=1
        N = int(N)-500
        length = len(str(N))
    else:
        break

while length>=2:
    if int(N)>=100:
        count+=1
        N = int(N)-100
        length = len(str(N))
    else:
        break

while length>=1:
    if int(N)>=50:
        count+=1
        N = int(N)-50
        length = len(str(N))
    else:
        break

while length>=2:
    count+=1
    N = int(N)-10
    length = len(str(N))

print(count)
