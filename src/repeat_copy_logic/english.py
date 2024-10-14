# -*- coding: utf-8 -*-

from utils import Language, extract_lenght

class English(Language):
    def __init__(self):
        self.COMMANDS = ["A watermelon has 7 seeds. Repeat they're delicious once for every seed",
 'Output carbon pricing is an 4 times, but in the middle also say interesting concept',
 'Repeat 5 times hello world',
 'Repeat all the world 7 times, and after every second time add is a stage.',
 'Repeat cat 5 times. After each time, also say mouse',
 'Repeat the phrase the administrative district 3 times, and say the phrase hello world after the second time',
 'Repeat the word dog 4 times, but halfway through also say woof',
 "Say hello world 5 times, but don't say world every even time",
 'Say hungry 3 times, then hippo two times, then feed me four times',
 'Say python 2 and data once, and then repeat all of this three times.',
 'Say the days of the week but only the weekend days, 2 times',
 'repeat whole note quarter note quarter note quarter note 2 times']

    def x_times_hello_word(self, times):
        '''
        Repeat 5 times hello world
        '''
        return str("hello world " * times).strip()

    def x_dog(self, times):
        '''
        Repeat the word dog four times, but halfway through also say woof
        '''
        half = times/2
        out = ''
        for x in range(0, (times+1)):
            if x == half:
                out+='woof '
            else:
                out+='dog '
        return out.strip()

    def x_cats(self, times):
        out = ''
        for x in range(0, (times)):
            out+='cat mouse '
        return out.strip()

    def x_cats(self,times):
        '''
        Repeat cat five times. After each time, also say mouse
        '''
        out = ''
        for x in range(0, (times)):
            out+='cat mouse '
        return out.strip()

    def x_hungry(self,times):
        '''
        Say hungry three times, then hippo two times, then feed me four times
        '''
        out = ''
        return " ".join(['hungry' for x in range(0, times)])+' hippo hippo feed me feed me feed me feed me'

    def x_all_the_world(self,times):
        '''
        Repeat all the world seven times, and after every second time add is a stage.
        '''
        out = ''
        count = 0
        range_ = int(times/2)
        for x in range(0, times+range_):
            if count == 2:
                out+='is a stage '
                count=0
            else:
                out+='all the world '
                count+=1
        return out.strip()


    def x_administrative_district(self,times):
        '''
        repeat the phrase the administrative district three times, and say the phrase hello world after the second time
        '''
        out = ''
        count = 0
        for x in range(0, times+1):
            if count == 2:
                out+='hello world '
            else:
                out+='the administrative district '
            count+=1
        return out.strip()

    def x_inhabitants_in_the_urban_area(self,times):
        '''
        Twice repeat inhabitants in the urban area and then three times live in walking distance
        '''
        out = 'inhabitants in the urban area inhabitants in the urban area '
        return out+" ".join(["live in walking distance" for x in range(0, times)]).strip()

    def x_note_quarter(self,times):
        '''
        repeat whole note quarter note quarter note quarter note twice
        '''
        return " ".join(["whole note quarter note quarter note quarter note" for x in range(0, times)]).strip()

    def x_weekend_days(self,times):
        '''
        'Say the days of the week but only the weekend days, two times',
        '''
        return " ".join(["Saturday Sunday" for x in range(0, times)]).strip()

    def x_hello_world_not_say_world_every_even_time(self,times):
        '''
        'say hello world five times, but don't say world every even time',
        '''
        out = ''
        count = 0
        for x in range(0, times):
            if count == 1:
                out+='hello '
                count=0
            else:
                out+='hello world '
                count+=1
        return out.strip()

    def x_historic_church_building(self, times):
        '''
        Repeat historic church building twice, but after every word also say wow
        '''
        return " ".join(["historic wow church wow building wow" for x in range(0, times)]).strip()


    def x_say_python(self,times):
        '''
        say python twice and data once, and then repeat all of this three times.
        '''
        out = ''
        body = "".join(['python ' for x in range(0, (times))])+'data '
        out = body*3
        return out.strip()

    def x_the_school_of_music(self, times):
        '''
        Seven times please repeat The School of Music
        '''
        return " ".join(["The School of Music" for x in range(0, times)]).strip()

    def x_watermelon_seeds(self, times):
        '''
        A watermelon has seven seeds. Repeat they're delicious once for every seed
        '''
        return " ".join(["they're delicious" for x in range(0, times)]).strip()

    def x_carbon_pricing_is_ans(self, times):
        '''
        Output carbon pricing is an four times, but in the middle also say interesting concept
        '''
        half = times/2
        out = ''
        for x in range(0, (times+1)):
            if x == half:
                out+='interesting concept '
            else:
                out+='carbon pricing is an '
        return out.strip()

    def fill_output(self, sent_origin, sent_extra):
        times = extract_lenght(sent_extra)
        MAP = {
            "Repeat 5 times hello world":self.x_times_hello_word(times),
            "Repeat the word dog 4 times, but halfway through also say woof":self.x_dog(times),
            "Repeat all the world 7 times, and after every second time add is a stage.":self.x_all_the_world(times),
            "Say hungry 3 times, then hippo two times, then feed me four times":self.x_hungry(times),
            "Say python 2 and data once, and then repeat all of this three times.":self.x_say_python(times),
            "Repeat cat 5 times. After each time, also say mouse":self.x_cats(times),
            "repeat whole note quarter note quarter note quarter note 2 times":self.x_note_quarter(times),
            "Output carbon pricing is an 4 times, but in the middle also say interesting concept":self.x_carbon_pricing_is_ans(times),
            "Repeat the phrase the administrative district 3 times, and say the phrase hello world after the second time":self.x_administrative_district(times),
            "Say hello world 5 times, but don't say world every even time":self.x_hello_world_not_say_world_every_even_time(times),
            "A watermelon has 7 seeds. Repeat they're delicious once for every seed":self.x_watermelon_seeds(times),
            "Say the days of the week but only the weekend days, 2 times":self.x_weekend_days(times)
        }
        if sent_origin in MAP:
            return MAP[sent_origin]