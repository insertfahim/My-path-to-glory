class Node:
    def __init__(self,val):
        self.val=val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head=Node(-1)
        self.tail=Node(-1)
        self.head.next=self.tail
        self.nodecount = 0
        

    def get(self, index: int) -> int:
        if index<0 or index>=self.nodecount:
            return -1
        i=0
        curr=self.head.next
        while i<index and curr:
            i+=1
            curr=curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        newnode=Node(val)
        newnode.next=self.head.next
        self.head.next=newnode
        self.nodecount+=1
        

    def addAtTail(self, val: int) -> None:
        curr=self.head
        while curr and curr.next!=self.tail:
            curr=curr.next
        newnode=Node(val)
        newnode.next=curr.next
        curr.next=newnode
        self.nodecount+=1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index>self.nodecount:
            return None
        i=0
        curr=self.head
        while i<index and curr:
            i+=1
            curr=curr.next
        newnode=Node(val)
        newnode.next=curr.next
        curr.next=newnode
        self.nodecount+=1

    def deleteAtIndex(self, index: int) -> None:
        if index<0 or index>=self.nodecount:
            return None
        i=0
        curr=self.head
        while i<index and curr:
            i+=1
            curr=curr.next
            
        curr.next=curr.next.next
        self.nodecount-=1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)