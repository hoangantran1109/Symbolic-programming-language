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
        self.text = word_tokenize(open(path).read()) #TODO the list of words from text file *DONE
        #self.token_counts = FreqDist(word for word in self.text) #TODO frequency distribution of words from text file *DONE
        self.token_counts = FreqDist(self.text)

    def numberOfTokens(self):
        '''returns number of tokens in the text '''
        return len((self.text))

    def vocabularySize(self):
        '''returns a list of the vocabulary of the text '''
        #sorted(set(self.text))
        #return len(set(self.text))
        return len(self.token_counts)
    def lexicalDiversity(self):
        '''returns the lexical diversity of the text '''
        # a=len(set(self.text))
        # b=len(self.text)
        # return int (b/a)
        return (self.numberOfTokens()/self.vocabularySize())

    def getKeywords(self):
        '''return words as possible key words, that are longer than seven characters, that occur more than seven times (sorted alphabetically)'''
        # list= [w for w in set(self.text) if len(w) > 7 and self.token_counts[w] > 7]
        # return sorted(list)
        return sorted(k for (k,v) in self.token_counts.items() if len(k) > 7 and v > 7)

    def numberOfHapaxes(self):
        '''returns the number of hapaxes in the text'''
        return len(self.token_counts.hapaxes())

    def avWordLength(self):
        '''returns the average word length of the text'''
        # wordCount = len(self.token_counts)
        # sum = 0
        # for word in self.token_counts:
        #     ch = len(word)
        #     sum = sum + ch
        # avg = sum / wordCount
        # return avg
        sum=0
        for word in self.token_counts:
            sum+=len(word)
        return sum/self.vocabularySize()


    def topSuffixes(self):
        '''returns the 10 most frequent 2-letter suffixes in words
            (restrict to words of length 5 or more)'''

        # list = [w for w in set(self.text) if self.token_counts[w] >= 5]
        # lista = sorted(list[2:])
        # return lista[0:9]
        wordsge5 = [w for w in self.token_counts.keys() if len(w) >= 5]
        suff= [w[-2:] for w in wordsge5]
        suff_fd = FreqDist(suff)
        return[s for s,_ in suff_fd.most_common(10)]

    def topPrefixes(self):
        '''returns the 10 most frequent 2-letter prefixes in words
            (restrict to words of length 5 or more)'''
        wordsge5 = [w for w in self.token_counts.keys() if len(w) >= 5]
        pref = [w[:2] for w in wordsge5]
        pref_fd = FreqDist(pref)
        return [s for s, _ in pref_fd.most_common(10)]

    def tokensTypical(self):
        '''returns first 5 tokens of the (alphabetically sorted) vocabulary
        that contain both often seen prefixes and suffixes in the text. As in topPrefixes()
        and topSuffixes(), Prefixes and Suffixes are 2 characters long.'''
        sorted_voc= sorted(self.token_counts)
        suffs=self.topSuffixes()
        prefs=self.topPrefixes()
        typical=[]
        for token in sorted_voc:
            for i in suffs:
                if i == token[-2:]:
                    for j in prefs:
                        if j == token[:2]:
                            typical.append(token)

        return typical[:5]

    #return [ t for t in sorted(self.token_counts) if t[-2:] in self.topSuffixes() and t[2:] in self.topPrefixes()][:5]