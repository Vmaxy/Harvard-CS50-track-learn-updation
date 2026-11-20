def remove(text):
    vowels =["a","e","i","o","u","A","E","I","O","U"]
    for i in vowels:
        text = text.replace(i,"")    
        
    return text

def main():
    print("Output : ",remove(input("Input : ")))

main()