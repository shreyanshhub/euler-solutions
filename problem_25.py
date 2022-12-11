def sol():
  count = 2
  a,b = 1,1
  while len(str(b)) != 1000:
    a,b = b,a+b
    count += 1
  return count
