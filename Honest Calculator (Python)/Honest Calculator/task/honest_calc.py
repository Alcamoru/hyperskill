# write your code here
right_type = False
while not right_type:
    print("Enter an equation")
    number_one, op, number_two = input().split()
    try:
        number_one = float(number_one)
        number_two = float(number_two)
        if op not in "+-%/*" :
            print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
        else:
            right_type = True
    except:
        print("Do you even know what numbers are? Stay focused!")