class TernarySearchTree():

	def __init__(self, value=None, endOfWord=False):
		self.value = value
		self.left = None
		self.right = None
		self.equal = None
		self.endOfWord = endOfWord


	def __contains__(self, word):
		'''
		If all characters of the word are found in trie, returns True if node corresponding to
		last character has 'endOfWord' marked as True. Note that even if the string is present
		in the tree, we only care about endOfWord value.
		'''
		node = self
		for char in word:
			while True:
				if not node:
					return False
				if char > node.value:
					node = node.right
				elif char < node.value:
					node = node.left
				else:
					last = node
					node = node.equal
					break
		return last.endOfWord

	# TODO: THIS WORKS, BUT IT DOESN'T MAKE MUCH SENSE, NEEDS REFACTORING
	def insert(self, word):
		''' 
		Insert a word, character by character, into the tree. If we arrive at a null child
		and still have characters left, we create a new node with the next character in word.
		Recursive base case: if we are at last character, just set endOfWord flag and we are done
		Note: When we insert a word with a substantial prefix that isn't found in the tree
		we just end up using a lot of equal nodes. This is by design. For a tree that
		has a more equitable distribution of prefixes, the tree with be more balanced (have
		less/minimal height)
		'''
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


	# INCOMPLETE, NOT WORKING/TESTED
	def delete(self, word):
		'''
		If word is found in tree, deletes word. Otherwise, does nothing.
		Four scenarios:
		1. Word is not in tree:
			-> do nothing
		2. Word is not prefix or suffix of any other word in tree
			-> delete all nodes in word
		3. Word is prefix of another word in tree
			-> set node.endOfWord to False
		4. Another word is prefix of this word in tree:
			-> (if node has no children), delete leaf nodes bottom-up up to most recent word
		'''
		# CASE 1
		if not word and not (node.endOfWord or node.hasChildren):
			return False

		node = self
		char = word[0]
			
		if char == node.value:
			word = word[1:]

			if node.endOfWord and not word:
				#CASE 3 and 4
				node.endOfWord = False
				if node.hasChildren():
					return False
				return True

			node = node.equal

		elif char > node.value:
			node = node.right
		elif char < node.value:
			node = node.left

		if node.delete(word):
			pass



	def hasChildren(self):
		return self.left or self.right or self.equal

	def all_suffixes(self, prefix):
		''' 
		Generate all possible words starting with this prefix in the tree.
		E.g. If prefix is empty, all words are generated.
		Note that we only need the equal child during the recursive call
		because left and right child are not used to build prefixes,
		strictly speaking, but only for comparison purposes.
		'''
		if self.endOfWord:
			yield "{0}{1}".format(prefix,self.value)

		if self.left:
			for word in self.left.all_suffixes(prefix):
				yield word
		if self.right:
			for word in self.right.all_suffixes(prefix):
				yield word
		if self.equal:
			for word in self.equal.all_suffixes(prefix+self.value):
				yield word


	def autocomplete(self, prefix):
		'''
		Given a prefix, finds all words in tree that begin with this prefix
		'''
		node = self
		for char in prefix:
			while True:
				if char > node.value:
					node = node.right
				elif char < node.value:
					node = node.left
				else:
					node = node.equal
					break
				if not node:
					print 'Prefix "%s" doesn\'t exist in tree' % (prefix)
					return set()
		return node.all_suffixes(prefix)
		

