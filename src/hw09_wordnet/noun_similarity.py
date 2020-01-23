import nltk
from itertools import combinations
from nltk.corpus import wordnet as wn
from collections import Counter
#python -m unittest -v hw09_wordnet/test_wordnet.py
def leave_odd_man_out(words):
    #TODO find the odd man in the list of words: use get_similarity_scores() method
    result = 1.0
    for w1 in words:
            if( w1 != words[0] ):
                test1 = get_similarity_scores([(w1,words[0])])
                for score in test1:
                    if(score[1] < result):
                        result=score[1]
    for w1 in words:
            if( w1 != words[0] ):
                test1 = get_similarity_scores([(w1,words[0])])
                for score in test1:
                    if(score[1] == result):
                        return w1












def get_similarity_scores(pairs):

    results = []

    for pair in pairs:

        max_score = 0.0
        max_line = () #should look like "('food-fruit', 0.1)"
        score = 0.0
        #TODO 1. iterate over all combinations of synsets formed by the synsets of the words in the word pair
        w1=pair[0]
        w2=pair[1]
        synset1= wn.synsets(w1)
        synset2 = wn.synsets(w2)
        for syn1 in synset1:
            for syn2 in synset2:
                # TODO 2. determine the maximum similarity score
               scores = [round(wn.path_similarity(syn1,syn2),1) if wn.path_similarity(syn1,syn2) != None else None]
               for score in scores:
                   if(score != None and score > max_score):
                       max_score=score
        # TODO 3. save max_line in results in form ("pair1-pair2", similarity_value) e.g.('car-automobile', 1.0)
        max_line = (w1 + '-' + w2, max_score)
        results.append(max_line)
    #TODO 4. return results in order of decreasing similarity
    results = sorted(results,key=lambda x:x[1])
    return results