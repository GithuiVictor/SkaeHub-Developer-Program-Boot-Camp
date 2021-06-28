#initializing list 
group_list = [(2, 3), (4, 7), (8, 11), (3, 6)]
# using lamda to find min() and max()
return_max = max(group_list,key=lambda item:item[1])[1]
return_min = min(group_list,key=lambda item:item[1])[1]
# printing original list
print("Original list with tuples:")
print((group_list))
print("the max and minum",return_max,return_min)