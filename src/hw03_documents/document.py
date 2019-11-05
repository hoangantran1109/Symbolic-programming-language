import os

import nltk
nltk.download('punkt')
def normalized_tokens(text):
    """ This takes a string and returns lower-case tokens, using nltk for tokenization. """
    # TODO: return list with lower-case tokens.*DONE
    token = nltk.word_tokenize(text)
    return [t.lower() for t in token]

class TextDocument:

    def __init__(self, text, id=None ):
        """ This creates a TextDocument instance with a string, a dictionary and an identifier. """
        self.text = text
        self.word_to_count = {token:normalized_tokens(text).count(token) for token in normalized_tokens(text)} # TODO: Create dictionary that maps words to their counts.*DONE
        self.id = id

    @classmethod
    def from_file(cls, filename):
        """ This creates a TextDocument instance by reading a file. """

        text = "" # TODO: read text from filename*DONE
        filename = os.path.abspath(filename)
        with open(filename, mode='r',encoding="utf-8") as f:
            for text in f.readlines():
                print(text, end='')
        return cls(text, filename)

    def __str__(self):
        """ This returns a short string representation, which is at most 25 characters long.
        If the original text is longer than 25 characters, the last 3 characters of the short string should be '...'.
        """
         # TODO: Implement correct return statement.*DONE
        return str((self.text[:22] + '...') if len(self.text) > 24 else self.text)

    def word_overlap(self, other_doc):
        """ This returns the number of words that occur in both documents (self and other_doc) at the same time.
        Every word should be considered only once, irrespective of how often it occurs in either document (i.e. we
        consider word *types*).
        """
        a = set(normalized_tokens(self.text))
        b = set(normalized_tokens(other_doc))
        return len(list(a&b))
"""python -m unittest hw03_documents\test_documents.py
"""