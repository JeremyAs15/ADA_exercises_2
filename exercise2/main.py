
# Authors: Daniel Bolivar and Jeremy Astaiza
# Solution of problem: "Is This a Binary Search Tree?" HackerRank https://www.hackerrank.com/challenges/is-binary-search-tree/problem

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def check_binary_search_tree_(root):
    prev = [None]

    def inorder(node):
        if node is None:
            return True
        if not inorder(node.left):
            return False
        if prev[0] is not None and prev[0] >= node.data:
            return False
        prev[0] = node.data
        if not inorder(node.right):
            return False
        return True

    return inorder(root)

# ------------------------ Test 1----------------------------

root1 = Node(3)
root1.left = Node(5)
root1.right = Node(2)
root1.left.left = Node(1)
root1.left.right = Node(4)
root1.right.right = Node(6)

test1 = check_binary_search_tree_(root1)
print("Test 1")
print("Result:", "Yes" if test1 else "No")
print()

# ------------------------ Test 2----------------------------

root2 = Node(4)
root2.left = Node(2)
root2.right = Node(6)
root2.left.left = Node(1)
root2.left.right = Node(3)
root2.right.left = Node(5)
root2.right.right = Node(7)

test2 = check_binary_search_tree_(root2)
print("Test 2")
print("Result:", "Yes" if test2 else "No")


