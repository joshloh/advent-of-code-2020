import sys

def calculate(array):
	l = len(array)
	for x in range(l):
		for y in range(l):
			# just in case the number 1010 is there :P
			if ((x != y) and (array[x]+array[y]==2020)):
				return array[x]*array[y]

numbers = []
for line in sys.stdin:
	numbers.append(int(line))
print(calculate(numbers))

