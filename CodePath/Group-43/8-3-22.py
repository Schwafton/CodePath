
# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#     def insertNode(self, node, value):
#         # Check our node
#         if node.val < value:
#             node.right = self.insertNode(node.right, value)
#         else:
#             node.left = self.insertNode(node.left, value)
#         return node


'''
    def same_tree(self, p, q):

        if p is None and q is None:
            return True
        #what if p is none and q is not none
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return self.same_tree(p.left, q.left) and self.same_tree(
            p.right, q.right)

    # Input: p = [1,2,3], q = [1,2,3]
'''

# self.same_tree(p.left, q.left)
#q = Node(1, 2, 2)
#same_tree(p, q)

# p = Node(1, 2, 4)
# insertNode(p, Node(3)
