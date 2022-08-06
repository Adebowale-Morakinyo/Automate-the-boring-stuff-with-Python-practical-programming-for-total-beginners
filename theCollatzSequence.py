#collatz function plus Input Validation
def collatz(number):
    if number % 2 == 0:
        return (number // 2)
    else:
        return (3 * number + 1)

#program that lets the user type in an integer and that keeps calling collatz()
#on that number until the function returns the value 1
print('Enter number:')
try:
    user_input = int(input())
except ValueError:
    print('Must enter an integer!')

while True:
    output = collatz(user_input)
    print(output)

    user_input = output
    if output == 1:
        break
