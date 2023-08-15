import random

passlen = int(input('Enter the length of the password :'))
s = "abcdefghijklmnopqrstuvwxys0123456789ABCDEFGHIJKLMNPOQRSTUVWXYZ!@#$%^&*()?"
P = "".join(random.sample(s, passlen ))
print(P)