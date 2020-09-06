class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, newdata):
        if not self.head:
            self.head = Node(newdata)
            self.tail = Node(newdata)
        else:
            prev = self.tail
            self.head.next = Node(newdata)
            self.tail = Node(newdata)
            prev.next = self.tail

    def gen_list(self):
        curr = self.head
        get_list = []
        while curr:
            get_list.append(curr.data)
            curr = curr.next
        return get_list


if __name__ == "__main__":
    lst = SinglyLinkedList()
    print(lst.gen_list())
    lst.append(23)
    lst.append('a')
    lst.append(42)
    lst.append('X')
    lst.append('the')
    lst.append('end')
    print(lst.gen_list())
