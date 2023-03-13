# 11. Here's a Python method to print the sum of the digits in a 3-digit number:
def sum_of_digits(num):
    if num < 100 or num > 999:
        print("Invalid input: number should be 3 digits")
    else:
        digit1 = num // 100
        digit2 = (num % 100) // 10
        digit3 = num % 10
        digit_sum = digit1 + digit2 + digit3
        print(f"The sum of the digits in {num} is {digit_sum}")

# 12. Here's a Python method that takes a number between 1 and 7 as input and uses a switch statement to print the corresponding weekday:
def print_weekday(num):
    switcher = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    weekday = switcher.get(num, "Invalid input: number should be between 1 and 7")
    print(weekday)

# 13. Here's a Python method to print "yes" if the units digit of a 2-digit number is equal to its tens digit:
def check_units_equals_tens(num):
    if num < 10 or num > 99:
        print("Invalid input: number should be 2 digits")
    elif num % 11 == 0:
        print("yes")
    else:
        print("no")

# 14. Here's a Python method to print "yes" if the units digit of a 3-digit number is equal to its hundreds digit:
def check_units_equals_hundreds(num):
    if num < 100 or num > 999:
        print("Invalid input: number should be 3 digits")
    elif num % 100 == num // 100:
        print("yes")
    else:
        print("no")

# 15. Here's a Python method to print "yes" if the units digit of a 4-digit number is equal to its tens digit:
def check_units_equals_tens(num):
    if num < 1000 or num > 9999:
        print("Invalid input: number should be 4 digits")
    elif num % 100 == num // 10 % 10:
        print("yes")
    else:
        print("no")

