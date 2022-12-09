def sol():
  
  n = 100001
  import math
  
  maxi = int(2*n*math.log(n))
  prime = [True]*maxi
  count = 0
  
  for i in range(2,maxi):
    
    if prime[i]:
      count += 1
      if count == n:
        return i
      for j in range(2*i,maxi,i):
        prime[i] = False
        
if __name__ == "__main__":
  sol()
      
