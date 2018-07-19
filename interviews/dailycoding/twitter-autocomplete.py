"""
This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

https://www.dailycodingproblem.com/solution/11?token=48a76debff9240f4e5e03df7e472d5bc46dbf38f7a763c42c840bc3a780b335117f863d1
"""
ENDS_HERE = '__ENDS_HERE'

class Trie(object):
    def __init__(self):
        self._trie = {}

    def insert(self, text):
        trie = self._trie
        for char in text:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]
        trie[ENDS_HERE] = True

    def elements(self, prefix):
        d = self._trie
        for char in prefix:
            if char in d:
                d = d[char]
            else:
                return []
        return self._elements(d)

    def _elements(self, d):
        result = []
        for c, v in d.items():
            if c == ENDS_HERE:
                subresult = ['']
            else:
                subresult = [c + s for s in self._elements(v)]
            result.extend(subresult)
        return result

trie = Trie()
words = ["dog", "deer", "deal"]
for word in words:
    trie.insert(word)
    print trie._trie

def autocomplete(s):
    print "s = ",s
    return trie.elements(s)

print autocomplete("do")

print autocomplete("de")

print autocomplete("d")
