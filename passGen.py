import string
import random
while 1:
    print("*********PASSWORD GENERATOR*********")
    print("Enter The desired length of the password: ")
    length=int(input())
    ran=''.join(random.choices(string.ascii_letters, k= length))
    print("The Randomly generated string is " + str(ran))