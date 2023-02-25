from stack_based_linter import Stack


def string_reversal(string):
    output = ""
    stack = Stack()

    for ch in string:
        stack.push(ch)

    while stack.read():
        output += stack.pop()

    return output


def string_reversal_recursive(string):
    if len(string) == 1:
        return string[0]
    return string_reversal_recursive(string[1:]) + string[0]


print(string_reversal("abcde"))
print(string_reversal_recursive("abcde"))
