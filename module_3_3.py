# 1
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])

# 2
values_list = [3.6, 'список', False]
values_dict = {'a' : 'словарь', 'b' : True, 'c' : 9}

print_params(*values_list)
print_params(**values_dict)

# 3
values_list_2 = ['список2', 5.2]

print_params(*values_list_2, 42)