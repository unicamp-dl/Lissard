# -*- coding: utf-8 -*-

class Language():
    def __init__(self):
        self.COMMANDS = []

def extract_lenght(sentence):
  return int("".join(list(filter(str.isdigit, sentence))))