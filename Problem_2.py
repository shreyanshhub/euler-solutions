def sol():
  
  sum = 0
  a,b = 0,1
  
  for i in range(1,4000001):
    
    if b % 2 == 0:
      sum += i
      
    a,b = b,a+b
    
  print(sum)

if __name__ = "__main__":
  sol()
    
    
