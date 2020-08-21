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


class OrderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        counter = 0
        current = self.head
        while current != None:
            counter += 1
            current = current.get_next()
        return counter

    def remove(self, item):
        current = self.head
        previous = None
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

    def search(self, item):
        current = self.head
        while current != None:
            if current.get_data() == item:
                return True
            elif current.get_data() > item:
                return False
            else:
                current = current.get_next()

        return False

    def get_list(self):
        current = self.head
        final_list = []
        while current != None:
            final_list.append(current.get_data())
            current = current.get_next()
        return final_list

    def add(self, item):
        temp = Node(item)
        current = self.head
        previous = None
        found = False
        while not found and current != None:
            if current.get_data() >= item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous == None:
            temp.set_next(current)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)
            

if __name__ == "__main__":
    my_list = OrderedList()
    my_list.add(31)
    print("List: ", my_list.get_list())
    my_list.add(71)
    print("List: ", my_list.get_list())
    my_list.add(17)
    print("List: ", my_list.get_list())
    my_list.add(93)
    print("List: ", my_list.get_list())
    my_list.add(26)
    print("List: ", my_list.get_list())
    my_list.add(54)
    print("List: ", my_list.get_list())
    print("List Size: ", my_list.size())



    