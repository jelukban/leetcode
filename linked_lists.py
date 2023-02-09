# 206. Reverse Linked List
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


# 141. Linked List Cycle
def hasCycle(head):
    seen = set()
    current = head

    while current:
        if current.next in seen:
            return True
        else:
            seen.add(current)

        current = current.next

    return False