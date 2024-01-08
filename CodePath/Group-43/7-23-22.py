def quickSort(arr, start, end):

    if (start >= end):
        return
    partitionIndex = partition(arr, start, end)

    quickSort(arr, start, partitionIndex - 1)

    quickSort(arr, partitionIndex+1, end)

    return arr


def partition(arr, start, end):
    # pivot = 15
    # 
    pivot = arr[end]
    partitionIndex = start

    for i in range(start, end-1):
        if (arr[i] <= pivot):
            temp = arr[partitionIndex]
            arr[partitionIndex] = arr[i]
            arr[i] = temp
            partitionIndex += 1

    arr[partitionIndex], arr[end] = arr[end], arr[partitionIndex]
    print(arr)
    return partitionIndex

arr = [7, 10, 4, 3, 20, 15]
# print(arr)
# print(partition(arr, 0, len(arr)-1))


def kth(arr, k):
    arr = quickSort(arr, 0, len(arr) - 1)
    # print("here")
    # print(arr)
    return arr[k-1]


input = [7, 10, 4, 3, 20, 15]

print(kth(input, 1))





'''
# 7-20-22
def floodFill(matrix, sr, sc, newColor):
  #matrix = [[1,1,1],[1,1,0],[1,01]]
  list = [[sr, sc]]
  for i in list:
    bfs(matrix, list, sr, sc)
'''
'''
def bfs(matrix, list, sr, sc):
  compare = matrix[sr][sc]

  if sr == 0 or sc == 0:
  
  if matrix[sr-1][sc] == compare and matrix[sr-1][sc] not in list:
    list.append[sr-1, sc]
    
  if matrix[sr+1][sc] == compare and matrix[sr+1][sc] not in list:
    list.append[sr+1, sc]

  if matrix[sr][sc-1] == compare and matrix[sr][sc - 1] not in list:
    list.append[sr, sc-1]
    
  if matrix[sr][sc+1] == compare and matrix[sr][sc +1] not in list:
    list.append[sr, sc+1]  
'''
'''
def convertstrtoint(value):
  result = 0
  num = 1
  for i in range(len(value)):
    if value[i] == "-":
      num = -1
    else:
      result = (result*10) + (ord(value[i]) - ord("0"))

  print(result*num)

convertstrtoint("1234")





#457%10 = 7
#457//10 = 45

def convertintostr(value):
  # result = 0
  # num = 1
  rem = 0
  string = ""
  sign = False
  
  if value < 0:
    value = abs(value)
    sign = True
  if value == 0:
    return "0"
  while value:
    rem = value%10
    value = value//10
    rem = str(rem)
    string = rem + string
  if sign:
    string = "-" + string

  return(string)
  



print(convertintostr(500))
print(convertintostr(-500))
print(convertintostr(0))
print(convertintostr(-0))
print(convertintostr(-6714))
'''
