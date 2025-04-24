from tempfile import tempdir

from fontTools.varLib.models import nonNone


class Node:
    def  __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class doubly:
    def __init__(self):
        self.head=None

    def append(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
            self.head.prev=None
            self.head.next=None
        else:
            last=self.head
            while(last.next is not None):
                last=last.next
            last.next=newnode
            newnode.prev=last
    def display(self):
        current=self.head
        if self.head==Node:
            print("list is empty")
            return
        print("node of double linked list:")
        while current!=None:
            print(current.data)
            current=current.next
    def delete_node(self,key):
        temp=self.head
        if temp is not None:
            if temp.data==key:
                self.head=temp.next
                temp=None
                return
            while temp is not Node:
                if temp.data is key:
                    break
                prev=temp
                temp=temp.next
            if temp==None:
                return
            prev.next=temp.next
            temp=None
d=doubly()
d.append(1)
d.append(2)
d.append(3)
d.append(4)
d.append(5)
d.append(6)
d.display()
d.delete_node(2)
print("after removing elements")
d.display()

