from stack_based_linter import Stack

def string_reversal(string):
    output = ""
    stack = Stack()
    
    for ch in string:
        stack.push(ch)

    while stack.read():
        output += stack.pop()

    return output


print(string_reversal("abcde"))