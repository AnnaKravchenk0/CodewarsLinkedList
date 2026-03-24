'''
Docstring for _11_Can you get the loop.solution
'''
def loop_size(node):
    '''
    Docstring for loop_size
    '''
    first = node
    second = node
    c = 0
    while node:
        first = first.next
        second = second.next.next
        if first == second:
            second = second.next
            c = 1
            while second != first:
                second = second.next
                c += 1
            return c
    return c
