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

	def insert(self, word):
		''' 
		Insert a word, character by character, into the tree. If we arrive at a null child
		and still have characters left, we create a new node with the next character in word.
		Recursive base case: if we are at last character, just set endOfWord flag and we are done
		Note: When we insert a word with a substantial prefix that isn't found in the tree
		we just end up using a lot of equal nodes. This is by design. For a tree that
		has a more equitable distribution of prefixes, the tree with be more balanced (have less/minimal height)
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



	def hasChildren(self):
		return self.left or self.right or self.equal

	def allSuffixes(self, prefix):
		''' 
		Generate all possible words starting with this prefix in the tree.
		E.g. If prefix is empty, all words are generated.
		Note that we only need the equal child during the recursive call
		because left and right child are not used to build prefixes,
		strictly speaking, but only for comparison purposes.
		'''
		if self.endOfWord:
			yield '{0}{1}'.format(prefix,self.value)

		if self.left:
			self.left.allSuffixes(prefix)
		if self.right:
			self.right.allSuffixes(prefix)
		if self.equal:
			self.equal.allSuffixes(prefix+self.value)


	def autocomplete(self, prefix):
		'''
		Given a prefix, finds all words in tree that begin with this prefix
		'''
		node = self
		index = 0

		while node != None:
			char = prefix[index]
			if char == node.value:
				index += 1

				# what if we have multiple words in the tree that are in the prefix
				# if our prefix is right at the end of a word?
				# either way, we have found prefix, and we are done.
				if index == len(prefix):
					break

				node = node.equal				

			elif char > node.value:
				node = node.right
			elif char < node.value:
				node = node.left

		# we didn't find the prefix completely
		if index < len(prefix):
			print 'Prefix "%s" doesn\'t exist in tree' % (prefix)
			return set()

		return node.allSuffixes(prefix)