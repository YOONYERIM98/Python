# 이것이 코딩 테스트다 3-3 숫자 카드 게임
n, m = map(int, input().split())

result = 0

for _ in range(n):
  data = list(map(int, input().split()))
  minval = min(data)

  result = max(result, minval)

print(result)
