'''
Docstring for _10_Alternating Split.solution
'''
class Node(object):
    '''
    Docstring for Node
    '''
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    '''
    Docstring for Context
    '''
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    '''
    Docstring for alternating_split
    '''
    if not head or not head.next:
        raise Exception

    first = head
    second = head.next


    first_ = first
    second_ = second

    while first_ and second_:
        first_.next = second_.next
        first_ = first_.next

        second_.next = first_.next
        second_ = second_.next

    if first_:
        first_.next = None
    if second_:
        second_.next = None

    return Context(first, second)



# list = 1 -> 2 -> 3 -> 4 -> 5 -> None
# alternating_split(list).first == 1 -> 3 -> 5 -> None
# alternating_split(list).second == 2 -> 4 -> None
