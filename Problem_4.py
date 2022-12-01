def sol():
  n = 10000000
  for i in range(1,n):
    
    for j in range(1,21):
      if i % j != 0:
        break
      if j == 20:
        return i
      
if __nam__ == "__main__":
  sol()
