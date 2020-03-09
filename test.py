#This is a test file

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

#Linked list class with a single head data        
class LinkedList:
    def __init__(self):
        self.head = None 

    #insertion method for linked List
    def insert(self, data):
        newNode = Node(data)
        if (self.head):
            current = self.head 
            while(current.next):
                current = current.next
            current.next = newNode 
        else:
            self.head = newNode
            
    #Print Lists
    def printLL(self):
        current = self.head
        while(current):
           print(current.data)
           current = current.next 

LL = LinkedList()
LL.insert(4)
LL.insert(5)
LL.insert(6)
LL.insert(7)

LL.printLL()