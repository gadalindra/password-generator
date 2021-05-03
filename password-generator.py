from random import choice
import string

while True:
    try:
        lenght = int(input('Lenght of your password: '))
        if lenght > 0:
            break
        else:
            print("No valid integer! Please try again ...")
            continue
    except ValueError:
        print("No valid integer! Please try again ...")

def passwordGenerator(lenght: int) -> int:
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.printable
    password = ""
    
    for s in range(lenght):
        password += choice(characters)
    print(f"Your password is: {password}")

passwordGenerator(lenght)
