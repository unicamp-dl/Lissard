# -*- coding: utf-8 -*-

from utils import Language, extract_lenght

class Spanish(Language):
    def __init__(self):
        self.COMMANDS = [
    "Repite 'hola mundo' 5 veces",
    "Repita la palabra 'perro' 4 veces, pero entre medias diga también 'auau'",
    "Repita 'el mundo entero' 7 veces y cada segunda vez agregue 'es un escenario'",
    "Di 'hambre' 3 veces, luego 'hipopótamo' dos veces y luego 'dame de comer' cuatro veces.",
    "Di 'python' 2 veces y 'datos' una vez y repite todo tres veces",
    "Repita 'gato' 5 veces. Después de cada vez, diga también 'ratón'.",
    "Repita 'nota inteira semínima semínima semínima' 2 vezes",
    "Repita la frase 'distrito administrativo' 3 veces y después de la segunda vez diga la frase 'hola mundo'",
    "Di 'hola mundo' 5 veces, pero no digas 'mundo' cada vez",
    "Hay 7 semillas en una sandía. Repite 'están deliciosas' una vez por cada semilla.",
    "mostrar los días laborables, pero sólo los fines de semana, 2 veces"
]
        
    def x_times_hello_word(self,times):
        '''
        Repeat 5 times hello world
        '''
        return str("hola mundo " * times).strip()

    def x_dog(self, times):
        '''
        Repita la palabra 'perro' 4 veces, pero entre medias diga también 'auau'
        '''
        half = times/2
        out = ''
        for x in range(0, (times+1)):
            if x == half:
                out+='auau '
            else:
                out+='perro '
        return out.strip()

    def x_cats(self, times):
        '''
        Repita 'gato' 5 veces. Después de cada vez, diga también 'ratón'.
        '''
        out = ''
        for x in range(0, (times)):
            out+='gato ratón '
        return out.strip()

    def x_hungry(self, times):
        '''
        Di 'hambre' 3 veces, luego 'hipopótamo' dos veces y luego 'dame de comer' cuatro veces.
        '''
        out = ''
        return " ".join(['hambre' for x in range(0, times)])+' hipopótamo hipopótamo dame de comer dame de comer dame de comer dame de comer'

    def x_all_the_world(self,times):
        '''
        Repita 'el mundo entero' 7 veces y cada segunda vez agregue 'es un escenario'
        '''
        out = ''
        count = 0
        range_ = int(times/2)
        for x in range(0, times+range_):
            if count == 2:
                out+='es un escenario '
                count=0
            else:
                out+='el mundo entero '
                count+=1
        return out.strip()


    def x_administrative_district(self, times):
        '''
        Repita la frase 'distrito administrativo' 3 veces y después de la segunda vez diga la frase 'hola mundo'
        '''
        out = ''
        count = 0
        for x in range(0, times+1):
            if count == 2:
                out+='hola mundo '
            else:
                out+='distrito administrativo '
            count+=1
        return out.strip()

    def x_note_quarter(self, times):
        '''
        repeat whole note quarter note quarter note quarter note twice
        '''
        return " ".join(["nota inteira semínima semínima semínima" for x in range(0, times)]).strip()


    def x_weekend_days(self, times):
        '''
        'Say the days of the week but only the weekend days, two times',
        '''
        return " ".join(["sábado domingo" for x in range(0, times)]).strip()

    def x_hello_world_not_say_world_every_even_time(self, times):
        '''
        Di 'hola mundo' 5 veces, pero no digas 'mundo' cada vez,
        '''
        out = ''
        count = 0
        for x in range(0, times):
            if count == 1:
                out+='hola '
                count=0
            else:
                out+='hola mundo '
                count+=1
        return out.strip()

    def x_say_python(self,times):
        '''
        Di 'python' 2 veces y 'datos' una vez y repite todo tres veces
        '''
        out = ''
        body = "".join(['python ' for x in range(0, (times))])+'datos '
        out = body*3
        return out.strip()

    def x_watermelon_seeds(self, times):
        '''
        Hay 7 semillas en una sandía. Repite 'están deliciosas' una vez por cada semilla.
        '''
        return " ".join(["están deliciosas" for x in range(0, times)]).strip()

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
            "Repite 'hola mundo' 5 veces":self.x_times_hello_word(times),
            "Repita la palabra 'perro' 4 veces, pero entre medias diga también 'auau'":self.x_dog(times),
            "Repita 'el mundo entero' 7 veces y cada segunda vez agregue 'es un escenario'":self.x_all_the_world(times),
            "Di 'hambre' 3 veces, luego 'hipopótamo' dos veces y luego 'dame de comer' cuatro veces.":self.x_hungry(times),
            "Di 'python' 2 veces y 'datos' una vez y repite todo tres veces":self.x_say_python(times),
            "Repita 'gato' 5 veces. Después de cada vez, diga también 'ratón'.":self.x_cats(times),
            "Repita 'nota inteira semínima semínima semínima' 2 vezes":self.x_note_quarter(times),
            "Repita la frase 'distrito administrativo' 3 veces y después de la segunda vez diga la frase 'hola mundo'":self.x_administrative_district(times),
            "Di 'hola mundo' 5 veces, pero no digas 'mundo' cada vez":self.x_hello_world_not_say_world_every_even_time(times),
            "Hay 7 semillas en una sandía. Repite 'están deliciosas' una vez por cada semilla.":self.x_watermelon_seeds(times),
            "mostrar los días laborables, pero sólo los fines de semana, 2 veces":self.x_weekend_days(times)
        }
        if sent_origin in MAP:
            return MAP[sent_origin]