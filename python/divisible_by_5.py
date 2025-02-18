def check_divisibility(num):
  if(num%5==0 ):
    return("TRUE")
  else:
    return("FALSE")
num = int(input("Enter a number: "))
print(check_divisibility(num))


