import sys

def calculate(array):
	l = len(array)
	for x in range(l):
		for y in range(l):
			for z in range(l):
				if ((x != y and x != z) and (array[x]+array[y]+array[z]==2020)):
					print(array[x], array[y], array[z])
					return array[x]*array[y]*array[z]

numbers = []
for line in sys.stdin:
	numbers.append(int(line))
print(calculate(numbers))

