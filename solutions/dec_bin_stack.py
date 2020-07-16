"""
This scipt finds the binary equivalent of a decimal number
"""


class Stack:
    """
    Stack Class
    """
    def __init__(self):
        """
        Constructor Class
        """
        self.new_stack = []

    def is_empty(self):
        """
        Check if stack is empty
        """
        return self.new_stack == []

    def push(self, item):
        """
        Push an item onto a stack
        """
        self.new_stack.append(item)

    def pop(self):
        """
        Pop a stack
        """
        return self.new_stack.pop()

    def peek(self):
        """
        Return the top most item in a stack
        """
        return self.new_stack[-1]

    def size(self):
        """
        Returns the size of the stack
        """
        return len(self.new_stack)


def matches(open, close):
    """
    Helper function for par_check
    """
    open_parenthesis = "({["
    close_parenthesis = ")}]"
    return open_parenthesis.index(open) == close_parenthesis.index(close)


def divide_by_2(number):
    """
    This function finds the binary equivalent of a decimal number
    """
    sample = Stack()
    while (number >= 2):
        remainder = number % 2
        sample.push(str(remainder))
        number = number // 2

    new_array = []
    while not sample.is_empty():
        new_array.append(sample.pop())

    return int("".join(new_array))


if __name__ == "__main__":
    print(divide_by_2(42))
    
