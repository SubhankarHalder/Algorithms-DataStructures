class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get_list(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(curr.data)
            curr = curr.next
        return nodes

    def append(self, newdata):
        if not self.head:
            self.head = Node(data=newdata)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(data=newdata)
    
    def append_tail(self, newdata):
        new_node = Node(data=newdata)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            prev = self.tail
            self.tail = new_node
            prev.next = self.tail
    
    def size(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count

    def search(self, key):
        curr = self.head
        found = False
        while curr:
            if curr.data == key:
                found = True
                return found
            curr = curr.next
        return found


if __name__ == "__main__":
    lst = SinglyLinkedList()
    print(lst.get_list())
    print(lst.size())
    lst.append_tail(23)
    lst.append_tail('a')
    lst.append_tail(42)
    lst.append_tail('X')
    lst.append_tail('the')
    lst.append_tail('end')
    print(lst.get_list())
    print(lst.size())
    print("Search X: ", lst.search('the'))
    print("Search Z: ", lst.search('Z'))




        