#assignment 3.3
#Tristan Werden
#Todo: None

try :
    score = float(input("input score: "))
except :
    print("that is not a number please use numeric input")
    quit()

if (score > 1) or  (score < 0) :
    print("that is not a valid number please use 0-1")
    quit()
elif score >= .9 :
    print("A")
elif score >= .8 :
    print("B")
elif score >= .7 :
    print("C")
elif score >= .6 :
    print("D")
else :
    print("F")
