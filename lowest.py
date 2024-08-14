data = "5678493"

lowest_number = 0

for number in data:
  number = int(number)
  
  if number < lowest_number:
    lowest_number = number
    
  else:
    pass
  
print(lowest_number)  