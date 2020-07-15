"""
This is a script to check whether parenthesis are balanced using stacks
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


def par_check(parenthesis):
    """
    Function that checks whether parenthesis are balanced. Returns boolean
    """
    model = Stack()
    for bracket in parenthesis:
        if bracket == "(":
            model.push(bracket)
        else:
            model.pop()
    if model.is_empty():
        return True
    else:
        return False

    
if __name__ == "__main__":
    print(par_check('((()))'))
    print(par_check('(()'))
