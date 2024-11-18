def validate_number(number):
    if number.isdigit() and len(number) == 10:
        digits = list(map(int, number))
    elif number.startswith("+") and " " in number:
        parts = number.split(" ", 1)
        country_code = parts[0][1:] 
        if country_code.isdigit() and 1 <= len(country_code) <= 2 and parts[1].isdigit() and len(parts[1]) == 10:
            digits = list(map(int, parts[1]))
        else:
            print("Incorrect")
            return
    else:
        print("Incorrect")
        return
    if sum(digits) > 0:
        print("Correct")
    else:
        print("Incorrect")
number = input().strip()
validate_number(number)
