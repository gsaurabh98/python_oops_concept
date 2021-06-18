#The filter() function in Python takes in a function and a list as arguments.

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = filter(lambda x: x%2==0, my_list)

print new_list


x = [1,2,3,4]

y = filter(lambda x: x%2 ==0 ,x)

print y

