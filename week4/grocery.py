go = {}
while True:
 try:
    item = input().upper()
    if item in go:
        go[item] += 1
    else:
       go[item] = 1


 except EOFError:
    for k,v in sorted(go.items()):
       print(k,v)
    break
 