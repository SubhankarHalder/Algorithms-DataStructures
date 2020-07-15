"""
This script implements Ordered List
"""

class Node:
    def __init__(self, new_data):
        self.data =  new_data
        self.reference = None

    def get_data(self):
        return self.data

    def get_reference(self):
        return self.reference

    def set_data(self, new_data):
        self.data = new_data

    def set_reference(self, new_reference):
        self.reference = new_reference


class UnorderedList:
    def __init__(self):
        self.head = None

    def add(self, new_element):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.get_data() > new_element:
                stop = True
            else:
                previous = current
                current = current.get_reference()
        temp = Node(new_element)
        if previous == None:
            temp.set_reference(self.head)
            self.head = temp
        else:
            temp.set_reference(current)
            previous.set_reference(temp)

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.get_data() == item:
                found = True
            elif current.get_data() > item:
                stop = True
            else:
                current = current.get_reference()

        return found
