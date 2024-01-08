def reverse_string(input_string):
  firstPtr = 0
  lastPtr = len(input_string) - 1
  list = []

  for char in input_string:
    list.append(char)

  while (firstPtr < lastPtr) or (firstPtr == lastPtr):
    dummy = list[firstPtr]
    list[firstPtr] = list[lastPtr]
    list[lastPtr] = dummy
    firstPtr += 1
    lastPtr -=1
  # ty
  # create the list into a string, i forgot how
  newString = "" 
  for x in list:
      newString += x
  return newString

print(reverse_string('hi'))

