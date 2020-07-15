"""
This is a script for basic stack in Python
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


if __name__ == "__main__":
    s = Stack()
    print(s.is_empty())
    s.push(4)
    s.push('dog')
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.is_empty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())