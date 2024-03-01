num = input('Enter a number (decimal only): ')
# type your code here
temp = num.lstrip("0123456789").lstrip('.')
dp = len(temp)

# do not change any code beyond this point
print('The number', num, 'has', dp, 'decimal places.')
