def sol():
  n = 100
  def ind_square(n=100):
    
    return n*(n+1)*(2*n+1)/6
  
  def square(n=100):
    sum = 0
    for i in range(1,101):
      
      sum += i
      
    return sum**2
  
  x = ind_square(100)
  y = square(100)
  
  print(x-y)
  
  
if __name__ == "__main__":
  sol()
 
      
