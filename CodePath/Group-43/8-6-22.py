class TreeNode:
  def __init__(self, val=None, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

# def printLeafNodes(root: TreeNode):
#   if root.left == None and root.right == None:
#     print(root.val)

#   if root.left:
#     print("root.left")
#     printLeafNodes(root.left)
#   if root.right:
#     print("root.right")
#     printLeafNodes(root.right)

# #    1
# #   / \
# #  3   4

# # TreeNode(val=3)

root = TreeNode(val=1, left=TreeNode(val=3), right=TreeNode(val=4))
root2 = TreeNode(val=2, left=TreeNode(val=4, left=TreeNode(val=8), right=TreeNode(val=5)), right=TreeNode(val=7))
# printLeafNodes(root)
# printLeafNodes(root2)

#    1
#   / \
#  2   3
#   \
#    5
root2 = TreeNode(val=1, left=TreeNode(val=2, right=TreeNode(val=5)), right=TreeNode(val=3))

# output: ["1->2->5", "1->3"]

def treePaths(root: TreeNode):
  paths=[]
  getPaths(paths, root)
  return paths

def getPaths(paths, root):
  if not root:
    return

  
    
  #leaves
  if root.left == None and root.right == None:
    paths.append(root.val) 
    paths.append(" ")

  else:
    paths.append(root.val) #all nodes but leaves
  
  getPaths(paths, root.left)
  getPaths(paths, root.right)


print(treePaths(root2))