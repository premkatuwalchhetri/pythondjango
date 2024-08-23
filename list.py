# first_list = [5,1,1,9,23,54]
# temp = 5
# short_list = []
# for number in first_list:
#   if number > temp:
#     short_list.append(number)
#     temp = number
#   else:
#     short_list.insert(len(short_list)-1,number)
# print(short_list)    
      
      
      
      
first_list = [1, 5, 9, 6, 89, 1203, 23]

temp = 0

sorted_list = []

for number in first_list:
    if number > temp:
        sorted_list.append(number)
        temp = number
    else:
        for i in range(len(sorted_list)):
            if number < sorted_list[i]:
                sorted_list.insert(i, number)
                

print(sorted_list)