'''This module implements Trie Data structure'''


class Node:
    '''Represents a node in the Trie'''

    def __init__(self):
        self.word = None
        self.word_type=None
        self.meaning =None
        self.childs = {}  # dict of childs


    def __insert__(self,word,word_type=None,meaning=None,string_pos=0):
        """Add a word to the node in a Trie"""
        if string_pos == len(word):
            self.word = word
            self.meaning=meaning
            self.word_type=word_type

            return True

        current_letter = word[string_pos]
        # Create the Node if it does not already exist
        if current_letter not in self.childs:
            self.childs[current_letter] = Node()

        self.childs[current_letter].__insert__(word,word_type, meaning=meaning,string_pos= (string_pos + 1))

        return True

    def __get_all__(self):
        """Get all of the words in the trie"""
        x = []
        for key, node in self.childs.items():
            if node.word is not None:
                x.append(node.word)

            x = x + node.__get_all__()

        return x




class Trie:
    """Trie Python Implementation"""
    def __init__(self):
        self.root = Node()

    def insert(self, word,word_type=None,meaning=None):
        '''Inserts "word" in trie'''
        self.root.__insert__(word,word_type,meaning)

    def all_words(self):
        '''Returns a list having all the words of trie'''
        return self.root.__get_all__()

    def prefix_search(self,word)->list:
        '''Returns a list having all the words of trie which have word as
        prefix
        '''
        tempNode=self.root
        #print(tempNode is self.root)

        for c in word:
            if c not in tempNode.childs:
                return []

            tempNode=tempNode.childs[c]

        if tempNode.childs.__len__()==0:
            return [tempNode.word]

        return tempNode.__get_all__()


    def get_meaning(self,word)->tuple:

        '''If word is found in the Trie ,returns a tuple (word,type of word,meaning of word)
        otherwise returns Empty tuple'''
        temp_node=self.root

        for c in word:
            if c not in temp_node.childs:
                return tuple()

            temp_node =temp_node.childs[c]

        return (temp_node.word,temp_node.word_type,temp_node.meaning)

