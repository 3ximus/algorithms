'''Find all possible permutations of a string

Time complexity  O(n*n!)
Space complexity O(1)
'''


def permutations(string):
	'''Finds all permutations of a given string'''
	p = set()
	if string == "":
		p.add("")
		return p
	new_set = permutations(string[1:])
	for word in new_set:
		for i in range(len(word) + 1):
			p.add(word[:i] + string[0] + word[i:])
	return p


# ---------------------------- MAIN


if __name__ == '__main__':
	'''
	Demo:
	 - creates string
	      "abc"
	'''
	string = "abc"
	print("String: " + string)
	print("Permutations:")
	for i in permutations(string):
		print(i)
