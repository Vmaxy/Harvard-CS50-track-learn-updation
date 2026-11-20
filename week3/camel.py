s = input('CamelCase: ')
print("snakecase: ",end="")
for c in s:
    if c.islower():
      print(c,end="")
    elif c.isupper():
        print("_",end="")
        print(c.lower(),end="")
print()
