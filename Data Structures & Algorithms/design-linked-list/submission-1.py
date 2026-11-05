class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        cur = self.head.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and cur != self.tail and index == 0:
            return cur.val
        return -1

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        next = self.head.next
        prev = self.head
        prev.next = newNode
        next.prev = newNode
        newNode.next = next
        newNode.prev = prev

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        next = self.tail
        prev = self.tail.prev
        prev.next = newNode
        next.prev = newNode
        newNode.next = next
        newNode.prev = prev

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.head.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and index == 0:
            newNode = ListNode(val)
            next, prev = cur, cur.prev
            prev.next = newNode
            next.prev = newNode
            newNode.next, newNode.prev = next, prev

    def deleteAtIndex(self, index: int) -> None:
        cur = self.head.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and cur != self.tail and index == 0:
            next = cur.next
            prev = cur.prev
            prev.next = next
            next.prev = prev


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)