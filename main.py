num = int(input('Enter a number into the factorial finder: '))
def factorial(number):
  factorial = 1
  while number < 0:
    number = int(input('Factorials do not exist for negative numbers. \nEnter a positive number into the factorial finder: '))
  else:
    if number == 0:
      print('The factorial of 0 is 1')
    else:
      for x in range(1,number+1):
        factorial = factorial*x
      print(f'The factorial of {number} is {factorial}')
factorial(num)
