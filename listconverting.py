def max_digit(number: int) -> int:
  
  #hier entsteht ne liste aus dem integer, der gemappt wird mit int,string)
    ist = list(map(int,str(number)))
    return max(ist)

#this will give the highest single digit in the given number


print(max_digit(59))


