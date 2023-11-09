# 이것이 코딩 테스트다 3-1 거스름
N = input() # 잔돈 입력
length = len(N)
count = 0
while length >= 3: #잔돈의 길이가 100의 자리보다 크거나 같고 N이 500원 이상이면 N-500원
  if int(N) >= 500:
    count += 1
    N = int(N) - 500
    length = len(str(N))
  else:
    break

while length >= 3: #잔돈의 길이가 100의 자리보다 크거나 같고 N이 100원 이상이면 N-100원
  if int(N) >= 100:
    count += 1
    N = int(N) - 100
    length = len(str(N))
  else:
    break

while length >= 2: #잔돈의 길이가 10의 자리보다 크거나 같고 N이 50원 이상이면 N-50원
  if int(N) >= 50:
    count += 1
    N = int(N) - 50
    length = len(str(N))
  else:
    break

while length >= 2: #잔돈의 길이가 10의 자리보다 크거나 같고 N이 10원이상이면 N-10원
  count += 1
  N = int(N) - 10
  length = len(str(N))

print(count)
