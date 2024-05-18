camel = input("camelCase: ")

# Using list comprehension to build the snake_case string
snake_case = ''.join(['_' + i if i.isupper() else i for i in camel])

print("snakeCase:", snake_case)
