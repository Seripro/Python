def add_numbers(a, b):
    return a + b

add_var = add_numbers

def call_function(fun, a, b):
    return fun(a, b)

print(add_var(10,20))
print(call_function(add_numbers, 10, 30))