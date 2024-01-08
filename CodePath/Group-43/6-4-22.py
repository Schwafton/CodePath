"""
def pal(s):
  new_string = ""
  lower_string = s.lower()
  for char in lower_string:
    if char.isalnum():
      new_string += char

  reversedString = new_string[::-1]
  print(reversedString)
  return new_string == reversedString

print(pal("race a car"))
print(pal("A man, a plan, a canal: Panama"))
print(pal("235"))
print(pal(" "))
print(pal("(*@&$@)*#"))
"""
def recursive_pal(new_string, start, end):
  if start >= end or start == end:
    return
  else:
    if new_string[start] != new_string[end]:
      return False
    return True
    recursive_pal(new_string, start+1, end-1)
    
def pal(s):
  new_string = ""
  lower_string = s.lower()
  for char in lower_string:
    if char.isalnum():
      new_string += char

  start = 0
  end = len(new_string)-1

  print(recursive_pal(new_string, start, end)

print pal("A man, a plan, a canal: Panama")
print pal("race a car")