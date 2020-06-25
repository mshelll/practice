
count = 0

def knode(root, start, k):
    if root is None:
        return 0

    if root.left == start:
        return 1
    
    if root.right == start:
        return 1

    left  = knode(root.left, start, k-1)
    right = knode(root.right, start, k-1)

    count += left or right
    return count





#distance of root node from start node  ==  x    left 

# All nodes at distance k-x from root node on the right
# All descendant nodes at distance k from start
# 
 

def find_nodes(root, d, nodes):
    if root is None:
        return nodes

    if d == 0:
        nodes.append(root)

    find_nodes(root.left, d-1, nodes)
    find_nodes(root.right, d-1, nodes)


def knodes(root, cur, start, d, nodes):
    if root is None or start is None or cur is None:
        return

    if cur == start and d == 0:
        nodes.append(root)

    knodes(root, root.left, d-1, nodes)
    knodes(root, root.right, d-1, nodes)

    knodes(root.left, root.left, d, nodes)
    knodes(root.right, root.right, d, nodes)


def knodes(root, cur, start, d, nodes):
    if root is None or start is None or cur is None:
        return

    if cur == start and d == 0:
        nodes.append(root)

    knodes(root, root.left, d-1, nodes)
    knodes(root, root.right, d-1, nodes)

    knodes(root.left, root.left, d, nodes)
    knodes(root.right, root.right, d, nodes)



def find_distance(root, start, dist):
    if root is None:
        return -1

    if root == start:
        return dist

    left = find_distance(root.left, start, dist+1)
    right  = find_distance(root.right, start, dist+1)                 

    return left or right


def kthnodes(root, start, k):
    if root is None:
        return []

    left = find_distance(root.left, start, 1)
    right = find_distance(root.right, start, 1)

    nodes = []
    if left:
        if left-k:
            find_nodes
        if k-left:
            find_nodes(root.right, k-left, nodes)

    elif right and k-right:
        find_nodes(root.left, k-left, nodes)

    return nodes


def 









    





def main():

    if node is None:
        return 0


    knode(node.left)
    knode(node.right)

