import sys

def get_groups(array):
	groups = []
	# represent each group as an array of answers
	answer = [] 
	for line in array:
		if line == '\r\n':
			if len(answer) > 0:
				groups.append(answer)
			answer = []
		else:
			answer.append(line.strip())
	return groups

def score_group(array):
	countset = set()
	alph = 'qwertyuiopasdfghjklzxcvbnm'
	for char in alph:
		countset.add(char)
	# assume all answers yes and intersect sets
	for person in array:
		newset = set()
		for ch in person:
			newset.add(ch)
		countset = countset.intersection(newset)
	return len(countset)


#main
lines = []
for line in sys.stdin:
	lines.append(line)
# print(get_groups(lines))
groups = get_groups(lines)
score = 0
for group in groups:
	# print(score_group(group))
	score += score_group(group)

print(score)

