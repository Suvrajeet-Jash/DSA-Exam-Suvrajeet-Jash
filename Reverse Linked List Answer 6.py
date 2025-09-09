class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_linked_list(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next  # Save the next node
        curr.next = prev       # Reverse the link
        prev = curr            # Move prev to current
        curr = next_node       # Move to the next node

    return prev  # New head of the reversed list

def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

print("Original List:")
print_list(head)

head = reverse_linked_list(head)

print("Reversed List:")
print_list(head)
