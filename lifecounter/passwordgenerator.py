import random


def generate_password():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    pw_length = 5
    pw = ""

    for i in range(pw_length):
        next_index = random.randrange(len(alphabet))
        pw += alphabet[next_index]

    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(pw)//2)
        pw = pw[0:replace_index] + str(random.randrange(10)) + pw[replace_index+1:]

    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(pw)//2, len(pw))
        pw = pw[0:replace_index] + pw[replace_index].upper() + pw[replace_index+1:]

    return pw

