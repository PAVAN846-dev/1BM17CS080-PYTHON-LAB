import string,random

def generatePassword(num):
    password = ''
    str1 = string.printable
    print(str1)

    for n in range(num):
        x = random.randint(0,94)
        password += string.printable[x]

    return password
print(generatePassword(100))
        
