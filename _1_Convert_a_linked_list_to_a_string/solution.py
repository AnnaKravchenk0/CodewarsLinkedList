'''
Docstring for _1_Convert_a_linked_list_to_a_string.solution
'''
# class Node():
#     '''
#     Docstring for Node
#     '''
#     def __init__(self, data, next = None):
#         self.data = data
#         self.next = next

def stringify(node):
    '''
    Docstring for stringify
    '''
    lst = ''
    while node:
        lst += f'{node.data} -> '
        node = node.next

    lst += f'{node}'

    return lst




# Node(1, Node(2, Node(3)))
# "1 -> 2 -> 3 -> None"
