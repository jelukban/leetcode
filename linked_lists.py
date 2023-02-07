# Reverse Linked List
def reverseList(head):
        current = head
        prev = None
        next_node = None

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return  prev