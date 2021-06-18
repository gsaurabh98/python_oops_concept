my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = map(lambda x: x**2,my_list)

print new_list


terms = int(input("How many terms? "))

# use anonymous function
result = list(map(lambda x: 2 ** x, range(terms)))
print result
