quitBool = False


def fizzbuzz(num1, num2=1):
    x = 3  # fizz
    y = 5  # buzz
    if num2 > num1:
        num1, num2 = num2, num1

    output = ''
    for i in range(num2, num1 + 1):
        if (i % x == 0) and (i % y == 0):
            output += 'FizzBuzz'
        elif i % x == 0:
            output += 'Fizz'
        elif i % y == 0:
            output += 'Buzz'
        else:
            output += str(i)
        print(output)
        output = ''


welcome = '''
Welcome to my game of FizzBuzz!
Please select an option
P - Play
Q - Quit
'''
while not quitBool:
    print(welcome)
    i = input("").lower()
    if i == "q" or i == "p":
        if i == "q":
            quitBool = True
        if i == "p":
            inp = input("What number do you want to use to play? \n>>")
            try:
                int(inp)
            except ValueError:
                try:
                    float(inp)
                except ValueError:
                    print("Your input was incorrect, try again")
            fizzbuzz(int(inp))
    else:
        print("I don't understand that, try again")
else:
    print("Thank you for playing!")
