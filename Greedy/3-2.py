# 이것이 코딩 테스트다 3-2 큰 수의 법
num = list(map(int, input().split()))  #배열의 크기, 숫자가 더해지는 횟수, 같은 수 반복 횟수
n = input().split()  #n개의 자연수
n.sort(reverse=True)
count = 1
sum = 0

for i in range(int(num[1])):  #숫자가 더해지는 횟수만큼 반복
  if count % (num[2] + 1) == 0:  #count가 k+1의 배수이면 두 번째로 큰 수 더하기
    sum += int(n[1])
    count = 1

  else:
    count += 1 #count가 k+1의 배수가 아니면 가장 큰 수 더하기
    sum += int(n[0])

print(sum)

# 사용 예시
# 5 8 3
# 2 4 5 4 6
# 결과 46
