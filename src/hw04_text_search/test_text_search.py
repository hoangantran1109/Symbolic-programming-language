import os
from unittest import TestCase

from hw04_text_search.text_vectors import TextDocument, DocumentCollection, SearchEngine


class DocumentCollectionTest(TestCase):

    def setUp(self):
        test_doc_list = [TextDocument(text_and_id[0], text_and_id[1]) for text_and_id in
                         [("the cat sat on a mat", "doc1"),
                          ("a rose is a rose", "doc2")]]
        self.small_collection = DocumentCollection.from_document_list(test_doc_list)

        #TODO: uncomment in case tests need access to whole document collection.
        this_dir = os.path.dirname(os.path.abspath(__file__))
        document_dir = os.path.join(this_dir, os.pardir, 'data/enron/enron1/ham/')
        self.large_collection = DocumentCollection.from_dir(document_dir, ".txt")

    def test_unknown_word_cosine(self):
        """ Return 0 if cosine similarity is called for documents with only out-of-vocabulary words. """
        # Document that only contains words that never occurred in the document collection.
        query_doc = TextDocument(text="unknownwords", id=None)
        # Some document from collection.
        collection_doc = self.small_collection.docid_to_doc["doc1"]
        # Similarity should be zero (instead of undefined).
        self.assertEqual(self.small_collection.cosine_similarity(query_doc, collection_doc), 0.)


class TextDocumentTest(TestCase):
    # TODO: Unittests for TextDocument go here. DONE
    def setUp(self):
        self.text = "Dr. Strangelove is the U.S. President's advisor."
    def test_from_file(self):
        doc1 = TextDocument.from_file("./hw04_text_search/example_document1.txt")
        token_set = set(doc1.token_counts)
        expected_token_set = {'dr.', 'strangelove', 'is', 'the', 'u.s.', 'president', \
                              "'s", 'advisor', '.'}
        self.assertEqual(token_set, expected_token_set)



class SearchEngineTest(TestCase):
    # TODO: Unittests for SearchEngine go here.

    def setUp(self):
        test_doc_list = [TextDocument(text_and_id[0], text_and_id[1]) for text_and_id in
                         [("the cat sat on a mat", "doc1"),
                          ("a rose is a rose", "doc2")]]
        self.small_collection = DocumentCollection.from_document_list(test_doc_list)
        self.my_searchEngine = SearchEngine(self.small_collection)
        # this_dir = os.path.dirname(os.path.abspath(__file__))
        # document_dir = os.path.join(this_dir, os.pardir, 'data/enron/enron1/ham/')
        # self.large_collection = DocumentCollection.from_dir(document_dir, ".txt")
        # self.my_searchEngine2 = SearchEngine(self.large_collection)
        # self.doc=self.large_collection.docs_with_all_tokens("New York")


        self.testdocument = TextDocument("the cat sat on a mat")



    def test_no_line_breaks(self):
        """ Make sure there are no newline characters in shown text snippets """
        someText = self.my_searchEngine.snippets("cat", self.testdocument, 50)
        self.assertFalse("\n" in someText)

    def test_remove_indentation_markers(self):
        """Remove the indentation markers of reply emails """
        someText = self.my_searchEngine.snippets("cat", self.testdocument, 50)
        self.assertNotIn("> > > >",someText)


