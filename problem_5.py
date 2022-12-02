def sol():
  
  n = 600851475143
  d = 2
  factors = []
 
  while n > 1:
    
    while n % d == 0:
      factors.append(d)
      n /= d
      
    d += 1
    
  return factors

factors = sol()
print(max(factors))
      
