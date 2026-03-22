'''
Docstring for _2_Parse_a_linked_list_from_a-string.solution
'''
class Node():
    '''
    Docstring for Node
    '''
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def linked_list_from_string(list_repr: str) -> Node | None:
    """ 1 -> 2 -> 3 -> None
    """

    list_repr = list_repr.split(' -> ')[:-1]


    head = Node(0)
    probe = head

    for el in list_repr:
        probe.next = Node(int(el))

        probe = probe.next

    return head.next



# Node(1, Node(2, Node(3)))

# print(linked_list_from_string('1 -> 2 -> 3 -> None'))
