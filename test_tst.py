from ternarysearchtree import TernarySearchTree
import random
import time

prefixes = [
	'boa',
	'ano',
	'mon',
	'fen',
	'gir',
	'pel',
	'lio',
	'que',
	'coq',
	'lic'
]

def test_add_and_contains(words, prefixLen, test_prefixes):
	t = TernarySearchTree()
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

def test_autocomplete(t, test_prefixes):
	# how do we know the words that the algorithm finds are all the possible words
	for prefix in test_prefixes.keys():
		# we can check the equality of sets this way (quite pythonic) or ask if symmetric difference is size 0
		start = time.time()
		completions = {word for word in t.autocomplete(prefix)}
		#print completions
		#print test_prefixes[prefix]
		assert(completions - test_prefixes[prefix] == set())
		print 'Autocomplete time for prefix "%s" with %d words was %f sec' % (prefix, len(completions), time.time() - start) 


if __name__ == '__main__':
	'''
	Read in a large text file from path using 'cat /usr/share/dict/words > words.txt' (235K words) 
	'''
	f = open('./words.txt')
	words = {line[:-1] for line in f}
	test_prefixes = {prefix: set([]) for prefix in prefixes}
	t = test_add_and_contains(words, 3, test_prefixes)
	test_autocomplete(t, test_prefixes)
	