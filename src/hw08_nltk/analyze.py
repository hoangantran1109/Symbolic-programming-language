

import nltk
from nltk import FreqDist
from nltk import word_tokenize

class Analyzer(object):
    def __init__(self, path):
        '''reads the file text, creates the list of words (use nltk.word_tokenize to tokenize the text),
            and calculates frequency distribution '''
        self.text = nltk.word_tokenize(open(path).read()) #TODO the list of words from text file *DONE
        self.token_counts = FreqDist(word for word in self.text) #TODO frequency distribution of words from text file *DONE


    def numberOfTokens(self):
        '''returns number of tokens in the text '''
        return len((self.text))

    def vocabularySize(self):
        '''returns a list of the vocabulary of the text '''
        sorted(set(self.text))
        return len(set(self.text))

    def lexicalDiversity(self):
        '''returns the lexical diversity of the text '''
        a=len(set(self.text))
        b=len(self.text)
        return int (b/a)

    def getKeywords(self):
        '''return words as possible key words, that are longer than seven characters, that occur more than seven times (sorted alphabetically)'''
        pos_tag=nltk.pos_tag(self.text)
        list= [w for w in set(self.text) if len(w) > 7 and self.token_counts[w] > 7]
        return sorted(list)

    def numberOfHapaxes(self):
        '''returns the number of hapaxes in the text'''
        pass

    def avWordLength(self):
        '''returns the average word length of the text'''
        pass

    def topSuffixes(self):
        '''returns the 10 most frequent 2-letter suffixes in words
            (restrict to words of length 5 or more)'''
        pass

    def topPrefixes(self):
        '''returns the 10 most frequent 2-letter prefixes in words
            (restrict to words of length 5 or more)'''
        pass

    def tokensTypical(self):
        '''returns first 5 tokens of the (alphabetically sorted) vocabulary
        that contain both often seen prefixes and suffixes in the text. As in topPrefixes()
        and topSuffixes(), Prefixes and Suffixes are 2 characters long.'''
        pass
