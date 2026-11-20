inter= (input("expression:"))
x,y,z = inter.split(" ")
x=int(x)
z=int(z)
if y=="+":
    print(float(x+z))
if y=="-":
    print(float(x-z))
if y=="*":
    print(float(x*z))
if y=="/":
    print(float(x/z))


