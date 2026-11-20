months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ").strip()

    try:
        month, day, year = date.split('/')

        if 1<=int(day)<=31 and 1<=int(month)<=12:
            print(f"{year}-{int(month):02}-{int(day):02}")
            break
    except ValueError:
        pass

    try:
        month, day, year = date.split(' ')
        if not day.endswith(','):
            raise ValueError

        month = months.index(month) + 1
        day = int(day.removesuffix(','))
        year = int(year)
        if 1<=int(day)<=31 and 1<=int(month)<=12:
            print(f"{year}-{int(month):02}-{int(day):02}")
            break
    except ValueError:
        pass

    continue
