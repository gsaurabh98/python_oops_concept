my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = reduce(lambda x,y: x+y ,my_list)
print new_list


new = reduce(lambda x,y: y if x>y else x, my_list)
print new

new1 = reduce(lambda x,y : x*y ,my_list)

print new1


a = 3
b = 4

a = (a+b) - a
b = (a-b) + a
a = (a+b) - a

print a, b