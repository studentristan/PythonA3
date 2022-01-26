#assignment 3.1
#Tristan Werden
#Todo: None

hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

total = hours * rate

if hours > 40 :
    overtime = hours - 40
    overtimePay = overtime * (rate * .5)
    total = total + overtimePay

print(total)
