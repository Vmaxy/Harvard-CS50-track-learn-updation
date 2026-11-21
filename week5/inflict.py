import inflect
p= inflect.engine()
lst = []
while True:
    try:
     name = input("Name")
     lst.append(name)
    except EOFError:
        print ("")
        break
for i in lst:
    my = p.join((lst),final_sep=",")
print(f"Adieu, adieu, to {my}")
