stair = []

c = int(input())  # 계단 수
dp = [0]*c

for i in range(c):
  stair.append(int(input()))  # 계단의 점수 입력

# 초기 값
if c == 0:  # 계단의 수가 0인 경우
  print(0)
elif c >= 3: # 3개 이상의 계단 수
  dp[0] = stair[0]
  dp[1] = stair[0]+stair[1]
  dp[2] = max(stair[0]+stair[2],stair[1]+stair[2])

  for n in range(3, c):
    dp[n] = max(dp[n-2]+stair[n],dp[n-3]+stair[n-1]+stair[n])

  print(dp[-1])
else: # 계단의 수가 2이하
  if c == 1:
    print(stair[0])
  else:
    print(stair[0]+stair[1])
