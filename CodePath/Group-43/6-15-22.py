# Problem #1: Remove Duplicates from Sorted List                        
def removeDupes(head):
  while head.next != None:
    if head.value == head.next.value:
      head.next = head.next.next

  return head
      

def linkedlistCycle(head):
  count = 0
  while head.next != None:
    count += 1
    if (count > 1000):
      return False
    else:
      return True

def linkedListCrossed(head):
  pointer1 = head
  pointer2 = head.next

  while (pointer2 != null) or (pointer2.next != null):
    if (pointer1 == pointer2): 
      return True
    else:
      pointer1 = pointer1.next                                       
      pointer2 = pointer2.next.next
  return False

def merge(list1, list2):
  data1 = list1.data
  data2 = list2.data

  while list1.head.next != None:
    