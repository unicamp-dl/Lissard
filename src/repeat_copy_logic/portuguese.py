# -*- coding: utf-8 -*-

from utils import Language, extract_lenght

class Portuguese(Language):
    def __init__(self):
        self.COMMANDS = [
    "Repita 'olá mundo' 5 vezes",
    "Repita a palavra 'cachorro' 4 vezes, mas no meio diga também 'auau'",
    "Repita 'o mundo inteiro' 7 vezes e a cada segunda vez adicione 'é um palco'",
    "Diga 'com fome' 3 vezes, depois 'hipopótamo' duas vezes e depois 'alimente-me' quatro vezes.",
    "Diga 'python' 2 vezes e 'dados' uma vez e repita tudo três vezes",
    "Repita 'gato' 5 vezes. Depois de cada vez diga também 'rato'",
    "Repita 'nota inteira semínima semínima semínima' 2 vezes",
    "Repita a frase 'distrito administrativo' 3 vezes e após a segunda vez diga a frase 'olá mundo'",
    "Diga 'olá mundo' 5 vezes, mas não diga 'mundo' todas as vezes pares",
    "Existem 7 sementes em uma melancia. Repita 'eles são deliciosos' uma vez para cada semente.",
    "exibir dias da semana, mas apenas fins de semana, 2 vezes"
]
    def x_times_hello_word(self,times):
        '''
        Repeat 5 times hello world
        '''
        return str("Olá Mundo " * times).strip()

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
                out+='cachorro '
        return out.strip()

    def x_cats(self,times):
        '''
        Repeat cat five times. After each time, also say mouse
        '''
        out = ''
        for x in range(0, (times)):
            out+='gato rato '
        return out.strip()

    def x_hungry(self, times):
        '''
        Say hungry three times, then hippo two times, then feed me four times
        '''
        out = ''
        return " ".join(['com fome' for x in range(0, times)])+' hipopótamo hipopótamo alimente-me, alimente-me, alimente-me, alimente-me'

    def x_all_the_world(self,times):
        '''
        Repeat all the world seven times, and after every second time add is a stage.
        '''
        out = ''
        count = 0
        range_ = int(times/2)
        for x in range(0, times+range_):
            if count == 2:
                out+='é um palco '
                count=0
            else:
                out+='o mundo inteiro '
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
             out+='olá mundo '
            else:
                out+='distrito administrativo '
            count+=1
        return out.strip()

    def x_note_quarter(self,times):
        '''
        repeat whole note quarter note quarter note quarter note twice
        '''
        return " ".join(["nota inteira semínima semínima semínima" for x in range(0, times)]).strip()


    def x_weekend_days(self, times):
        '''
        'Say the days of the week but only the weekend days, two times',
        '''
        return " ".join(["sábado domingo" for x in range(0, times)]).strip()

    def x_hello_world_not_say_world_every_even_time(self,times):
        '''
        'say hello world five times, but don't say world every even time',
        '''
        out = ''
        count = 0
        for x in range(0, times):
            if count == 1:
                out+='olá '
                count=0
            else:
                out+='olá mundo '
                count+=1
        return out.strip()

    def x_say_python(self, times):
        '''
        say python twice and data once, and then repeat all of this three times.
        '''
        out = ''
        body = "".join(['python ' for x in range(0, (times))])+'dados '
        out = body*3
        return out.strip()

    def x_watermelon_seeds(self, times):
        '''
        A watermelon has seven seeds. Repeat they're delicious once for every seed
        '''
        return " ".join(["eles são deliciosos" for x in range(0, times)]).strip()

    def x_carbon_pricing_is_ans(self, times):
        '''
        Output carbon pricing is an four times, but in the middle also say interesting concept
        '''
        half = times/2
        out = ''
        for x in range(0, (times+1)):
            if x == half:
                out+='conceito interessante '
            else:
                out+='preço do carbono '
        return out.strip()

    def fill_output(self, sent_origin, sent_extra):
        times = extract_lenght(sent_extra)
        MAP = {
            "Repita 'olá mundo' 5 vezes":self.x_times_hello_word(times),
            "Repita a palavra 'cachorro' 4 vezes, mas no meio diga também 'auau'":self.x_dog(times),
            "Repita 'o mundo inteiro' 7 vezes e a cada segunda vez adicione 'é um palco'":self.x_all_the_world(times),
            "Diga 'com fome' 3 vezes, depois 'hipopótamo' duas vezes e depois 'alimente-me' quatro vezes.":self.x_hungry(times),
            "Diga 'python' 2 vezes e 'dados' uma vez e repita tudo três vezes":self.x_say_python(times),
            "Repita 'gato' 5 vezes. Depois de cada vez diga também 'rato'":self.x_cats(times),
            "Repita 'nota inteira semínima semínima semínima' 2 vezes":self.x_note_quarter(times),
            "Repita a frase 'distrito administrativo' 3 vezes e após a segunda vez diga a frase 'olá mundo'":self.x_administrative_district(times),
            "Diga 'olá mundo' 5 vezes, mas não diga 'mundo' todas as vezes pares":self.x_hello_world_not_say_world_every_even_time(times),
            "Existem 7 sementes em uma melancia. Repita 'eles são deliciosos' uma vez para cada semente.":self.x_watermelon_seeds(times),
            "exibir dias da semana, mas apenas fins de semana, 2 vezes":self.x_weekend_days(times)
        }
        if sent_origin in MAP:
            return MAP[sent_origin]