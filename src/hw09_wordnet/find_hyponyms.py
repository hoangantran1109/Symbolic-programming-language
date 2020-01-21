import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet
from collections import defaultdict

class HyponymSearcher(object):
    def __init__(self, text_path):

        self.noun_lemmas = []

        #TODO Read text as a string
        text=open(text_path).read()

        #TODO Split into sentences: use nltk.sent_tokenize
        sentences=nltk.sent_tokenize(text)

        #TODO Split into tokens: use nltk.word_tokenize
        tokens=nltk.word_tokenize(text)

        #TODO Perform POS tagging
        pos_tags=nltk.pos_tag(tokens)
        #TODO lemmatize nouns (any token whose POS tags starts with "N"): use WordNetLemmatizer()
        lemmatizer=WordNetLemmatizer()
        #TODO determine all noun lemmas and save it in self.noun_lemmas
        Noun_tags=['NN','NNP','NNPS','NNS']
        for token, tag in pos_tags:
            if tag in Noun_tags:
                lemma = lemmatizer.lemmatize(token, wordnet.NOUN)
                self.noun_lemmas.append(lemma)



    def hypernymOf(self,synset1, synset2):
        #TODO Is synset2 a hypernym of synset 1? (Or the same synset), return True or False
        if(synset1 == synset2):
            return True
        for hypernym in synset1.hypernyms():
            if synset2 == hypernym:
                return True
            if self.hypernymOf(hypernym,synset2):
                return True
        return False


    def get_hyponyms(self,hypernym):
        #TODO determine set of noun lemmas in ada_lovelace.txt that are hyponyms of the given hypernym

        list1 = []
        # list1 se la cac synsets cho moi lemma
        for lemma in self.noun_lemmas:
            lemma = lemma.lower()
            hypo = wordnet.synsets(hypernym)[0].hyponyms()
            lemma_syn= wordnet.synsets(lemma)[0]
            if lemma_syn in hypo:
                list1.append(lemma)
        return set(list1)
        # list1 = []
        # # list1 se la cac synsets cho moi lemma
        # for lemma in self.noun_lemmas:
        #     syn_lemma = wordnet.synsets(lemma)
        #     hype_lemma = syn_lemma.hypernyms().name()
        #     wanted_hype = hypernym.hypernyms().name()
        #     if (hype_lemma == wanted_hype):
        #         list1.append(lemma)
        # return set(list1)
        # list1=[]
        # # list1 se la cac synsets cho moi lemma
        # for lemma in self.noun_lemmas:
        #     synset = wordnet.synsets(lemma)
        #     print(synset)
        # for synset_1 in synset:
        #     syn_hyper=synset_1.hypernyms()
        #     print(syn_hyper)
        #
        # for w in syn_hyper:
        #     if(w == hypernym):
        #         list1.append(w)
        # print(list1)
        # return (list1)

        # # kiem tra synsets cua moi lemma == hypernym cua de bai hay k
        # list2=[]
        # for lemma_synset in list1:
        #         if(lemma_synset == hypernym.hypernym()):
        #             list2.append(lemma_synset)
        # return list2

def help_get_hyponyms(synset):
    hyponyms = set()
    for hyponym in synset.hyponyms():
          hyponyms |= set(help_get_hyponyms(hyponym))
    return hyponyms | set(synset.hyponyms())