# def countword(arr,word):
#   counter = 0

#   for i in range(0,len(arr)):
#     if(arr[i]==word):
#       counter+= 1

#   return counter


# arr = ["The", "dog", "jumped", "in", "the", "dog", "house"]
# word = "$%"
# print(countword(arr, word))
def printList(head):
  print("PRINTING FINAL LIST:")
  current = head
  while(current):
    print(current.val)
    current = current.next
    
class Node(object):
    def __init__(self, v):
        self.val = v
        self.next = None
        self.prev = None

node1 = Node(0)
node2 = Node(1)
node3 = Node(2)
node4 = Node(3)
node5 = Node(4)
node1.prev = None
node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3
node4.next = node5
node5.prev = node4
node5.next = None

# class Node(self, value):
#   self.next = None
#   self.prev = None
#   self.val = value

def reverseLinkedList(LinkedList):

  head = LinkedList
  
  while head:
    temp = head.next
    head.next = head.prev
    head.prev = temp
    head = node5
  
  printList(head)

reverseLinkedList(node1)

#
# Given a node, return the length of the linked list
#
# Input: 1 ; Return: 1
# Input: 1->2->3 ; Return 3
#
'''
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getLength(node):
    length = 0
    while node != None:
        length += 1
        node = node.next

    return length


class Tests:
    if __name__ == "__main__":
        n0 = ListNode(0)
        print(f"Test 1 - getLength returned: {getLength(n0)}, expected: 1")

        n1 = ListNode(val=1)
        n2 = ListNode(val=2)
        n3 = ListNode(val=3)
        n1.next = n2
        n2.next = n3
        print(f"Test 2 - getLength returned: {getLength(n1)}, expected: 3")
'''

'''
#
# Given a sorted linked list, delete all duplicates such that each element appear only once.
# Input : 1 ; Output : 1
# Input : 1->1 ; Output: 1
# Input : 1->1->1->2->2 ; Output: 1->2
#
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def equals(self, n):
        # self is None, n is valid
        if not self and n:
            return False
        if self.val != n.val:
            return False

        if self.next == None:
            if n.next != None:
                return False
            else:
                return True

        return ListNode.equals(self.next, n.next)


def removeDuplicates(head):
    if head == None or head.next == None:
        return head
    curNode = head

# 1 > 1 > 2 > 2
# 1 == 1 -> 1 > 2 > 2
# 
#    if curNode.val == curNode.next.val:
#        curNode.next = curNode.next.next
#    else:
#        curNode = curNode.next

    while curNode.next:
      if curNode.val == curNode.next.val:
        print(curNode.val)
        print(curNode.next.val)
        curNode.next = curNode.next.next
      else:
        print(curNode.val)
        print(curNode.next.val)
        curNode = curNode.next

    return head


class Tests:
    if __name__ == "__main__":
        n1_1 = ListNode(1)
        print("Test cases 1 passed: " + str(removeDuplicates(n1_1).equals(n1_1)))

        n2_1a = ListNode(1)
        n2_1b = ListNode(1)
        n2_1a.next = n2_1b

        n2_answer = ListNode(1)
        print("Test case 2 passed: " + str(removeDuplicates(n2_1a).equals(n2_answer)))

        n3_1a = ListNode(1)
        n3_1b = ListNode(1)
        n3_2a = ListNode(2)
        n3_2b = ListNode(2)
        n3_1a.next = n3_1b
        n3_1b.next = n3_2a
        n3_2a.next = n3_2b

        n3_answer1 = ListNode(1)
        n3_answer2 = ListNode(2)
        n3_answer1.next = n3_answer2

        print("Test case 3 passed: " + str(removeDuplicates(n3_1a).equals(n3_answer1)))
'''

#
# Given a singly linked list, determine if it is a palindrome.
#
# Example 1:
# Input: 1->2
# Output: false
#
# Example 2:
# Input: 1->2->2->1
# Output: true


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(node):
    fullLength = getLength(node)

    firstHalf = []
    currentNode = 0
    while currentNode < (fullLength / 2):
        firstHalf.append(node.val)
        node = node.next
        currentNode += 1

    node = node.next

    while currentNode > 0:
        if node.val != firstHalf[currentNode]:
            return False
        node = node.next
        currentNode -= 1

    if currentNode != 0:
        return False

    return True


def getLength(node):
    length = 0
    while node != None:
        length += 1

        if node.next == None:
            return length
        node = node.next
    return length


class Tests:
    if __name__ == "__main__":
        # 1
        n1_1 = ListNode(val=1)
        print(f"Test 1 - isPalindrome returned: {isPalindrome(n1_1)}, expected: True")

        # 1 -> 2
        n2_1 = ListNode(val=1)
        n2_2 = ListNode(val=2)
        n2_1.next = n2_2
        print(f"Test 2 - isPalindrome returned: {isPalindrome(n2_1)}, expected: False")

        # 1 -> 2 -> 3
        n3_1 = ListNode(1)
        n3_2 = ListNode(2)
        n3_3 = ListNode(3)
        n3_1.next = n3_2
        n3_2.next = n3_3
        print(f"Test 3 - isPalindrome returned: {isPalindrome(n3_1)}, expected: False")

        # 1 -> 2 -> 1
        n4_1 = ListNode(1)
        n4_2 = ListNode(2)
        n4_3 = ListNode(1)
        n4_1.next = n4_2
        n4_2.next = n4_3
        print(f"Test 4 - isPalindrome returned: {isPalindrome(n4_1)}, expected: True")