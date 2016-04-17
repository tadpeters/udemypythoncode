# for i in range (17):
# 	print("{0:>2} in binary is {0:>08b}".format(i))

# for i in range (17):
# 	print("{0:>2} in binary is {0:>02x}".format(i))

# x = 20
# y = 0x20
# z = 0xa
# b = 0b101010

# print (b)
# print( x, y)
# print( z * y)

# When converting a decimal number to binary, you look for the highest power
# of 2 smaller than the number and put a 1 in that column. You then take the
# remainder and repeat the process with the next highest power - putting a 1
# if it goes into the remainder and a zero otherwise. Keep repeating until you
# have dealt with all powers down to 2 ** 0 (i.e., 1).
#
# Write a program that requests a number from the keyboard, then prints out
# its binary representation.
#
# Obviously you could use a format string, but that is not allowed for this
# challenge.
#
# The program should cater for numbers up to 65535; i.e. (2 ** 16) - 1
#
# Hint: you will need integer division (//), and modulo (%) to get the remainder.
# You will also need ** to raise one number to the power of another:
# For example, 2 ** 8 raises 2 to the power 8.
#
# As an optional extra, avoid printing leading zeros.
#
# Once the program is working, modify it to print Octal rather than binary.
"""
get a number from user. (number)

declare variables
xpont = 15
base = 2 or 8.
range is 15 to 0 by -1's
digitCatcher = []

test is a number > (base ^ xpont)
	yes
	subrtract (base ** xpont) from number
	add 1 to right side of string perhaps append a list. (digitCatcher)
	decrement xpont
no
	decrement xpont
	append 0 to list (digitCatcher)
	test again

if binary or hex display list result in quads 
if base = 8 display list result in octets

"""
# 5	2 1
# 1	1 0
#	1 0 1
# 5 = 101


