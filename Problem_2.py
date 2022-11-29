def sol():
  sum = 0
  
  dp = [0 for i in range(1,4000001)]
  dp = [1,1]
  
  for i in range(2,4000001):
    
    dp[i] = dp[i-1] + dp[i-2]
    if dp[i] % 2 == 0:
      sum += dp[i]
      
  return sum 

if __name__ == "__main__":
  sol()
    
    
