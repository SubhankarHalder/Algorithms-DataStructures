class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, newdata):
        self.data = newdata

    def set_next(self, newnext):
        self.next = newnext

    
class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, data):
        temp = Node(data)
        temp.set_next(self.head)
        self.head = temp

    def search(self, item):
        current = self.head
        while current != None:
            if current.get_data() == item:
                return True
            current = current.get_next()
        return False

    def size(self, item):
        current = self.head
        counter = 0
        while current != None:
            counter += 1
            current = current.get_next()
        return counter

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        
        if previous == None:
            self.head = current.get_next()

        else:
            previous.set_next(current.get_next())


if __name__ == "__main__":
    my_list = UnorderedList()
    my_list.add(31)
    my_list.add(71)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)
