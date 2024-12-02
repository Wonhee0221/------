import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
  num = int(input())
  dp = [[]] * 41 
  dp[0] = [1,0]
  dp[1] = [0,1]
  dp[2] = [1,1]
  
  for i in range(3,num+1):
    dp[i] = [dp[i-1][0] + dp[i-2][0], dp[i-1][1]+dp[i-2][1]]
  print(dp[num][0], dp[num][1])

