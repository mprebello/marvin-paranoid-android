#====================================================================
# Manipule Audio Inputs
# Author: Marcel Rebello
# mail: mprebello@gmail.com
# ====================================================================
import random, marvin_quotes, marvin_rules

class AnalisysAnswer(object):
    def __init__(self):
        self.__default_sentences = marvin_quotes.default
        self.__default_rules = marvin_rules.default

    def verify(self, human_voice):
        self.__human_voice = human_voice
        rule = self.__testRule()
        catalog = self.__default_rules[rule]['CatalogSentence']
        action = self.__default_rules[rule]['Action']
        all_the_sentences = self.__default_sentences[catalog]
        sentence = self.__randomSentence(all_the_sentences)
        answer = [action, sentence]
        return answer

    def __randomSentence(self, all_the_sentences):
        min = 0
        max = len(all_the_sentences) -1
        random_number = random.randint(min, max)
        sentence = all_the_sentences[random_number]
        return sentence

    def __testRule(self):
        for rule in self.__default_rules:
            if rule in self.__human_voice:
                return rule

        return 'Default'
