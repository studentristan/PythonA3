#assignment 3.2
#Tristan Werden
#Todo: None

try :
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
except :
    print("Error, please enter numeric input")
    quit()

total = hours * rate

if hours > 40 :
    overtime = hours - 40
    overtimePay = overtime * (rate * .5)
    total = total + overtimePay

print(total)
