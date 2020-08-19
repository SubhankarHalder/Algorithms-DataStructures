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
    
    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        counter = 0
        current = self.head
        while current != None:
            counter += 1
            current = current.get_next()
        return counter

    def search(self, item):
        current = self.head
        while current != None:
            if current.get_data() == item:
                return True
            current = current.get_next()
        return False

    def remove(self, item):
        previous = None
        current = self.head
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
    
    def get_list(self):
        current = self.head
        list_a = []
        while current != None:
            list_a.append(current.get_data())
            current = current.get_next()
        return list_a

    def append(self, item):
        new = Node(item)
        current = self.head
        previous = None
        while current != None:
            previous = current
            current = current.get_next()

        previous.set_next(new)


if __name__ == "__main__":
    my_list = UnorderedList()
    my_list.add(31)
    my_list.add(71)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)
    print("List: ", my_list.get_list())
    print("List Size: ", my_list.size())
    print("Is 3 in List? ", my_list.search(3))
    my_list.remove(31)
    print("After removal of 31 from list: ", my_list.get_list())
    print("List Size:", my_list.size())
    my_list.append(22)
    print("List after appending 22: ", my_list.get_list())
    print("Lust Size: ", my_list.size())
        
        


        