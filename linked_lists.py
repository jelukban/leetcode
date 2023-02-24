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

    return prev


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


# 21. Merge Two Sorted Lists
def mergedTwoListsRecursive_two(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1
    if list1.val < list2.val:
        return ListNode(list1.val, mergedTwoListsRecursive_two(list1.next, list2))
    return ListNode(list2.val, mergedTwoListsRecursive_two(list1, list2.next))
