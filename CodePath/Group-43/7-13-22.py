# Input: [1, 2, 5, 3, 7, 10, 9, 12]
# Output: 5



def shortest_sorted(arr):
  left =  0 
  right = len (arr) - 1

  if len(arr) == 0:
    print("answer:")
    return 0
  else:
    # scan from left
    while (arr[left] <= arr[left + 1]) and (left+1 < len(arr)-1):
      left += 1
    # scan from right
    while (arr[right] >= arr[right - 1]) and (right-1 >= 0):
      right -= 1
  
    if right-left-1 <= 0:
      print("answer:")
      return 0
    else:
      # find min & max in part of array that needs to be sorted
      mini = min(arr[left:right+1])  
      maximum = max(arr[left:right+1])
      
      # compare min with left side of original arr
      if (left-1 >= 0) and (mini < arr[left-1]):
        left -= 1  
      if (right+1 < len(arr)) and (maximum > arr[right+1]): 
        right += 1
      print("answer:")

      return (right-left) + 1

array = [1, 3, 2, 0, -1, 7, 10]
print(shortest_sorted(array))
print("------------------------")

array2 = [1, 2, 5, 3, 7, 10, 9, 12]
print(shortest_sorted(array2))
print("------------------------")

array3 =  [3, 2, 1]
print(shortest_sorted(array3))
print("------------------------")

array4 = [1, 2, 3]
print(shortest_sorted(array4))
print("------------------------")

array5 = []
print(shortest_sorted(array5))
print("------------------------")

array6 = [1,2,3,2,1]
print(shortest_sorted(array6))
print("------------------------")

array7 = [1,2,2]
print(shortest_sorted(array7))
print("------------------------")


def rle(string):
  '''
  O(n) time -> O(n) space 
  Iterating through the original string and creating a new string result in
  O(n) time and O(n) space, i think.
  Corner cases include if we count lower and upper together (just add
  string.lower() if we do), empty string, maybe numbers too
  '''
  # Checking if len of str is 0, if it is, return empty string
  if len(string) == 0:
    return ''
  else:
    # Creating new string to store results
    newStr = ''
    # Variable to hold count of how many times a letter pops up
    count = 0
    # First letter in the string
    letter = string[0]
    # Iterating through the entire string
    for l in string:
      # Checking if the letter we've been onn, equals to the next letter
      if l == letter:
        # Increase count by 1 if it is :D
        count += 1
      else:
        # If not then we add the count letter first, then we add the count, (make count into an str, else you cant concatenate)
        newStr += letter
        newStr += str(count)
        # Setting new letter
        letter = l
        # Starting count from 1 here to include the letter we just assigned
        count = 1
    # At the very end we have to do it, just cause if we don't it passes over 
    # the last letter/count, so we add this
    newStr += letter
    newStr += str(count)
  return newStr

print(rle('wwwwaaadexxxxxx'))
print(rle('444422333666666'))
print(rle(''))
print(rle('AaAaAaAa')) # possible edge case, depending on interviewer, this case we're cap sensitive
assert(rle('aabaccccdexdx') == 'a2b1a1c4d1e1x1d1x1')