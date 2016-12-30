### Question 1

"""
Returns an array with all possible anagrams of a word
:param string word: the word that will generate all anagrams
:return array: an array of strings with all the anagrams
"""
def anagrams(word):
    if len(word) <=1:
        return word
    else:
        tmp = []
        for perm in anagrams(word[1:]):
            for i in range(len(word)):
                tmp.append(perm[:i] + word[0:1] + perm[i:])
        return tmp

def first_question(s,t):

    # Checks for null values
    if s == None or t == None:
        return False

    # Checks of the target word is longer than the original word
    if len(s) < len(t):
        return False

    # get all the anagrams in the target word and checks if they are
    # a substring of the original word
    for anagram in anagrams(t.lower()):
        if anagram in s.lower():
            return True

    return False

# Test Case #1
print first_question("udacity","")
# This call should return false since an empty string does not contains any anagram
# Test Case #2
print first_question("udacity",None)
# This call should return false since a null object doesn't have any anagram
# Test Case #3
print first_question("","ad")
# This call should return false since an empty string contains no substrings
# Test Case #4
print first_question(None,"ad")
# This call should return false since a null object contains no substring
# Test Case #5
print first_question("","")
# This call should return false since an empty string does not contains any anagram
# Test Case 6
print first_question(None,None)
# This call should return false since both strings are null
# Test Case 7
print first_question("UdAcItY","aD")
# This call should return true since "aD" has the "da" anagram and is contained in the initial string
# Test Case #8
print first_question("BPQrjPYGB6LP58Ua2F6fShf7fQ0APJnmnv3kgbj5M6XsmBzbvAvDnmr1tj4SrAGVecHeoKZGItJD2HqlhZ1jHOO29Okhj16PNKLyUvXaifWeQTP72UqBSezUqJiGHQxBsc5Ehp5Dv7VIHk06B3Lvs4RyAYmYc9wImo0Dn9LEW0blEEhQO33QygGV80rJyiYsYYLHVr3yfmitmobeee4F5ngyFDeM7WwOsZyUTRcynPsGN7tsE0pxYTzeCejfEJwo6NJOXtPLsF0NWNivVq2WnMRZuI0bIT2yz9IWNJ3UC4lj2WEhkkLNm1HRtXBuwOWoD1P9jqvCPkaC2NRVazXBQULIsKG2Mbt6cTaxlJWBb7sIMWbCgiKS3368wxEb5hIBoYJIaEUUnOjYZ599br3I6QFvJVyTjAR6ccwkTczroNn6gtu2UgpTX4eKIZ8Yo4hIYQlLAoOO99IAVSqZcPpj44x3RBJMpbYZoL282tr87PlZSGaWHwFC1rwAPGASAjPU7SBm1kUYsV63jyopxjGXsoU1FQKVzsZDNFh1ZswVyQ83E9MrJpXfhAGbXP6epEtUsHPVeRSlwJwkTX9qcUP4A9cK2zf55wADCMuFfIzSesGhWKZrzBsVhA92iuGDh4WFL0UMCjJLyhpC6v49MGZnLqxSVPuIs4DW9iP9Ar4W7DhnptuirwpXHJXiqjFBHFHwpi8DJnxAk84ZEQei6yXKXsJH23EQbqEFRsxsJG3T3jWgr8nBuKVrGB7aDaSgqpG3KivkR8TzobIWVu59uq5MEqVFZxtP0komrXXazJ8IOxxSRR5vczc1OMyohJubLXNQwcYJhl9floEYLyqpL0zuZ4R7HFDzFQNjsyDnoCGxioyzHTr68fEY5zSZP7NbzcI6I1S4YCS06ynjhDrCk6jFZYC0f2Eq9Z97H6qKjSzouuQJT6GIuACplbnleo0SEAI3sIaJi0ck8w1LP7glLjIBJT2BHcssicxYAwl40a2z","ohMy")
# This call should return true since "ohMy" has the "myoh" anagram and is contained in the initial string
# Test Case #9
print first_question("BPQrjPYGB6LP58Ua2F6fShf7fQ0APJnmnv3kgbj5M6XsmBzbvAvDnmr1tj4SrAGVecHeoKZGItJD2HqlhZ1jHOO29Okhj16PNKLyUvXaifWeQTP72UqBSezUqJiGHQxBsc5Ehp5Dv7VIHk06B3Lvs4RyAYmYc9wImo0Dn9LEW0blEEhQO33QygGV80rJyiYsYYLHVr3yfmitmobeee4F5ngyFDeM7WwOsZyUTRcynPsGN7tsE0pxYTzeCejfEJwo6NJOXtPLsF0NWNivVq2WnMRZuI0bIT2yz9IWNJ3UC4lj2WEhkkLNm1HRtXBuwOWoD1P9jqvCPkaC2NRVazXBQULIsKG2Mbt6cTaxlJWBb7sIMWbCgiKS3368wxEb5hIBoYJIaEUUnOjYZ599br3I6QFvJVyTjAR6ccwkTczroNn6gtu2UgpTX4eKIZ8Yo4hIYQlLAoOO99IAVSqZcPpj44x3RBJMpbYZoL282tr87PlZSGaWHwFC1rwAPGASAjPU7SBm1kUYsV63jyopxjGXsoU1FQKVzsZDNFh1ZswVyQ83E9MrJpXfhAGbXP6epEtUsHPVeRSlwJwkTX9qcUP4A9cK2zf55wADCMuFfIzSesGhWKZrzBsVhA92iuGDh4WFL0UMCjJLyhpC6v49MGZnLqxSVPuIs4DW9iP9Ar4W7DhnptuirwpXHJXiqjFBHFHwpi8DJnxAk84ZEQei6yXKXsJH23EQbqEFRsxsJG3T3jWgr8nBuKVrGB7aDaSgqpG3KivkR8TzobIWVu59uq5MEqVFZxtP0komrXXazJ8IOxxSRR5vczc1OMyohJubLXNQwcYJhl9floEYLyqpL0zuZ4R7HFDzFQNjsyDnoCGxioyzHTr68fEY5zSZP7NbzcI6I1S4YCS06ynjhDrCk6jFZYC0f2Eq9Z97H6qKjSzouuQJT6GIuACplbnleo0SEAI3sIaJi0ck8w1LP7glLjIBJT2BHcssicxYAwl40a2z","Udacity")
# This call should return true since "Udacity" doesn't has any anagram that's contained in the original string

### Question 2

import re

"""
Returns an array with all possible palindromes of a word
:param string word: the word that will generate all the palindromes
:return array: an array of strings with all the anagrams
"""
def palindromes(word):

    if len(word) < 1:
        return set()

    if len(word) == 1:
        return set('a')

    results = set()
    word_length = len(word)
    for idx, char in enumerate(word):

        start, end = idx - 1, idx + 1
        while start >= 0 and end < word_length and word[start] == word[end]:
            results.add(word[start:end+1])
            start -= 1
            end += 1

        start, end = idx, idx + 1
        while start >= 0 and end < word_length and word[start] == word[end]:
            results.add(word[start:end+1])
            start -= 1
            end += 1

    return list(results)

def second_question(a):

    # checks for null values
    if a == None:
        return None

    # remove empty spaces
    a = a.replace(" ", "").lower()
    # remove punctuations
    a = re.sub(r'[^\w\s]','',a)

    length_of_longest_palindrome = 0
    longest_palindrome = ""

    # get all the palindromes in the word and checks which is the longest
    for palindrome in palindromes(a):
        if len(palindrome) > length_of_longest_palindrome:
            longest_palindrome = palindrome
            length_of_longest_palindrome = len(palindrome)

    return longest_palindrome

# Test Case #1
print second_question("Aerate pet area.")
# This call should return "aeratepetarea" since it's the longest palindrome in the string
# Test Case #2
print second_question("")
# This call should return an empty string since it's getting an empty string as a parameter and an empty string
# has no palindromes
# Test Case #3
print second_question(None)
# This call should return a null value since it's getting a null value as a parameter and a null value
# has no palindromes
# Test Case #4
print second_question("a")
# This call should return "a" since the palindrome of a string of one character is its own palindrome
# Test Case #5
print second_question("A but tuba.A car, a man, a maraca.A dog, a plan, a canal: pagoda.A dog! A panic in a pagoda!A lad named E. MandalaA man, a plan, a canal: Panama.A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal-Panama!A new order began, a more Roman age bred Rowena.A nut for a jar of tuna.A Santa at Nasa.A Santa dog lived as a devil God at NASA.A slut nixes sex in Tulsa.A tin mug for a jar of gum, Nita.A Toyota! Race fast, safe car! A Toyota!A Toyota's a Toyota.Able was I ere I saw Elba.Acrobats stab orca.Aerate pet area.Ah, Satan sees Natasha!Aibohphobia (fear of palindromes)Air an aria.Al lets Della call Ed Stella.alulaAmen icy cinema.Amore, Roma.Amy, must I jujitsu my ma?AnaAnimal loots foliated detail of stool lamina.AnnaAnne, I vote more cars race Rome to Vienna.Are Mac 'n' Oliver ever evil on camera?Are we not drawn onward to new era?Are we not drawn onward, we few, drawn onward to new era?Are we not pure? 'No sir!' Panama's moody Noriega brags. 'It is garbage!' Irony dooms a man; a prisoner up to new era.Art, name no tub time. Emit but one mantra.As I pee, sir, I see Pisa!Avid diva.")
# This call should return "raarewenotpurenosirpanamasmoodynoriegabragsitisgarbageironydoomsamanaprisoneruptoneweraar" since it's the longest palindrome in the string

### Question 3

import heapq
from collections import defaultdict

"""
Returns a dictionary that is a represenation of the MST
:param dictionary G: the adjacency list representing the tree
:return dictionary: the adjacency list representing the MST
"""
def third_question(G):

    if G == {} or G == None:
        return None

    if len(G) < 2:
        return G

    # create the adjaceny list
    graph = [[0]*len(G) for _ in range(len(G))]
    vertices = list(G.keys())

    # assign values to the adjaceny list
    for node in range(len(G)):
        for edge in G[vertices[node]]:
            graph[node][vertices.index(edge[0])] = edge[1]

    T = set();
    X = set();

    # Select a random starting point
    X.add(0);

    # cross the adjacency list to calculate the MST
    while len(X) != len(vertices):
        crossing = set();

        for x in X:
            for k in range(len(vertices)):
                if k not in X and graph[x][k] != 0:
                    crossing.add((x, k))

        edge = sorted(crossing, key=lambda e:graph[e[0]][e[1]])[0];
        T.add(edge)
        X.add(edge[1])

    # Make the adjacency list for the MST in the required format
    result = {}

    for vertice in vertices:
        result[vertice] = []

    for edge in T:
        result[vertices[edge[0]]].append((vertices[edge[1]],graph[edge[0]][edge[1]]))

    for vertice in vertices:
        if result[vertice] == []:
            result.pop(vertice, None)

    return result

# Test Case #1
G = {'A': [('B', 2)],'B': [('A', 2), ('C', 5)],'C': [('B', 5)]}
print third_question(G)
# This call should return {'A': [('B', 2)], 'B': [('C', 5)]} that's the MST for the given tree
# Test Case #2
G = {0:[(1,11),(2,13),(3,12)],1:[(0,11),(3,14)],2:[(0,13),(3,10)],3:[(0,12),(1,14),(2,10)]}
print third_question(G)
# This call should return {0: [(1, 11), (3, 12)], 3: [(2, 10)]} that's the MST for the given tree
G = {}
# Test Case #3
print third_question(G)
# This call should return None as an empty tree doesn't have a MST
G = None
# Test Case #4
print third_question(G)
# This call should return None as an null object doesn't have a MST
# Test Case #5
G = {'A': [('B', 2)]}
print third_question(G)
# This call should return {'A': [('B', 2)]} that's the MST for the given tree
# Test Case #6
G = {'A': []}
print third_question(G)
# This call should return {'A': []} because the MST of single-noded tree is itself

### Question 4

"""
Returns a dictionary that is a represenation of the MST
:param List T: list of list representing the binary tree
:param r: index of the root node
:param n1: index of the first node
:param n1: index of the second node node
:return int: index of the least common ancestor
"""
def fourth_question(T, r, n1, n2):

    if r > len(T) or n1 > len(T) or n2 > len(T):
        return "Error: values out of range"

    if sum(T[r]) == 0:
        return "Error: the root doesn't have any children"

    node_1_ancestors = []
    node_2_ancestors = []
    number_of_nodes = len(T)

    node = n1
    step = 0

    # get all the ancestors of the first node
    while r not in node_1_ancestors:
        for i in range(0,number_of_nodes):
            if len(T[i]) != len(T):
                return "Error: arrays length doesn't match"
            if T[i][node] == 1:
                node_1_ancestors.append(T[i][node] * i)
                node = T[i][node] * i

    node = n2

    # get all the ancestors of the second node
    while r not in node_2_ancestors:
        for i in range(0,number_of_nodes):
            if T[i][node] == 1:
                node_2_ancestors.append(T[i][node] * i)
                node = T[i][node] * i

    # get which ancestor list is the longest
    longest_ancestors_list = []

    if len(node_1_ancestors) > len(node_2_ancestors):
        longest_ancestors_list = node_1_ancestors
    else:
        longest_ancestors_list = node_2_ancestors

    least_common_ancestor = longest_ancestors_list[-1]

    #get the common ancestors
    common_ancestors = list(set(node_1_ancestors).intersection(node_2_ancestors))

    # calculate the least common ancestor
    for ancestor in common_ancestors:
        if longest_ancestors_list.index(ancestor) > longest_ancestors_list.index(least_common_ancestor):
            least_common_ancestor = ancestor

    return least_common_ancestor

# Test Case #1
print fourth_question([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)
# This case should return '3', since 3 is the least common ancestor

print fourth_question([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          6)
# This case should return error because the value of n2 is out of boundaries

print fourth_question([
           [0, 0, 0, 0, 0],
           [0, 0, 1, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 1, 0, 0]],
          3,
          1,
          4)
# This case should return error because the value the lenghts of the arrays doesn't match

print fourth_question([[0, 1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0, 0],
           [1, 0, 0, 1, 0, 0],
           [0, 0, 0, 0, 1, 0],
           [0, 0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0, 0]],
          2,
          1,
          5)
# This case should return '4', since 4 is the least common ancestor

print fourth_question([[0, 1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 1, 0],
           [0, 0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0, 0]],
          2,
          1,
          5)
# This case should return error because the root doesnt have any children

### Question 5

# Definition of Node class
class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

# Insert a node to a list
def insert(node,data):
    new_node = Node(data)
    new_node.set_next(self.head)
    self.head = new_node

# Linked List Class
class linked_list:
    def __init__(self):
        self.head = None
        self.size = 0

    # add node to a list method
    def add_node(self, data):
        new_node = Node(0)
        new_node.data = data
        new_node.next = self.head
        self.head = new_node

    # print the list method (for testing purposes)
    def list_print(self):
        node = self.head
        while node:
            print node.data
            node = node.next

# Create a linked list
def create_list_of_size(size):
    ll = linked_list()
    ll.size = size
    for i in range(size,0,-1):
        ll.add_node(i)
    return ll

def fifth_question(ll,m):

    if ll == None:
        return None

    node = ll

    # get the size of the list
    size = 0
    while node:
        size += 1
        node = node.next

    if m > size or m < 0:
        return "Error: the selected index is out of bounds"

    # calculate the positon of the node we're looking for
    position = size - m

    # move the current node to the position we want
    result = ll
    for i in range(0,position):
        result = result.next
    return result

# Test Case #1
ll = create_list_of_size(5).head
print fifth_question(ll,3).data
# This test case must return a node with data 3

# Test Case #2
ll = create_list_of_size(9).head
print fifth_question(ll,3).data
# This test case must return a node with data 7

# Test Case #3
ll = create_list_of_size(5072384).head
print fifth_question(ll,3).data
# This test case must return a node with data 5072382

# Test Case #4
ll = create_list_of_size(7).head
print fifth_question(None,3)
# This test case must return None

# Test Case #5
ll = create_list_of_size(7).head
print fifth_question(ll,9)
# This test case must return the following error: the selected index is out of bounds

# Test Case #6
ll = create_list_of_size(7).head
print fifth_question(ll,-6)
# This test case must return the following error: the selected index is out of bounds

# Test Case #7
ll = create_list_of_size(7).head
print fifth_question(ll,0)
# This test case must return None
