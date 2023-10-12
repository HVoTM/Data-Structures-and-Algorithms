import random

def generate_random_list(length, min_value, max_value):
    random_list = [random.randint(min_value, max_value) for _ in range(length)]
    return random_list

# Example usage:
length = 10  # Change the length of the list as needed
min_value = 1  # Change the minimum value as needed
max_value = 100  # Change the maximum value as needed

random_list = generate_random_list(length, min_value, max_value)
print(random_list)
