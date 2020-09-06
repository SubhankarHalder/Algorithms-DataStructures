class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, newdata):
        self.head = Node(data=newdata, next=self.head)

    def append(self, newdata):
        if not self.head:
            self.head = Node(data=newdata)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data=newdata)

    def find(self, key):
        found = False
        curr = self.head
        while curr:
            if curr.data == key:
                found = True
                return found
            curr = curr.next
        return found

    def remove(self, key):
        curr = self.head
        prev = None
        if curr.data == key:
            self.head = None
            return
        while curr:
            if curr.data == key:
                break
            prev = curr
            curr = curr.next
        prev.next = curr.next

    def reverse(self):
        curr = self.head
        prev = None
        next_nd = None
        while curr:
            next_nd = curr.next
            print(f"temp data 1: {next_nd.data}")
            curr.next = prev
            print(f"next_nd data 2: {next_nd.data}")
            prev = curr
            print(f"next_nd data 3: {next_nd.data}")
            curr = next_nd
            print(f"next_nd data 4: {next_nd.data}")
        self.head = prev
    
    def get_list(self):
        data = []
        curr = self.head
        while curr:
            data.append(curr.data)
            curr = curr.next
        return data


if __name__ == "__main__":
    lst = SinglyLinkedList()
    print(lst.get_list())
    lst.prepend(23)
    lst.prepend('a')
    lst.prepend(42)
    lst.prepend('X')
    lst.append('the')
    lst.append('end')
    print(lst.get_list())
    print(lst.get_list())
    lst.reverse()
    print(lst.get_list())
