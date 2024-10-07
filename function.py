greeting = 'Hello'
to = 'World'

# Welcome greeting function
def greet(message, name="World"):
    result = f"{message}, {name}"
    print(result)

greet(greeting, to)
