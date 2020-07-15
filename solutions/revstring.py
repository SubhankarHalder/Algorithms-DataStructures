"""
This script reverses a string using stack
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


def revstring(mystr):
    """
    This function uses a stack to reverse a string
    """
    model = Stack()
    for character in mystr:
        model.push(character)

    new_string = [model.pop() for index in range(model.size())]
    return "".join(new_string)


if __name__ == "__main__":
    sample_string = "abcdefghijklmnopqrstuvwxyz"
    print(revstring(sample_string))