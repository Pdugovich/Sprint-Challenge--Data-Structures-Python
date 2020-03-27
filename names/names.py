import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
""" 
Running the code above took 16.169 seconds
(I should probably upgrade my machine)
the run time should be O(n^2), since for each name it needs
to check every other name in names 2. So it should perform around
100,000,000 searches.

This seems like a good use for a binary search tree, but what we did
in class won't exactly work

The main issues are that I need to compare the words somehow, and words
arent' numbers. During lecture, Brian reminded us that characters
have ASCII values, which are numbers and comparable.

Also, I need to save the name and the ASCII value so I can
append the name to the duplicates list
"""
class BinarySearchTree:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def insert(self, value):
		# The main adjustment to insert is comparing the value[1]s,
		# so the ASCII numbers will be compared, not the names
		if value[1] < self.value[1]:
			if self.left == None:
				self.left = BinarySearchTree(value)
			else:
				self.left.insert(value)
		elif value[1] >= self.value[1]:
			if self.right == None:
				self.right = BinarySearchTree(value)
			else:
				self.right.insert(value)

	def contains(self, target):
		# for this function, I am comparing again the ASCII values
		if target[1] == self.value[1]:
			# This was modified to remove the 'return' statement, 
			# since we're doing something, and also to append
			# the name, not ASCII value to the duplicates list
			duplicates.append(target[0])
		else:
			# This section is mostly unchanged. It is still recursive
			# until it finds an empty L/R node
			if target[1] < self.value[1]:
				if self.left == None:
					return
				else:
					return self.left.contains(target)
			elif target > self.value:
				if self.right == None:
					return
				else:
					return self.right.contains(target)

# I initiated the BinarySearchTree with the first name in names_1
# value[1] is a list comprehension, creating a list of ASCII values
# for each character in the name
bst = BinarySearchTree((names_1[0], [ord(c) for c in names_1[0]]))

# This first loop populates the BinarySearch Tree with the 
# names, ordered by ASCII code 
for name in names_1[1:]:
	bst.insert((name, [ord(c) for c in name]))
# This second loop checks if each name is 
for name in names_2:
	bst.contains((name, [ord(c) for c in name]))

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
