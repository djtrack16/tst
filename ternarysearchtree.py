class TernarySearchTree():

	# ternary search trees can be used any time a hashtable would be used to store strings
	# tries are suitable when there is a proper distribution of words over the alphabet(s).
	# ternary trees are more space-efficient when the strings to be stored share a common prefix
	# for "given a word, find the next word in dictionary" or
	# "find all telephone numbers with 9342" or "typing few starting character in a web browser
	# " .... displays all website names with this prefix (i.e. auto complete feature)"
	# 
	# You can check with wikipedia article for a brief introduction.

	#Design: left < node, right > node, down >= node
	# each node ends up being a prefix of stored strings. all strings in the middle subtree of a node
	# start with that prefix.
	def __init__(self, value=None, left=None, right=None, equal=None, endOfWord=False):
		self.value = value # idiomatically, this is a letter, but using 'value' so we know it can actually be any character
		self.left = left
		self.right = right
		self.equal = equal
		self.endOfWord = False


	def __contains__(self, word):
		# if word has been parsed down to empty, just see if this character sequence is marked as a word
		# note that even if the string is present in the tree, we only care if the endOfWord flag is True
		# otherwise, this word is not in our tree.
		node = self
		while node != None:
			char = word[0]
			if char == node.value:
				word = word[1:]
				if word == '':
					return node.endOfWord
				node = node.equal
			elif char > node.value:
				node = node.right
			elif char < node.value:
				node = node.left
		# if word is never empty, we didn't find the complete string in trie
		return False

	''' Insert a word, character by character, into the tree. If we arrive at a null child
		and still have characters left, we create a new node with the next character in word.
		Recursive base case: if we are at last character, just set endOfWord flag and we are done
		Note: When we insert a word with a substantial prefix that isn't found in the tree
		we just end up using a lot of equal nodes. This is by design. For a tree that
		has a more equitable distribution of prefixes, the tree with be more balanced (have less/minimal height)
	'''
	def insert(self, word):
		
		char = word[0]
		if not self.value:
			self.value = char

		if char < self.value:
			if not self.left:
				self.left = TernarySearchTree()
			self.left.insert(word)
		elif char > self.value:
			if not self.right:
				self.right = TernarySearchTree()
			self.right.insert(word)
		else:
			if len(word) == 1:
				self.endOfWord = True
				return

			if not self.equal:
				self.equal = TernarySearchTree()
			self.equal.insert(word[1:])

	def delete(self, word):
		# TODO
		pass

	''' Simple function to traverse the tree in post-order like fashion'''
	def traverse(self):
		# if we want to see how our tree is constructed
		if self.left:
			self.left.traverse()
		if self.equal:
			self.equal.traverse()
		if self.right:
			self.right.traverse()
		print self.value

	''' Given a prefix, generate all possible suffixes in the tree.
		E.g. If prefix is '', we print all the words in our tree
		Note that we only need the equal child during the recursive call
		because left and right child are not used to build prefixes,
		strictly speaking, but only for comparison purposes.
	'''
	def allSuffixes(self, prefix):
		if self.endOfWord:
			print prefix+self.value

		if self.left:
			self.left.allSuffixes(prefix)
		if self.right:
			self.right.allSuffixes(prefix)
		if self.equal:
			self.equal.allSuffixes(prefix+self.value)


	''' Given a prefix, finds the ending node of this prefix in the tree,
		Then calls allSuffixes method (above) on the given prefix
	'''
	def autocomplete(self, prefix):
		node = self
		index = 0
		while node != None:
			char = prefix[index]
			if char == node.value:
				index += 1
				node = node.equal
				# once we find it here, we are done.
				if index == len(prefix):
					break
			elif char > node.value:
				node = node.right
			elif char < node.value:
				node = node.left

		# we didn't find the prefix completely
		if index < len(prefix):
			print 'Prefix "%s" doesn\'t exist in tree' % (prefix)
			return

		node.allSuffixes(prefix)

	''' Destroy the tree in bottom-up fashion.
		Delete all the leaves first, then delete their parents, and so forth up the tree
		To actually 'delete', we can use variable=None or python's del keyword.
		We release the attributes first, and then delete the class instance itself
		The use of del vs None is somewhat debatable and polarizing within the python community
		I use both to annoy everyone :)
	'''
	def destroy(self):
		if self.left: self.left.destroy()
		if self.right: self.right.destroy()
		if self.equal: self.equal.destroy()

		self.value = None
		self.endOfWord = None
		del self