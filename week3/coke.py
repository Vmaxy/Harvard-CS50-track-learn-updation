balace = 50
while balace>0:
    print(f"Amount due: {balace}")
    coin= int(input("Insert coin: "))
    if coin in [5,10,25] :
        balace -=  coin
print(f"bsls{abs(balace)}")
