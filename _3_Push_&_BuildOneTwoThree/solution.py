'''
Node is defined in preloaded like this:


'''
# from preloaded import Node
class Node:
    '''
    Docstring for Node
    '''
    def __init__(self, data):
        self.data = data
        self.next = None


def push(head, data):
    '''
    Docstring for push
    '''
    new = Node(data)
    new.next = head
    return new

def build_one_two_three():
    '''
    Docstring for build_one_two_three
    '''
    chained = None

    chained = push(chained, 3)
    chained = push(chained, 2)
    chained = push(chained, 1)

    return chained
