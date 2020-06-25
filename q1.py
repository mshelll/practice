

def fib(n):

    if n == 0 or n == 1:
        return n

    return fib(n-1) + fib(n-2)


arr = [0, 1]
def fib(n):
    global arr
    for i in range(2, n):
        arr[i] = arr[i-1] + arr[i-2]

    return arr[n-1]

Graph :
id : int
lch :
rch :


def traverse(head):

    if head is None:
        return

    q = []
    q.append(head)

    visited = ()

    while(q):
        node = q.pop(0)
        print(node)

        left = node.lch
        if left and left not in visited:
            visted.add(left)
            q.append(left)

        right = node.rch
        if right and right not in visited:
            visted.add(right)
            q.append(right)



def traverse(head):

    if head is None:
        return

    q = []
    q.append(head)

    #visited = ()

    while(q):
        node = q.pop(0)
        print(node)

        left = node.lch
        if left: #and left not in visited:
            #visted.add(left)
            q.append(left)

        right = node.rch
        if right: # and right not in visited:
            #visted.add(right)
            q.append(right)


        #     q.append(node.lch)
        # if node.rch: q.append(node.rch)

        # for ns in head.adj(): 
        #     if ns not in visited:
        #         visited.add(ns)
        #         q.append(ns)






