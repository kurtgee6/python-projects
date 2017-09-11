#ask the user for a number
#tell whether their number is prime or not

print('')
print('Check to see if a number is prime')
ask = int(input("Give me a number > "))
numbers = list(range(2, 11))

for i in numbers:
    if ask % i == 0:
        print('')
        print("Congrats {} was a prime number".format(ask))
        print('')
    else:
        print('Sorry that was not a prime number')
