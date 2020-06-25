class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

def display(head):
    if head is None:
        return

    cur = head
    while cur:
        print(cur.data)
        cur = cur.next

def reverse(node):

    if node is None:
        return None

    if node.next is None:
        return node

    #import pdb; pdb.set_trace()

    last_node = node.next
    node.next = None
    head = reverse(last_node)
    last_node.next = node
    return head


ll = LinkedList()

cur = Node(0)
#cur.data = 1

ll.head = cur

for i in range(1, 3):
    node = Node(i)
    #node.data = i
    cur.next = node
    cur = cur.next

display(ll.head)

#nh = reverse(ll.head)

display(reverse(ll.head))



