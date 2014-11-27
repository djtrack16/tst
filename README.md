tst
===

A less-naive trie implementation known as "ternary search tree" (TST) is useful for storing prefixes of strings. TSTs are most suitable when you are storing a proper distribution of words over the alphabet.


**Advantages**

* More memory efficient than naive trie implementation. In a TST, common prefixes are stored in a much smarter way, unless the insertion order of elements creates a degenerate TST (e.g. when it basically looks like a linked list)
* Decent search time for a prefix: O(klogn) where *k* is the length of the word and *n* is the height of the tree (Later, I will give a runtime analysis per method)
* Partial matches, approximation matching, near-neighbor lookups, 

**Disadvantages**

* Slower search than naive trie (naive trie search time is always O(length of word))
* By design, we use a full node for every character in every string -- so for many insertions, memory usage will probably go up sharply, especially when more than half of the nodes don't have a common prefix  Succinct trees or compact prefix trees improve on this, and IIRC, have slightly faster search times (Please correct me if I'm wrong)
* If we are trying to store large keys (length > 10^3), we are better off using a data structure with hashing (dict, set, etc)
* Deleting words can get tricky.

**Complexity:**
(klogn, k=length of word, n is height of tree; worst case, we traverse height of tree)
- Insert, Membership, Delete: O(klogn)
- Delete Tree: O(numNodes)
- Size: O(1)
- Autocomplete: O(number of words that begin with that prefix)

**API**

root = TernarySearchTree()

*Add word*

root.insert('apple')

*Membership*

Ex.
If apple in root: return True

*Autocomplete*

What words in our tree begin with this prefix, 'ba'?

root.autocomplete(prefix) finds the last node in this prefix, and begins searching for all possible suffixes here.

If prefix is empty string, prints all words in the tree.

*Delete Tree*

root.destroy()

*Traverse Tree*

root.traverse() (post-order traversal by default)

**TODOs**

- Capability for deleting words
- Self-balancing strategy to avoid degeneracy (especially in cases where we delete a word that is in the midst of a common prefix)
- Performance and functionality testing
- Let me know if you'd like to use this. I can set up a package for it
- Comparison handling for case-insensitivity (maybe add another flag in node for case?)

For the curious:
http://www1.bcs.org.uk/upload/pdf/oommen.pdf


*Performance*

*When processing 250K words* Maximum time to insert a word, and maximum time to check if a word is in trie

?:tst dliddell$ python test_tst.py 
* Max Insert time was 0.562557 sec, Max Membership Checking time was 0.024212 sec
* autocomplete time for prefix "pel" with 141 words was 0.001439 seconds
* autocomplete time for prefix "coq" with 18 words was 0.000227 seconds
* autocomplete time for prefix "lio" with 23 words was 0.000262 seconds
* autocomplete time for prefix "que" with 144 words was 0.001258 seconds
* autocomplete time for prefix "mon" with 817 words was 0.007794 seconds
* autocomplete time for prefix "lic" with 65 words was 0.000615 seconds
* autocomplete time for prefix "fen" with 49 words was 0.000450 seconds
* autocomplete time for prefix "boa" with 69 words was 0.000682 seconds
* autocomplete time for prefix "ano" with 152 words was 0.001605 seconds
* autocomplete time for prefix "gir" with 49 words was 0.000412 seconds

