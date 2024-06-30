#Друге завдання

import random

def get_numbers_ticket(min, max, quantity):
    if not (1 <= min <= max <= 1000 and 1 <= quantity <= (max - min + 1)):
        return []

    unique_numbers = set()

    while len(unique_numbers) < quantity:
        unique_numbers.add(random.randint(min, max))

    sorted_numbers = sorted(unique_numbers)

    return sorted_numbers
print(get_numbers_ticket(1, 49, 6))