two_digit_number = input("Type a two digit númbers? \n") #Input numbers.

first_digit = two_digit_number[0] #checking index number.
second_digit = two_digit_number[1]

print(first_digit) #show the number of index
print(second_digit)
print(type(two_digit_number)) #show the type of variable

result = int(first_digit) + int(second_digit) #Casting both string variable to integer and does sum.

print(f"Your sum is: {result} ") #Output result.