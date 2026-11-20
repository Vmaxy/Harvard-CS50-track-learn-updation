while True:
    try:
       x,y = input("fraction: ").split("/")
       x = int(x)
       y = int(y) 
       percent  = round(x / y *100)
       if y >= x:
          if x >=0:
            break
    
    except ValueError:
     continue
    except ZeroDivisionError:
     continue
if percent <= 1:
    print("E")

elif percent >= 99:
    print("F")

else:
    print(f"{percent}%")
