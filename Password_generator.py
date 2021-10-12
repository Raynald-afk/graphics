from random import sample
"""
This program generates random passwords for the user
using the random module
"""
letters = "abcdefghijklmnopqrstuvwxyz"
symbols = "!@#$%^&*())~><?:"
numbers = 123456789
all = letters+symbols+str(numbers)
print("Your New Password:","".join(sample(all,10)))