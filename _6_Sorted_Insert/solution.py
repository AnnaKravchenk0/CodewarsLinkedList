""" For your information:
"""
class Node(object):
    '''
    Docstring for Node
    '''
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    '''
    Docstring for sorted_insert
    '''
    node = Node(data)
    if head.data >= data:
        node.next = head
        return node

    probe = head

    while probe.next is not None and probe.next.data < data:
        probe = probe.next

    node.next = probe.next
    probe.next = node

    return head




# sortedInsert(1 -> 2 -> 3 -> null, 4) === 1 -> 2 -> 3 -> 4 -> null)
# sortedInsert(1 -> 7 -> 8 -> null, 5) === 1 -> 5 -> 7 -> 8 -> null)
# sortedInsert(3 -> 5 -> 9 -> null, 7) === 3 -> 5 -> 7 -> 9 -> null)
