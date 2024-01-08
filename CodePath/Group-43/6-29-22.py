def countword(arr,word):
  counter = 0

  for i in range(0,len(arr)):
    if(arr[i]==word):
      counter+= 1

  return counter


arr = ["The", "dog", "jumped", "in", "the", "dog", "house"]
word = "dog"
print(countword(arr, word))