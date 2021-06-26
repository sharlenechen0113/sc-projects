"""
File: largest_digit.py
Name: Sharlene Chen
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: the number to be processed and compared with
	:return: the largest digit in the number
	"""
	num = abs(n)
	initial_largest_digit = num % 10	# set largest digit to the last digit of the number
	return helper(num, initial_largest_digit)


def helper(num,largest_digit):
	"""
	This is a helper function that helps find the largest digit with extra variables to assist
	calculation. The calculation loops through the number by dividing it by 10 repeatedly to
	separate out each digit, then compares recursively to find the largest digit.
	:param num: the number to be checked
	:param largest_digit: the current largest digit
	:return: the most recent largest digit
	"""
	if num == 0:
		return largest_digit
	else:
		last_digit = int(num % 10) #compare from the last digit
		num = int((num - last_digit) / 10)
		if last_digit >= largest_digit:
			return helper(num,last_digit)
		else:
			return helper(num,largest_digit)

if __name__ == '__main__':
	main()
