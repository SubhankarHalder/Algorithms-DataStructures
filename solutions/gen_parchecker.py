"""
General Case of Parenthesis Checker
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


def par_check(parenthesis):
    """
    Function that checks whether parenthesis are balanced. Returns boolean
    """
    model = Stack()
    balanced = True
    index = 0
    while index < len(parenthesis) and balanced:
        bracket = parenthesis[index]
        if bracket in "({[":
            model.push(bracket)
        elif model.is_empty():
            balanced = False
        else:
            top = model.pop()
            if not matches(top, bracket):
                balanced = False
        index = index + 1

    if balanced and model.is_empty():
        return True
    else:
        return False


if __name__ == "__main__":
    print(par_check('{({([][])}())}'))
    print(par_check('[{()]'))
