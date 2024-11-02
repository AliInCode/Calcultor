
while True:
    number_1= float(input("please enter number 1 :"))
    number_2= float(input("please enter number 2 :"))
    number_3= float(input("please enter number 3 :"))
    number_4= float(input("please enter number 4 :"))
    character= str(input("please enter character :"))
    print("--------------------------------------------------------")
    if character == "+":
        print(number_1 + number_2 + number_3 + number_4)
    elif character == "-":
        print(number_1 - number_2 - number_3 - number_4)
    elif character == "*":
        print(number_1 * number_2 * number_3 * number_4)
    elif character == "/":
        print(number_1 / number_2 / number_3 / number_4)
    elif character == "%":
        print(number_1 % number_2 % number_3 % number_4)
    elif character == "**":
        print(number_1 ** number_2 ** number_3 ** number_4)
    exit =  str(input("Do you Want continue? :")).lower()
    if exit =="y":
        continue
        print("--------------------------------------------------------")
    elif exit == "n":
        break