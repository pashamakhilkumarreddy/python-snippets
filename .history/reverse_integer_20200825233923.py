def reverse_integer(number: int) -> int:
  string = str(number)
  if string[0] == '-':
    return int('-' + string[:0:-1]
return int(string[:0:-1])
  
print(reverse_integer(143))