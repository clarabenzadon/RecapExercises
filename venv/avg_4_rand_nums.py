import random

num1 = int(input("Input First number "))
num2 = int(input("Input Second number "))

numbers = []
for i in range(4):
  numbers.append(random.uniform(num1, num2))

print(numbers)
print(sum(numbers)/len(numbers))