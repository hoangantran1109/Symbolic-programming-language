import re

import nltk
from nltk import FreqDist
from nltk import word_tokenize
from nltk.tokenize import *
from nltk.corpus import brown, stopwords


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
        list= [w for w in set(self.text) if len(w) > 7 and self.token_counts[w] > 7]
        return sorted(list)

    def numberOfHapaxes(self):
        '''returns the number of hapaxes in the text'''
        return len(self.token_counts.hapaxes())

    def avWordLength(self):
        '''returns the average word length of the text'''
        wordCount = len(self.token_counts)
        sum = 0
        for word in self.token_counts:
            ch = len(word)
            sum = sum + ch
        avg = sum / wordCount
        return avg


    def topSuffixes(self):
        '''returns the 10 most frequent 2-letter suffixes in words
            (restrict to words of length 5 or more)'''
        # tokens = self.text
        # stop_words = set(stopwords.words('english'))
        # tokens = [t for t in tokens if t not in stop_words]
        # fdist = nltk.FreqDist(tokens)
        # return [suffix for suffix, freq in fdist.most_common(10)]

    def topPrefixes(self):
        '''returns the 10 most frequent 2-letter prefixes in words
            (restrict to words of length 5 or more)'''
        pass

    def tokensTypical(self):
        '''returns first 5 tokens of the (alphabetically sorted) vocabulary
        that contain both often seen prefixes and suffixes in the text. As in topPrefixes()
        and topSuffixes(), Prefixes and Suffixes are 2 characters long.'''
        pass
