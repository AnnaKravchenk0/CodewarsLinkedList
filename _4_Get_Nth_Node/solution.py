'''
Docstring for _4_Get_Nth_Node.solution
'''
# from preloaded import Node



class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    '''
    Docstring for get_nth
    '''
    counter = 0
    while node:
        if counter == index:
            return node
        counter += 1
        node = node.next
    raise Exception




# getNth(1 -> 2 -> 3 -> null, 0).data === 1
# getNth(1 -> 2 -> 3 -> null, 1).data === 2
# linked_list = Node(1, Node(2, Node(3, None)))
# print(get_nth(linked_list, 0))
