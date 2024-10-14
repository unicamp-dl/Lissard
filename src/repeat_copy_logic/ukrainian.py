# -*- coding: utf-8 -*-

from utils import Language, extract_lenght

class Ukrainian(Language):
    def __init__(self):
        self.COMMANDS = [
    "Повторіть «Привіт Світ» 5 разів",
    "Повторіть слово «собака» 4 рази, але між ними також скажіть «auau»",
    "Повторіть «весь світ» 7 разів і кожного другого разу додайте «це етап»",
    "Скажіть «голодний» 3 рази, потім «бегемотик» двічі, потім «нагодуй мене» чотири рази.",
    "Скажіть «python» 2 рази і «дата» один раз і повторіть все тричі",
    "Повторіть «кішка» 5 разів. Після кожного разу також скажіть «мишка»",
    "Повторіть «вся нота чверть нота чверть» 2 рази",
    "Повторіть фразу «адміністративний район» 3 рази і після другого разу скажіть фразу «привіт світ»",
    "Скажіть «привіт світ» 5 разів, але не кажіть «світ» кожного разу",
    "У кавуні 7 насінин. Повторіть «вони смачні» один раз для кожного насіння.",
    "відображати будні, але тільки вихідні, 2 рази"
]

    def x_times_hello_word(self, times):
        '''
        Repeat 5 times hello world
        '''
        return str("Привіт Світ " * times).strip()

    def x_dog(self,times):
        '''
        Repeat the word dog four times, but halfway through also say woof
        '''
        half = times/2
        out = ''
        for x in range(0, (times+1)):
            if x == half:
                out+='auau '
            else:
                out+='собака '
        return out.strip()

    def x_cats(self, times):
        '''
        Repeat cat five times. After each time, also say mouse
        '''
        out = ''
        for x in range(0, (times)):
            out+='кішка мишка '
        return out.strip()

    def x_hungry(self,times):
        '''
        Say hungry three times, then hippo two times, then feed me four times
        '''
        return " ".join(['голодний' for x in range(0, times)])+' бегемотик бегемотик нагодуй мене нагодуй мене нагодуй мене нагодуй мене'

    def x_all_the_world(self,times):
        '''
        Repeat all the world seven times, and after every second time add is a stage.
        '''
        out = ''
        count = 0
        range_ = int(times/2)
        for x in range(0, times+range_):
            if count == 2:
                out+='це етап '
                count=0
            else:
                out+='весь світ '
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
                out+='привіт світ '
            else:
                out+='адміністративний район '
            count+=1
        return out.strip()

    def x_note_quarter(self,times):
        '''
        repeat whole note quarter note quarter note quarter note twice
        '''
        return " ".join(["вся нота чверть нота чверть" for x in range(0, times)]).strip()


    def x_weekend_days(self,times):
        '''
        'Say the days of the week but only the weekend days, two times',
        '''
        return " ".join(["Субота неділя" for x in range(0, times)]).strip()

    def x_hello_world_not_say_world_every_even_time(self,times):
        '''
        'say hello world five times, but don't say world every even time',
        '''
        out = ''
        count = 0
        for x in range(0, times):
            if count == 1:
                out+='привіт '
                count=0
            else:
                out+='привіт світ '
                count+=1
        return out.strip()

    def x_say_python(self,times):
        '''
        say python twice and data once, and then repeat all of this three times.
        '''
        out = ''
        body = "".join( ['python ' for x in range(0, (times))])+'дата '
        out = body*3
        return out.strip()

    def x_watermelon_seeds(self,times):
        '''
        A watermelon has seven seeds. Repeat they're delicious once for every seed
        '''
        return " ".join(["вони смачні" for x in range(0, times)]).strip()

    def fill_output(self, sent_origin, sent_extra):
        times = extract_lenght(sent_extra)
        MAP = {
            "Повторіть «Привіт Світ» 5 разів":self.x_times_hello_word(times),
            "Повторіть слово «собака» 4 рази, але між ними також скажіть «auau»":self.x_dog(times),
            "Повторіть «весь світ» 7 разів і кожного другого разу додайте «це етап»":self.x_all_the_world(times),
            "Скажіть «голодний» 3 рази, потім «бегемотик» двічі, потім «нагодуй мене» чотири рази.":self.x_hungry(times),
            "Скажіть «python» 2 рази і «дата» один раз і повторіть все тричі":self.x_say_python(times),
            "Повторіть «кішка» 5 разів. Після кожного разу також скажіть «мишка»":self.x_cats(times),
            "Повторіть «вся нота чверть нота чверть» 2 рази":self.x_note_quarter(times),
            "Повторіть фразу «адміністративний район» 3 рази і після другого разу скажіть фразу «привіт світ»":self.x_administrative_district(times),
            "Скажіть «привіт світ» 5 разів, але не кажіть «світ» кожного разу":self.x_hello_world_not_say_world_every_even_time(times),
            "У кавуні 7 насінин. Повторіть «вони смачні» один раз для кожного насіння.":self.x_watermelon_seeds(times),
            "відображати будні, але тільки вихідні, 2 рази":self.x_weekend_days(times)
        }
        if sent_origin in MAP:
            return MAP[sent_origin]
