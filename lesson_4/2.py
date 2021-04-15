from random import randint

random_numbers = [randint(1, 300) for i in range(13)]
numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_numbers = [numbers[i]
               for i in range(1, len(numbers)) if numbers[i] > numbers[i - 1]]

new_random_numbers = [random_numbers[i]
                      for i in range(1, len(random_numbers)) if random_numbers[i] > random_numbers[i - 1]]

print(new_numbers)
print(new_random_numbers)
