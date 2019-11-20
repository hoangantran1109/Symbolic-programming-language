from nltk import FreqDist, word_tokenize
from collections import defaultdict
import os, math


def dot(dictA, dictB):
    """TODO: doctest for dot() go here. Ex.3.1 DONE
    >>> dot({'a':1,'b':2,'c':3},{'a':1,'b':2,'c':3})
    14
    >>> dot({'a':1,'b':2},{'a':1,'b':2,'c':3})
    5
    >>> dot({'a':1},{'a':1,'b':2,'c':3})
    1
    >>> dot({},{'a':1,'b':2,'c':3})
    0
    >>> dot({},{})
    0
    """
    return sum([dictA.get(tok) * dictB.get(tok, 0) for tok in dictA])


def normalized_tokens(text):
    """TODO: doctest for normalized_tokens() go here. Ex.3.1 DONE
    This takes a string and returns lower-case tokens, using nltk for tokenization.

    >>> normalized_tokens('Info Ma tik')
    ['info', 'ma', 'tik']
    >>> normalized_tokens('Py Charm')
    ['py', 'charm']
    >>> normalized_tokens('LMU')
    ['lmu']
    """
    return [token.lower() for token in word_tokenize(text)]

# TODO: Docstring documentation for all member functions (including constructors) Ex.3.2 DONE
"""
    This is a class for initialize string and dictionary for textdocuments. 
      
    Attributes: 
        text (string): a strinf of TextDocument. 
        id: an identifier of TextDocument. 
 
"""
class TextDocument:
    def __init__(self, text, id=None):
        """
                The constructor for TextDocument class.
                  This creates a TextDocument instance with a string, a dictionary and an identifier.
                Parameters:
                   text (string): a string.
                   token_counts : a dictionary
                   id : an identifier.
        """
        self.text = text
        self.token_counts = FreqDist(normalized_tokens(text))
        self.id = id

    @classmethod
    def from_file(cls, filename):
        """ This creates a TextDocument instance by reading a file.
        """
        with open(filename, 'r') as myfile:
            text = myfile.read().strip()
        return cls(text, filename)

# TODO: Docstring documentation for all member functions (including constructors) Ex.3.2
class DocumentCollection:
    def __init__(self, term_to_df, term_to_docids, docid_to_doc):
        # string to int
        self.term_to_df = term_to_df
        # string to set of string
        self.term_to_docids = term_to_docids
        # string to TextDocument
        self.docid_to_doc = docid_to_doc

    @classmethod
    def from_dir(cls, dir, file_suffix):
        """ Read documents (from directory)
        """
        files = [(dir + "/" + f) for f in os.listdir(dir) if f.endswith(file_suffix)]
        docs = [TextDocument.from_file(f) for f in files]
        return cls.from_document_list(docs)

    @classmethod
    def from_document_list(cls, docs):
        """Return (all) documents that contain (all) terms of a query
        """
        term_to_df = defaultdict(int)
        term_to_docids = defaultdict(set)
        docid_to_doc = dict()
        for doc in docs:
            docid_to_doc[doc.id] = doc
            for token in doc.token_counts.keys():
                term_to_df[token] += 1
                term_to_docids[token].add(doc.id)
        return cls(term_to_df, term_to_docids, docid_to_doc)

    def docs_with_all_tokens(self, tokens):
        docids_for_each_token = [self.term_to_docids[token] for token in tokens]
        docids = set.intersection(*docids_for_each_token)  # union?
        return [self.docid_to_doc[id] for id in docids]

    def tfidf(self, counts):
        """Reweight token frequencies by tf-idf weighting.
        """
        N = len(self.docid_to_doc)
        return {tok: tf * math.log(N / self.term_to_df[tok]) for tok, tf in counts.items() if tok in self.term_to_df}

    def cosine_similarity(self, docA, docB):
        """Compute cosine-similarity for two documents.
        """
        weightedA = self.tfidf(docA.token_counts)
        weightedB = self.tfidf(docB.token_counts)
        dotAB = dot(weightedA, weightedB)
        normA = math.sqrt(dot(weightedA, weightedA))
        normB = math.sqrt(dot(weightedB, weightedB))
        if(dotAB == 0): return 0
        return (dotAB) / (normA * normB)



# TODO: Docstring documentation for all member functions (including constructors) Ex.3.2
class SearchEngine:
    def __init__(self, doc_collection):
        self.doc_collection = doc_collection

    def ranked_documents(self, query):
        query_doc = TextDocument(query)
        query_tokens = query_doc.token_counts.keys()
        docs = self.doc_collection.docs_with_all_tokens(query_tokens)
        docs_sims = [(doc, self.doc_collection.cosine_similarity(query_doc, doc)) for doc in docs]
        return sorted(docs_sims, key=lambda x: -x[1])

    def snippets(self, query, document, window=50):
        tokens = normalized_tokens(query)
        text = document.text
        for token in tokens:
            start = text.lower().find(token.lower())
            if -1 == start:
                continue
            end = start + len(token)
            left = "..." + text[start - window:start]
            middle = "[" + text[start: end] + "]"
            right = text[end:end + window] + "..."
            yield left + middle + right

#python -m doctest -v hw04_text_search/text_vectors.py