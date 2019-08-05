# A toy script

print("Please enter two numbers to add.\nFirst Number:")

n = raw_input()

print("Second Number:")

m = raw_input()

# convert user string input to float
answer = float(n) + float(m)

print("The sum of {} and {} is {}".format(n, m, answer))
