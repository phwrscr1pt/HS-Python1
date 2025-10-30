# Create a list from 1-100
# Remove the odd number that is divisible by 3
# final_list -> [1, 2, 4, 5, 7, 8, 10, 11, 12, ...]
# count many numbers left

numbers = []
for value in range(1,101):
    numbers += [value]
print(numbers)

# numbers = list(range(1, 101))
# print(numbers)

for number in numbers:
    if number % 2 != 0 and number % 3 == 0:
        numbers.remove(number)
print(numbers)

print("The number of numbers in the remaining list is", len(numbers))
