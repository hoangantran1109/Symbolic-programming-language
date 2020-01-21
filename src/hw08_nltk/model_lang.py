import nltk
from nltk.corpus import udhr

class LangModeler(object):
    def __init__(self, languages, words):
        self.languages = languages
        self.words = words

    def build_language_models(self):
        # TODO return ConditionalFrequencyDistribution of words in the UDHR corpus conditioned on each language
        # hint: use nltk.ConditionalFreqDist
        lang_base = dict()
        for lang in self.languages:
            lang_base[lang] = [word.lower() for word in udhr.words(lang + '-Latin1')]
            # print(udhr.words(lang+'-Latin1'))
        return nltk.ConditionalFreqDist((lang, word) for lang in self.languages for word in lang_base[lang])


    def guess_language(self,language_model_cfd, text):
        """Returns the guessed language for the given text"""

        #TODO for each language calculate the overall score of a given text
        #based on the frequency of words accessible by language_model_cfd[language].freq(word) and then
        #identify most likely language for a given text according to this score
        scores = []
        for lang in language_model_cfd.conditions():
            lang_score = 0
            for word in text.split():
                lang_score += language_model_cfd[lang].freq(word.lower())
            scores.append((lang, lang_score))  # (eng, 5)
        return sorted(scores, key=lambda x: x[1], reverse=True)[0][0]
#python -m unittest -v hw08_nltk/test_lang_guesser.py