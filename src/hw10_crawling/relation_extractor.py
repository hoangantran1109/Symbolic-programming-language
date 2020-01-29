import nltk

#python -m unittest -v hw10_crawling/test_spaCy.py

import spacy

class RelationExtractor(object):

    def __init__(self, path, nlp):
        self.nlp = nlp
        #TODO read text as a string and tokenize it by sentences
        file=open(path,encoding="utf8").read()
        self.sentences = nltk.sent_tokenize(file) #TODO replace -> create the list of sentences from the file


    def entities_and_nounChunks(self,doc):
        #TODO extract all entities and noun phrases and save them into one list
        Ent = [ent for ent in doc.ents]
        Noun_chunks = [noun_chunks for noun_chunks in doc.noun_chunks]
        return (Ent + Noun_chunks)


    def update_tokenizer(self,spans):
        #TODO make from entities and noun chunks a single token
        # Ent_for_st = [span.ents for span in spans]
        # for span in spans:
        #     Noun_chunks_for_st=[noun_chunks for noun_chunks in span.noun_chunks]
        # return (Ent_for_st+[Noun_chunks_for_st])
        get_sort_key = lambda span: (span.end - span.start, -span.start)
        sorted_spans = sorted(spans, key=get_sort_key, reverse=True)
        result = []
        seen_tokens = set()
        for span in sorted_spans:
            # Check for end - 1 here because boundaries are inclusive
            if span.start not in seen_tokens and span.end - 1 not in seen_tokens:
                result.append(span)
            seen_tokens.update(range(span.start, span.end))
        result = sorted(result, key=lambda span: span.start)
        return result





    def extract_money_relations(self,doc):
        #TODO extract the noun phrases and MONEY items they refer to
        relations = [] #holds the noun phrase and MONEY item it refers to (e.g. [("Net income", "$6.4 million"),...])
        # 1. iterate over tokens in the given sentence (entities and noun phrases are a single token now)
        spans = list(doc.ents) + list(doc.noun_chunks)
        spans = self.update_tokenizer(spans)

        with doc.retokenize() as retokenizer:
            for span in spans:
                retokenizer.merge(span)

        # 2. check if entity type is MONEY
        for money in filter(lambda w: w.ent_type_ == "MONEY", doc):
            # 3. check if MONEY is attribute (attr)
            if money.dep_ in ("attr", "dobj"):
                # 4. find noun phrase for this attr (should be of type nsubj (nominal subject))
                subject = [w for w in money.head.lefts if w.dep_ == "nsubj"]
                if subject:
                    subject = subject[0]
                    # 5. save this relation in a list "relations"
                    relations.append((subject, money))
                    # 6. check if MONEY is a preposition object (pobj) and its head is a prepositional modifier (prep)
                    # 7. find noun phrase for this pobj (which is the head of the prepositional modifier)
            elif money.dep_ == "pobj" and money.head.dep_ == "prep":
                # 8. save also this relation in a list "relations"
                relations.append((money.head.head, money))
        return relations

    def extract_relations(self):
        #TODO extract relations from text
        relations_in_text = []
        #1. iterate over self.sentences
        for sentence in self.sentences:
        #2. convert each sentence in a spaCy object
            a=self.nlp(sentence)
        #3. extract entities and nounChunks
            b=self.entities_and_nounChunks(a)
        #4. update tokenizer
            c=self.update_tokenizer(b)
        #5. extract money relations in each sentence
            d=self.extract_money_relations(a)
            relations_in_text.append(d)
        #6. save the list with relations in a list "relations_in_text"
        return relations_in_text
