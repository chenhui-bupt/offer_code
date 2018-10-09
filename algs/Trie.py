class Node:
    def __init__(self):
        self.val = None
        self.next = [None] * 256


class TrieST:
    def __init__(self):
        self.root = Node()
        self.n = 0

    def get(self, key):
        if key is None:
            raise Exception()
        x = self.getHelper(key, 0)
        if not x:
            return None
        else:
            return x.val

    def getHelper(self, pNode, key, d):
        if not pNode: return
        if (d == len(key)):
            return pNode
        c = key[d]
        self.getHelper(pNode.next[ord(c)], key, d+1)

    def contains(self, key):
        return self.get(key) is not None

    def put(self, key, val):
        if key is None:
            raise Exception()
        if val is None:
            self.delete(key)
        self.root = self.put(self.root, key, val, 0)

    def putHelper(self, pNode, key, val, d):
        if not pNode:
            return Node()
        if d == len(key):
            if pNode.val is None:
                self.n += 1
            pNode.val = val
        c = key[d]
        pNode.next[ord(c)] = self.putHelper(pNode.next[ord(c)], key, val, d+1)
        return pNode

    def keysWithPrefix(self, prefix):
        results = []
        node = self.get(prefix)
        self.keysWithPrefixHelper(node, list(prefix), 0, results)
        return results

    def keysWithPrefixHelper(self, pNode, prefix, results):
        if pNode is None:
            return
        if pNode.val is not None:
            results.append(prefix[::])
        for i in range(256):
            prefix.append(chr(i))
            self.keysWithPrefixHelper(pNode.next[i], prefix, results)
            prefix.pop()

    def keysThatMatch(self, pattern):
        if pattern is None:
            raise Exception()
        results = []
        prefix = []
        self.keysThatMatchHelper(self.root, prefix, pattern, results)
        return results

    def keysThatMatchHelper(self, pNode, prefix, pattern, results):
        if pNode is None:
            return
        d = len(prefix)
        if len(prefix) == len(pattern) and pNode.val is not None:
            results.append(prefix[::])
        if len(prefix) == len(pattern):
            return
        c = pattern[d]
        if c == '.':
            for i in range(256):
                prefix.append(chr(i))
                self.keysThatMatchHelper(pNode.next[i], prefix, pattern, results)
                prefix.pop()
        else:
            prefix.append(c)
            self.keysThatMatchHelper(pNode.next[ord(c)], prefix, pattern, results)
            prefix.pop()

    def longestPrefixOf(self, query):
        return
    def delete(self, key):
        if key is None:
            raise Exception()
        self.root = self.deleteHelper(self.root, key, 0)

    def deleteHelper(self, pNode, key, d):
        if not pNode:
            return
        if d == len(key):
            if pNode.val is not None:
                self.n -= 1
            pNode.val = None
        else:
            c = key[d]
            pNode.next[ord(c)] = self.deleteHelper(pNode.next[ord(c)], key, d+1)
        if pNode.val is not None:
            return pNode
        for i in range(256):
            if pNode.next[i]:
                return pNode
        return None

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

