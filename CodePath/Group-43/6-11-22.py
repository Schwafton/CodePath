def problem1(arr):
  '''
  arrLength = len(arr)
  if len(arr) % 2 == 0:
    majorityLength = arrLength/2  #even
  else:
    majorityLength = round(arrLength/2) #odd
    print("majorityLength:")
    print(majorityLength)
    print(" ")

  O(n) time
  O(n) space
  '''

  dict = {}

  for nums in arr:
    if nums not in dict:
      dict[nums] = 1
    else:
      dict[nums] += 1
      if dict[nums] >= round(len(arr)/2):
        return nums
  

arr1 = [3,2,3]
arr2 = [2, 2, 1, 1, 1, 2, 2]
arr3 = [4, 4, 4, 1]

#print(problem1(arr1))
#print(problem1(arr2))
#print(problem1(arr3))

#-----------------------------------------------------------
# O(n^2) time
#O(1) space
def majority(array):

    length = len(array)
    frequency = 0
    print(array)

    for i in range(length-1):
        for j in range(length-1):
            if array[j] == array [i]:
                frequency += 1
        if frequency > length/2:
            break
    return array[i]

# majority([2,3,3,3,2])

  
#-----------------------------------------------------------

'''
Input: s = "III"
Input: s = "LVIII"
Input: s = "MCMXCIV"
V = 5
X = 10
L = 50
D = 500
M = 5000
C = 100

dict = {'I':1,'V': 5, 'X': 10, 'L':50, 'D':500, 'M':5000, 'C':100}

O(n) time
O(1) space
'''

def romanNum (input):
  dict = {'I':1,'V': 5, 'X': 10, 'L':50, 'C':100,'D':500, 'M':1000 }
  
  previousLetterVal = 0
  sum = 0
  for eachLetter in input:
    currentLetterVal = dict[eachLetter]
    if (previousLetterVal < currentLetterVal):
      #subtract
      temp = currentLetterVal - previousLetterVal - previousLetterVal #deleting the previousLetterVal that I added in the last run of for loop
      sum += temp
    else:
        #add to total sum
      sum += currentLetterVal

      #reset previous letter to the current letter
    previousLetterVal = dict[eachLetter]


  return sum

print("Roman Numeral: ")
print(romanNum("III"))
print(romanNum("IV"))
print(romanNum("V")) 
print(romanNum("LVIII")) #58
print(romanNum('MCMXCIV')) #1994
