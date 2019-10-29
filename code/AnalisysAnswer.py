#====================================================================
# Manipule Audio Inputs
# Author: Marcel Rebello
# mail: mprebello@gmail.com
# ====================================================================
import random
import marvin_quotes

class AnalisysAnswer(object):
    def __init__(self):
        self.__default_message = marvin_quotes.default
        #self.__default_message_init = marvin_quotes.default
        #self.__default_message_finish = marvin_quotes.default

    def first_answer(self):
        number = random.randint(1, 4)
        init = 'Init - {}'.format(number)
        return init

    def last_answer(self):
        number = random.randint(1, 4)
        last = 'Finish - {}'.format(number)
        last_answer = self.__loop_rules(last)
        return last_answer

    def verify(self, answer):
        row = self.__loop_rules(answer)
        if row != None:
            return row
        else:
            last_row = self.last_answer()
            return last_row

    def __loop_rules(self, answer):
        for row in self.__default_message:
            rule = row['Rule']
            if rule in answer:
                return row
        return None
