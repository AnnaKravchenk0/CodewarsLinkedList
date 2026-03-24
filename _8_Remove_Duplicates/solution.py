'''
Docstring for _8_Remove_Duplicates.solution
'''
class Node(object):
    '''
    Docstring for Node
    '''
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    '''
    Docstring for remove_duplicates
    '''
    if not head:
        return head

    probe = head

    while probe.next:
        if probe.data == probe.next.data:
            probe.next = probe.next.next


        else:
            probe = probe.next

    return head

# var list = 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5 -> null
# removeDuplicates(list) === 1 -> 2 -> 3 -> 4 -> 5 -> null
