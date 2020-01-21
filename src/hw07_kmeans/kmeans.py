import string

import nltk
import numpy as np
import random

class Reader:

    def __init__(self, path):
        self.path = path
        self.punctuation = set(string.punctuation)
        self.courses = self.get_lines()
        self.vocabulary = self.get_vocabulary()
        self.vector_spaced_data = self.data_to_vectorspace()

    def get_lines(self):
        #TODO return list of courses from file

        with open(self.path, "r") as f:
         return [l[:-1] for l in f.readlines()]

    def normalize_word(self,word):
        #TODO normalize word by lower casing and deleting punctuation from word
        #TODO use set of punctuation symbols self.punctuation
        # s = word
        # for c in self.punctuation:
        #     s = s.replace(c, "")
        # return print(s.lower())

        for el in self.punctuation:
            word=word.replace(el,'')
        return word.lower()

    def get_vocabulary(self):
        #TODO return list of unique words from file and sort them alphabetically
        vocab = []
        for course in self.courses:
            words = course.split()
            for word in words:
                n_word = self.normalize_word(word)
                if n_word not in vocab and len(n_word) > 0:
                    vocab.append(n_word)
        return sorted(vocab)

    def vectorspaced(self,course):
        #TODO represent course by one-hot vector: vector filled with 0s, except for a 1 at the position associated with word in vocabulary
        #TODO length of vector should be equal vocabulary size
        return [int(word in self.normalize_word(course)) for word in self.vocabulary]
        # course_toks=[self.normalize_word(token) for token in nltk.word_tokenize(course)]
        # return [1 if item in course_toks else 0 for item in self.vocabulary]

    def data_to_vectorspace(self):
        return [self.vectorspaced(course) for course in self.courses if course]

class Kmeans:
    """performs k-means clustering"""

    def __init__(self, k):
        self.k = k
        self.means = None

    def distance(self, x,y):
        #TODO calculate Euclidean distance between two vectors x and y
        # dists=[]
        # for i in range(len(x)):
        #     dists.append(x[i]-y[i])
        # dists=[x**2 for x in dists]
        # return np.sqrt(sum(dists))
        return np.sqrt(sum([(x[i]-y[i])**2 for i in range(len(x))]))
        #return np.linalg.norm(np.array(x)-np.array(y))
    def classify(self,input):
        #TODO calculate Euclidean distances between input and the means and return the mean index with min distance
        # distance=[(self.distance(self.means[i],input),i) for i in range(len(self.k))]
        # return sorted(distance)[0][1]
        #
        return min(range(self.k),key=lambda i:self.distance(input,self.means[i]))

    def vector_mean(self,vectors):
        #TODO calculate mean of the list of vectors
        return list(np.mean(vectors,axis=0))

    def train(self, inputs):
        # choose k random points as the initial means
        self.means = random.sample(inputs, self.k)#step 1

        #uncomment the following line and use the given means for the unittest
        #self.means = [inputs[32], inputs[67], inputs[46]]

        assignments = None
        iter = 0
        while iter != 100:
            # find new assignments
            assignments = list(map(self.classify, inputs))

            # compute new means based on the new assignments
            for i in range(self.k):
                # find all the points assigned to cluster i
                i_points = [p for p, a in zip(inputs,assignments) if a == i]
                if i_points:
                    # make sure i_points is not empty so don't divide by 0
                    self.means[i] = self.vector_mean(i_points)
            iter += 1
