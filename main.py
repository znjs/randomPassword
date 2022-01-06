#imports
import string
import random

#length of password
length = int(input('Enter the length of the password'))

#defining the password parameters
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

#Combining all parameters to generate a passoword
all = lower + upper + num + symbols

password = "".join(random.sample(all, length))

print(password)