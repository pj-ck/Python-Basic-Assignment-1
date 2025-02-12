'''Q10. Tuple Item Update
You have to modify a tuple item without converting it into a list. Provide an example of any case where this exactly can happen. 
'''


my_tuple = (10, 20, [30, 40, 50], 60)
my_tuple[2][1] = 99  

print(my_tuple)
