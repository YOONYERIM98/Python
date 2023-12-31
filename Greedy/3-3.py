# 이것이 코딩 테스트다 3-3 숫자 카드 게임
n, m = map(int, input().split()) # n * m 입력

result = 0

for _ in range(n): # n행 만큼 반복하면서 카드 값 입력
  data = list(map(int, input().split()))
  minval = min(data) # n행의 가장 작은 카드 값 찾기

  result = max(result, minval) # 가장 큰 카드 값 찾기

print(result)

# 사용 예시
# 3 3
# 3 1 2
# 4 1 4
# 2 2 2
# 결과 2

# 2 4 
# 7 3 1 8
# 3 3 3 4
#결과 3
