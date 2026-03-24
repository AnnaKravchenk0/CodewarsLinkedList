'''
Docstring for _9_Swap Node Pairs In Linked List.solution
'''
class Node:
    '''
    Docstring for Node
    '''
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    '''
    Docstring for swap_pairsaa
    '''

    if not head or not head.next:
        return head

    first = head
    second  = first.next
    new = second

    flag = None


    while second:
        if flag:
            flag.next = second

        first.next = second.next
        second.next = first

        flag = first

        first = first.next
        if first and first.next:
            second = first.next
        else:
            second = None


    return new
