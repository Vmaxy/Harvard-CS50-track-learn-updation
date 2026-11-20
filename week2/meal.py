def main():
    data = convert(input('what time it is? '))
    if 7 <= data <= 8:
        print("breakfast time")
    elif 12<= data <= 13:
        print("lunch time")
    elif 18<= data <=19 :
        print('dinner time')
    



def convert(time):
    hours, minutes = time.split(":")
    return float(hours)+(float(minutes)/60)


if __name__ == "__main__":
    main()