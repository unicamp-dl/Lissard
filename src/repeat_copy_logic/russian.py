# -*- coding: utf-8 -*-

from utils import Language, extract_lenght

class Rusian(Language):
    def __init__(self):
        self.COMMANDS = ['Повтори 5 раз «привет мир»',
'Повтори слово «собака» 4 раза, но на полпути также скажи «гав»',
'Повторите «весь мир» 7 раз и после каждого второго раза добавляйте «это сцена»',
'Скажите «голодный» 3 раза, затем два раза «бегемот», затем четыре раза «накорми меня»',
'Скажи "python" 2 раза и "данные" один раз, а затем повтори все это три раза',
'Повторите «кошка» 5 раз. После каждого раза также произносите «мышь»',
'Повторите «целую ноту четвертную ноту четвертную ноту четвертную ноту» 2 раз',
'Выведите «цена на выбросы углерода» 4 раза, но в середине также напишите «интересная концепция»',
'Повторите фразу «административный район» 3 раза и после второго раза произнесите фразу «привет мир»',
"Скажите «привет мир» 5 раз, но не говорите «мир» каждый четный раз",
"В арбузе 7 семян. Повторите «Они вкусные» один раз для каждого семечка",
"вывести дни недели, но только выходные дни, 2 раза"]

    def x_times_hello_word(self,times):
        '''
        Repeat 5 times hello world
        '''
        return str("привет мир " * times).strip()

    def x_dog(self,times):
        '''
        Repeat the word dog four times, but halfway through also say woof
        '''
        half = times/2
        out = ''
        for x in range(0, (times+1)):
            if x == half:
                out+='гав '
            else:
                out+='собака '
        return out.strip()

    def x_cats(self,times):
        '''
        Repeat cat five times. After each time, also say mouse
        '''
        out = ''
        for x in range(0, (times)):
            out+='кошка мышь '
        return out.strip()

    def x_hungry(self,times):
        '''
        Say hungry three times, then hippo two times, then feed me four times
        '''
        return " ".join(['голодный' for x in range(0, times)])+' бегемот бегемот накорми меня накорми меня накорми меня накорми меня'

    def x_all_the_world(self,times):
        '''
        Repeat all the world seven times, and after every second time add is a stage.
        '''
        out = ''
        count = 0
        range_ = int(times/2)
        for x in range(0, times+range_):
            if count == 2:
                out+='это сцена '
                count=0
            else:
                out+='весь мир '
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
                out+='привет мир '
            else:
                out+='административный район '
            count+=1
        return out.strip()

    def x_note_quarter(self,times):
        '''
        repeat whole note quarter note quarter note quarter note twice
        '''
        return " ".join(["целую ноту четвертную ноту четвертную ноту четвертную ноту" for x in range(0, times)]).strip()


    def x_weekend_days(self,times):
        '''
        'Say the days of the week but only the weekend days, two times',
        '''
        return " ".join(["Суббота Воскресенье" for x in range(0, times)]).strip()

    def x_hello_world_not_say_world_every_even_time(self, times):
        '''
        'say hello world five times, but don't say world every even time',
        '''
        out = ''
        count = 0
        for x in range(0, times):
            if count == 1:
                out+='привет '
                count=0
            else:
                out+='привет мир '
                count+=1
        return out.strip()

    def x_say_python(self,times):
        '''
        say python twice and data once, and then repeat all of this three times.
        '''
        out = ''
        body = "".join(['python ' for x in range(0, (times))])+'данные '
        out = body*3
        return out.strip()

    def x_watermelon_seeds(self,times):
        '''
        A watermelon has seven seeds. Repeat they're delicious once for every seed
        '''
        return " ".join(["Они вкусные" for x in range(0, times)]).strip()

    def x_carbon_pricing_is_ans(self, times):
        '''
        Output carbon pricing is an four times, but in the middle also say interesting concept
        '''
        half = times/2
        out = ''
        for x in range(0, (times+1)):
            if x == half:
                out+='интересная концепция '
            else:
                out+='цена на выбросы углерода '
        return out.strip()

    def fill_output(self,sent_origin, sent_extra):
        times = extract_lenght(sent_extra)
        MAP = {
            "Повтори 5 раз «привет мир»":self.x_times_hello_word(times),
            "Повтори слово «собака» 4 раза, но на полпути также скажи «гав»":self.x_dog(times),
            "Повторите «весь мир» 7 раз и после каждого второго раза добавляйте «это сцена»":self.x_all_the_world(times),
            "Скажите «голодный» 3 раза, затем два раза «бегемот», затем четыре раза «накорми меня»":self.x_hungry(times),
            'Скажи "python" 2 раза и "данные" один раз, а затем повтори все это три раза':self.x_say_python(times),
            "Повторите «кошка» 5 раз. После каждого раза также произносите «мышь»":self.x_cats(times),
            "Повторите «целую ноту четвертную ноту четвертную ноту четвертную ноту» 2 раз":self.x_note_quarter(times),
            "Выведите «цена на выбросы углерода» 4 раза, но в середине также напишите «интересная концепция»":self.x_carbon_pricing_is_ans(times),
            "Повторите фразу «административный район» 3 раза и после второго раза произнесите фразу «привет мир»":self.x_administrative_district(times),
            "Скажите «привет мир» 5 раз, но не говорите «мир» каждый четный раз":self.x_hello_world_not_say_world_every_even_time(times),
            "В арбузе 7 семян. Повторите «Они вкусные» один раз для каждого семечка":self.x_watermelon_seeds(times),
            "вывести дни недели, но только выходные дни, 2 раза":self.x_weekend_days(times)
        }
        if sent_origin in MAP:
            return MAP[sent_origin]