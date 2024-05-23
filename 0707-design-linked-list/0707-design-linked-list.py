class Node:
    def __init__(self,prev=None,next=None,val=None):
        self.prev=prev
        self.next = next
        self.val=val

class MyLinkedList:
    def __init__(self):
        self.head=Node(None,None,-1)
        self.tail=Node(None,None,-1)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.nodecounts=0
        

    def get(self, index: int) -> int:
        if index<0 or index>=self.nodecounts:
            return -1
        i=0
        curr=self.head.next
        while curr and i<index:
            i+=1
            curr=curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        newnode = Node(self.head,self.head.next,val)
        self.head.next.prev=newnode
        self.head.next=newnode
        self.nodecounts+=1
        

    def addAtTail(self, val: int) -> None:
        newnode=Node(self.tail.prev,self.tail,val)
        self.tail.prev.next=newnode
        self.tail.prev=newnode
        self.nodecounts+=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index<0 or index>self.nodecounts:
            return None
        i=0
        curr=self.head.next
        while i<index and curr:
            i+=1
            curr=curr.next
        newnode=Node(curr.prev,curr,val)
        curr.prev.next=newnode
        curr.prev=newnode
        self.nodecounts+=1
        

    def deleteAtIndex(self, index: int) -> None:
        if index<0 or index>=self.nodecounts:
            return None
        i=0
        curr=self.head.next
        while i<index and curr:
            i+=1
            curr=curr.next
        curr.prev.next=curr.next
        curr.next.prev=curr.prev
        self.nodecounts-=1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)