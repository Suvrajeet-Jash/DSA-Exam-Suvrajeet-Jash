class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,data):
        new_node = Node(data)

        if self.head == None: #When the list is empty
            self.head = new_node
            self.tail = new_node

        else: #When the list is not empty
            self.tail.next = new_node
            self.tail = new_node

    def printLinkedList(self):
        current = self.head
        while current:
            print(current.data, end = "\n")
            current = current.next
        print("None")

l1 = LL()
l1.append(10)
l1.append(20)
l1.append(30)
l1.append(40)
l1.append(50)

print("My Linked List: ")
l1.printLinkedList()

            
            
