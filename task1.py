from functools import reduce

floats = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers = [22, 33, 10, 6894, 11, 2, 1]

print(floats) # initial
floats = list(map(lambda x: round(x**3, 3), floats))
print(floats) # processed
print('')

print(names) # initial
names = list(filter(lambda x: len(x) >= 5, names))
print(names) # processed
print('')

print(numbers) # initial
reduce_numbers = reduce(lambda num1, num2: num1*num2, numbers)
print(reduce_numbers) # result of reduce()