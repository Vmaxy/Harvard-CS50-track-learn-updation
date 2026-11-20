def money (greeting):
    if greeting.startswith("hello"):
       return "$0"
    elif greeting.startswith("h"):
        return "$20"
    else:    
       return "$100"

def main():
    print(money(input("Greeting: ").lower()))

main()