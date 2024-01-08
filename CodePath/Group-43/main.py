
'''
stack = []
for num in nums:
  if num < 0:
    stack.append(num)

if stack:
  insert_index = 0
  for i in range(len(nums)):
    if stack[0]*-1< nums[i]:
      insert_index = i

  for i in stack:
    nums.insert(insert_index, stack.pop())
    insert_index += 1


Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Input: [3, 5, 1, 4, 9, 2]    
           3      p = 5, q = 2
          / \
         5   1
        / \   \
       4   9   2

Output: 3
'''



'''
class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root, string):

    if root:
        string += str(root.val)
        string += " "

    if root.left:
        string += str(root.left.val)
        string += " "

        serialize(root.left, string)

    if root.right:
        string += str(root.right.val)
        string += " "
        serialize(root.right, string)
      
    print(string)
    return string
    # string += str(serialize(root.left).val) + str(serialize(root.right).val) + str(root.val)


def deserialize(string):
  stringArray = string.split(" ")
  print(stringArray)

  # root, left, right
  root = TreeNode(stringArray[0])
  
  
  return stringArray

root = TreeNode(5, TreeNode(1), TreeNode(10))
root2 = TreeNode(5, TreeNode(1), TreeNode(7))
root3 = TreeNode(5, TreeNode(2), TreeNode(7))

string = ""
serializedString = serialize(root, string)
deserialize(serializedString)


# print(serialize(root2))
# print(serialize(root3))

# def validateBST(root):

#   if root.left:
#     if root.left.val > root.val:
#       return False
#     validateBST(root.left)
#   if root.right:
#     if root.right.val < root.val:
#       return False
#     validateBST(root.right)
#   return True

# print("in code")
# def insertNode():
# node = TreeNode(val, None, None)

# if not root:
#   print("no tree")
#   root = node
#   return root

# inserted = False
# curr = root

# while inserted == False:
#     if node.val > curr.val:
#         if curr.right:
#             curr = curr.right
#         else:
#             curr.right = node
#             inserted = True
#     if node.val < curr.val:
#         if curr.left:
#             curr = curr.left
#         else:
#             curr.left = node
#             inserted = True

#   return root

# class TreeNode:
#   def __init__(self, val=None, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right

# # def printLeafNodes(root: TreeNode):
# #   if root.left == None and root.right == None:
# #     print(root.val)

# #   if root.left:
# #     print("root.left")
# #     printLeafNodes(root.left)
# #   if root.right:
# #     print("root.right")
# #     printLeafNodes(root.right)

# # #    1
# # #   / \
# # #  3   4

# # # TreeNode(val=3)

# root = TreeNode(val=1, left=TreeNode(val=3), right=TreeNode(val=4))
# root2 = TreeNode(val=2, left=TreeNode(val=4, left=TreeNode(val=8), right=TreeNode(val=5)), right=TreeNode(val=7))
# # printLeafNodes(root)
'''