#Number 1
print("This is Number 1.")
def grade_calculation(score):
    if score < 0 or score > 100:
        return ("Error, please enter numeric input between 0 and 100.")
    elif score >= 90:
        return ("A")
    elif score >= 80:
        return ("B")
    elif score >= 70:
        return ("C")
    elif score >= 60:
        return ("D")
    elif score >= 50:
        return ("E")
    else:
        return ("F")

try:
    score = float(input("Enter the score: "))
    result = grade_calculation(score)
    if result.startswith("Error, please enter numeric input between 0 and 100."):
        print(result)
    else:
        print("Grade:",result)
except ValueError: 
    print("Error, please enter numeric input between 0 and 100.")

print("\n")
print("This is Number 2.")
#Number 2
def computepay(hours,rate):
    try:
        hours = int(hours)
        rate = float(rate)
        if hours > 40:
            Overtime = hours - 40
            hours = 40
            pay = (hours * rate) + (Overtime * (1.5 * rate))
            return pay
        else:
            pay = hours * rate
            return pay
    except ValueError:
        return ("Error, please enter numeric input")

try:
    hours = input("Enter the hours: ")
    rate = input("Enter the rate:  ")
    salary = computepay(hours,rate)
    if type(salary) == str:
        print(salary)
    else:
        print("this is the salary:",salary)
except KeyboardInterrupt:
    print("Error, please enter numeric input")

print("\n")
print("This is Number 3.")
#Number 3
def num_divide3(num):
    count = 0
    for i in range(1, num + 1):
        if i % 3 == 0:
            count += 1   
    return count

while True:
    user = input("Enter a positive integer: ")
    if user.lower() == "done":
        print("Bye !!")
        break
    try:
        num = int(user)
        if num <= 0:
            print("Please enter a positive number.")
        else:
            numba = num_divide3(num)
            print("numbers divisible by 3 among numbers from 1 to",user,":",numba)
    except ValueError:
        print("Please enter a positive number.")

print("\n")
print("End of program.")
print("Rackhel, 202312229.")


