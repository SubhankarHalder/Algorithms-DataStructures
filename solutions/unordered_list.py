"""
This code implements an unordered linked list
"""

class Node:
    """
    Implements Linked List Node
    """
    def __init__(self, initial_data):
        self.data = initial_data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, new_data):
        self.data = new_data

    def setNext(self, new_pos):
        self.next = new_pos

class UnorderedList:
    """
    Implements an Urordered List
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def add(self, add_data):
        temp = Node(add_data)
        temp.setNext(self.head)
        self.head = temp

        if self.size() == 1:
            self.tail = temp

    def catalog(self):
        current = self.head
        elements = []
        while current != None:
            elements.append(current.getData())
            current = current.getNext()
        return elements

    def size(self):
        current_node = self.head
        count = 0
        while current_node != None:
            count += 1
            current_node = current_node.getNext()

        return count

    def search(self, item):
        current_pos = self.head
        found = False
        while current_pos != None and not found:
            if item == current_pos.getData():
                found = True
            else:
                current_pos = current_pos.getNext()

        return found

    def remove(self, item):
        current_pos = self.head
        previous_pos = None
        found = False
        while not found:
            if current_pos.getData() == item:
                found = True
            else:
                previous_pos = current_pos
                current_pos = current_pos.getNext()
        if previous_pos == None:
            self.head = current_pos.getNext()
        elif current_pos.getData() == self.tail.getData():
            previous_pos.setNext(current_pos.getNext())
            self.tail = previous_pos
        else:
            previous_pos.setNext(current_pos.getNext())

    def append(self, item):
        temp = Node(item)
        self.tail.setNext(temp)
        self.tail = temp




        
if __name__ == "__main__":
    mylist = UnorderedList()
    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    mylist.add(93)
    mylist.add(26)
    mylist.add(54)
    data = mylist.catalog()
    list_size = mylist.size()
    list_search = mylist.search(93)
    print("Unordered List: ", data)
    print("Size of List: ", list_size)
    print("Found Item 31?: ", list_search)
    print("")
    print("Now removing 31")
    mylist.remove(31)
    print("")
    print(f"New List: {mylist.catalog()}")
    print("")
    print("Append 42")
    mylist.append(42)
    print(f"New List: {mylist.catalog()}")
    print("Now removing 42")
    mylist.remove(42)
    print("")
    print(f"New List: {mylist.catalog()}")
    print("")
    print("Append 99")
    mylist.append(99)
    print(f"New List: {mylist.catalog()}")
