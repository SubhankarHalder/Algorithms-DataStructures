class ListNode:
    """
    A node in a singly linked list
    """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)

class SinglyLinkedList:
    def __init__(self):
        """
        Creates a new singly linked list
        Takes O(1) time
        """
        self.head = None

    def __repr__(self):
        """
        Returns a string representation of the list
        Takes O(n) time
        """
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next

        return '[' + ', ' .join(nodes) + ']'

    def prepend(self, newdata):
        """
        Insert a new element at the beginning of the list
        Takes O(1) time
        """
        self.head = ListNode(data=newdata, next=self.head)

    def append(self, newdata):
        """
        Insert a new element at the end of the list
        Takes O(1) time
        """
        if not self.head:
            self.head = ListNode(data=newdata)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(data=newdata)

    def find(self, key):
        """
        Search for the first element with 'data' matching 'key'.
        Return the element or 'None' if not found.
        Takes O(n) time
        """
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        return curr

    def remove(self, key):
        """
        Remove the first occurence of 'key' in the list.
        Takes O(n) time
        """
        curr = self.head
        previous = None
        while curr and curr.data != key:
            previous = curr
            curr = curr.next
        if not previous:
            self.head = curr.next
        else:
            previous.next = curr.next

    def reverse(self):
        """
        Reverse the list in place
        Takes O(n) time
        """
        curr = self.head
        temp = None
        final = None
        while curr:
            temp = curr.next
            curr.next = final
            final = curr
            curr = temp
        self.head = final


if __name__ == "__main__":
    lst = SinglyLinkedList()
    print(lst)
    lst.prepend(23)
    lst.prepend('a')
    lst.prepend(42)
    lst.prepend('X')
    lst.append('the')
    lst.append('end')
    print(lst)
    print(lst.find('X'))
    print(lst.find('y'))
    lst.reverse()
    print(lst)
    lst.remove(42)
    print(lst)

