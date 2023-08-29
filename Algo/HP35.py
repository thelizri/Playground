def evaluate_rpn(input):
    stack = []
    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
    }

    for char in input.split():
        if char.isnumeric():
            stack.append(int(char))
        else:
            second, first = stack.pop(), stack.pop()
            result = operations[char](first, second)
            stack.append(result)

    return stack.pop()


input_str = "3 4 + 2 4 + *"
result = evaluate_rpn(input_str)
print(result)
