from ternarysearchtree import TernarySearchTree
import random
import time

test_prefixes = {
	'boa': set([]),
	'ano': set([]),
	'lic': set([]),
	'mon': set([]),
	'fen': set([]),
	'gir': set([]),
	'pel': set([]),
	'lio': set([]),
	'que': set([]),
	'coq': set([]),
}

def test_add_and_contains(words, prefixLen):
	t = TernarySearchTree()
	#test_prefixes = {} # as we build the tree, we get all the words starting with the prefixes we want to test
	maxInsert = 0
	maxContains = 0
	for w in words:

		# time insert
		add_start = time.time()
		t.insert(w)
		add_end = time.time() - add_start
		maxInsert = max(maxInsert, add_end)

		if len(w) >= prefixLen:
			if w[:prefixLen] in test_prefixes:
				test_prefixes[w[:prefixLen]].add(w)

		contains_start = time.time()
		assert(w in t)
		contains_end = time.time() - contains_start
		maxContains = max(maxContains, contains_end)

	print 'Max Insert time was %f sec, Max Membership Checking time was %f sec' % (maxInsert, maxContains)
	return t

def test_autocomplete(t, words):
	# how do we know the words that the algorithm finds are all the possible words
	#max_autocomplete_time = 0
	for prefix in test_prefixes.keys():
		# we can check the equality of sets this way (quite pythonic) or ask if symmetric difference is size 0
		start = time.time()
		completions = t.autocomplete(prefix)
		assert(completions == test_prefixes[prefix])
		print 'Autocomplete time for prefix "%s" with %d words was %f sec' % (prefix, len(completions), time.time() - start) 



''' Generate an arbitrary prefix of length prefixLen and add it to dictionary '''
def getPrefixes(prefixLen):
	pass

if __name__ == '__main__':
	'''
	Read in a large text file from path using 'cat /usr/share/dict/words > words.txt' (235K words) 
	'''
	f = open('./words.txt')
	words = set([])
	for line in f:
		words.add(line[:-1])

	t = test_add_and_contains(words, 3)
	test_autocomplete(t, words)