'''
number:
    int
    float
    bool
    complex
'''

import random

float_number = 3.98

print(int(float_number))

int_number_1 = 2

int_number_2 = 4

list = [int_number_1, int_number_2]

print(max(list))

print(pow(int_number_1, int_number_2))


print(random.sample(range(20),10))

print(random.choice(range(10)))
