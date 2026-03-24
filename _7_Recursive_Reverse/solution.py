'''
Docstring for _7_Recursive_Reverse.solution
'''
class Node(object):
    '''
    Docstring for Node
    '''
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    ''' Recursive Reverse() '''
    if head is None or head.next is None:
        return head

    new = reverse(head.next)
    head.next.next = head
    head.next = None

    return new



# list = "2 -> 1 -> 3 -> 6 -> 5 -> None"
# reverse(list) === "5 -> 6 -> 3 -> 1 -> 2 -> None"
