import random
while True:
 try:
    n = int(input("level: "))
    if n > 0:
     break
 except ValueError:
    continue
generate = random.randint(1,n)
while True:
 try:
   guess = int(input("guess: "))
   if guess <= 0:
      continue
   elif generate < guess:
      print("less")
   elif generate> guess:
      print("high")
   else:
      print("just right ")
      break
 except ValueError:
        continue

