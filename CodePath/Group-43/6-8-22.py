
# def frequency(array):
#   dict = {}
#   frequency = 0

#   for i in range(len(array)):
#     for j in range(len(array)):
#       if array[i] == array[j]:
#         frequency += 1
    
#     # if array[i] already exists in dict, then skip
#     if frequency in dict:
#       dict[frequency] = dict[frequency].append(array[i])  # values would be in an array

#     else:
#       dict[frequency] = [array[i]]
#     frequency = 0

#   # for eachElement in dict:
#   #   dict.get()
#   #   frequency = 0
#   print("dict: ")
#   print(dict)

# frequency([1,23,43,23,5])

# def freqK(arr,k):
#     d = dict()
    
#     for i in arr:
#         if i not in d:
#             d[i] = 1
#         else:
#             d[i] += 1
#     
#     for key,value in d.items():
#         if value == k:
#             return key

# print(freqK([1,23,43,23,5],3))


def freq(array,k):
  # function only works for the FIRST element that has the specified frequency.
  dict = {}
  #keys = elements, values = frequency
  for eachElement in array:
  # if element is present in dictionary, increment the frequency
    if eachElement in dict:
      dict[eachElement] += 1 #{1:2} 1 = key, 2 = value. one is added to the value if the value is already in the dict
    else:
      dict[eachElement] = 1 #{1:1} ---> if there is a new value that isn't in the array it is added as {1:1} , 1 =key: 1=value
      
  for key,value in dict.items():
    if value == k:
      return key

  print(dict)
  #if element is not present in dictionary, add it to the dictionary
  #convert values to list, determine the index of the value we're searching for, use that index to locate the key in the dictionary, and return that key

print(freq([1, 5, 23,43,23, 6, 5, 5, 5, 23, 23,3], 4)) # you are getting 5 because 5 also appears 4 times. 5 and 23 both appear 4 times.
# print(freq([1,3,5,3,3,2],3))