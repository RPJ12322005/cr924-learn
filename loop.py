def loopTest():
    print("Does this work?")
    numbers=[13,23,17,98]
    index=0
    while(index<len(numbers)):
        number=numbers[index]
        print("Number is " + str(number) + " at index " + str(index))
        index+=1
    print("-----------")
    for number in numbers:
        print("Number is " + str(number) + " at index " + str(index))
      