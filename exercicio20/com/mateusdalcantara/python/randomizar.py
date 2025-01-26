import random
import favorite_number

#https://docs.python.org/3/library/random.html

random_integer = random.randint(1, 10)#only integer numbers 1 to 10
print("- Your ramdom number between 1 to 10 is [{}]"
      .format(random_integer))

print("- My favorite number is [{}]"
      .format(favorite_number.the_huge_number))

print("- Creating floating random numbers: [{}]"
      .format(random.random() * 10)) #0 to 9

random_float = random.uniform(1, 10) #1 to 10
print(random_float)

print()
print("==========")
print()

random_heads_or_tails = random.randint(0, 1)
if random_heads_or_tails == 0:
    print("Side of the coin is [{}]".format("Heads"))
else:
    print("Side of the coin is [{}]".format("Tails"))