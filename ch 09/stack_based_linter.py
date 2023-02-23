class Stack():
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def read(self):
        return [] if  len(self.data) == 0 else self.data[-1]


class Linter():

    def __init__(self):
        self.stack = Stack()

    def lint(self, text):

        for tx in text:
            if self.__is_opening_brace(tx):
                self.stack.push(tx)
            elif self.__is_closing_brace(tx):
                popped_opening_brace = None if not self.stack.read() else self.stack.pop()

                if not popped_opening_brace:
                    return f"{tx} doesn't have opening brace"

                if self.__is_not_a_match(popped_opening_brace, tx):
                    return f"{tx} has mismatched opening brace"
            else:
                continue

        if self.stack.read():
            return "{self.stack.read()} does not have closing brace"

        return True

    def __is_opening_brace(self, ch):
        return ch in ['{', '[', '(']

    def __is_closing_brace(self, ch):
        return ch in ['}', ']', ')']

    def __is_not_a_match(self, opening_brace, closing_brace):
        return closing_brace != {"[": "]", "{": "}", "(": ")"}[opening_brace]


if __name__ == "__main__":
    linter = Linter()
    linter2 = Linter()

    print(linter.lint("( var x = { y: [1, 2, 3] } )"))
    print(linter2.lint(" var x = { y: [1, 2, 3] } )"))
