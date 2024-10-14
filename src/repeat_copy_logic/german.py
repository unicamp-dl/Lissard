# -*- coding: utf-8 -*-

from utils import Language, extract_lenght

class German(Language):
    def __init__(self):
        self.COMMANDS = [
    "Wiederhole „Hallo Welt“ 5 Mal.",
    "Wiederholen Sie das Wort „Hund“ 4 Mal, sagen Sie aber auch zwischendurch „Wauwau“.",
    "Wiederholen Sie „die ganze Welt“ 7 Mal und fügen Sie jedes zweite Mal hinzu: „Es ist eine Bühne.“",
    "Sagen Sie 3 mal „hungrig“, dann zweimal „Hippo“ und dann viermal „Füttere mich“.",
    "Sagen Sie 2 mal „Python“ und einmal „Daten“ und wiederholen Sie alles dreimal",
    "Wiederholen Sie „Katze“ 5 mal. Sagen Sie nach jedem Mal auch „Maus“",
    "Wiederholen Sie „Ganze Note, Viertelnote, Viertelnote“ 2 mal",
    "Wiederholen Sie den Satz „Verwaltungsbezirk“ 3 mal und sagen Sie nach dem zweiten Mal den Satz „Hallo Welt“.",
    "Sagen Sie 5 mal „Hallo Welt“, aber sagen Sie nicht jedes Mal „Welt“.",
    "Eine Wassermelone enthält 7 Samen. Wiederholen Sie „Sie sind köstlich“ einmal für jeden Samen.",
    "Wochentage anzeigen, aber nur Wochenenden, 2 Mal"
]

    def x_times_hello_word(self,times):
        '''
        Repeat 5 times hello world
        '''
        return str("Hallo Welt " * times).strip()

    def x_dog(self,times):
        '''
        Repeat the word dog four times, but halfway through also say woof
        '''
        half = times/2
        out = ''
        for x in range(0, (times+1)):
            if x == half:
                out+='Wauwau '
            else:
                out+='Hund '
        return out.strip()

    def x_cats(self,times):
        '''
        Repeat cat five times. After each time, also say mouse
        '''
        out = ''
        for x in range(0, (times)):
            out+='Katze Maus '
        return out.strip()

    def x_hungry(self,times):
        '''
        Say hungry three times, then hippo two times, then feed me four times
        '''
        out = ''
        return " ".join(['hungrig' for x in range(0, times)])+' Hippo Hippo Füttere mich Füttere mich Füttere mich Füttere mich'

    def x_all_the_world(self,times):
        '''
        Repeat all the world seven times, and after every second time add is a stage.
        '''
        out = ''
        count = 0
        range_ = int(times/2)
        for x in range(0, times+range_):
            if count == 2:
                out+='Es ist eine Bühne '
                count=0
            else:
                out+='die ganze Welt '
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
                out+='Hallo Welt '
            else:
                out+='Verwaltungsbezirk '
            count+=1
        return out.strip()

    def x_note_quarter(self,times):
        '''
        repeat whole note quarter note quarter note quarter note twice
        '''
        return " ".join(["Ganze Note, Viertelnote, Viertelnote" for x in range(0, times)]).strip()


    def x_weekend_days(self,times):
        '''
        'Say the days of the week but only the weekend days, two times',
        '''
        return " ".join(["Samstag Sonntag" for x in range(0, times)]).strip()

    def x_hello_world_not_say_world_every_even_time(self,times):
        '''
        'say hello world five times, but don't say world every even time',
        '''
        out = ''
        count = 0
        for x in range(0, times):
            if count == 1:
                out+='Hallo '
                count=0
            else:
                out+='Hallo Welt '
                count+=1
        return out.strip()

    def x_say_python(self,times):
        '''
        say python twice and data once, and then repeat all of this three times.
        '''
        out = ''
        body = "".join(['python ' for x in range(0, (times))])+'Daten '
        out = body*3
        return out.strip()

    def x_watermelon_seeds(self,times):
        '''
        A watermelon has seven seeds. Repeat they're delicious once for every seed
        '''
        return " ".join(["Sie sind köstlich" for x in range(0, times)]).strip()

    def fill_output(self,sent_origin, sent_extra):
        times = extract_lenght(sent_extra)
        MAP = {
            "Wiederhole „Hallo Welt“ 5 Mal.":self.x_times_hello_word(times),
            "Wiederholen Sie das Wort „Hund“ 4 Mal, sagen Sie aber auch zwischendurch „Wauwau“.":self.x_dog(times),
            "Wiederholen Sie „die ganze Welt“ 7 Mal und fügen Sie jedes zweite Mal hinzu: „Es ist eine Bühne.“":self.x_all_the_world(times),
            "Sagen Sie 3 mal „hungrig“, dann zweimal „Hippo“ und dann viermal „Füttere mich“.":self.x_hungry(times),
            "Sagen Sie 2 mal „Python“ und einmal „Daten“ und wiederholen Sie alles dreimal":self.x_say_python(times),
            "Wiederholen Sie „Katze“ 5 mal. Sagen Sie nach jedem Mal auch „Maus“":self.x_cats(times),
            "Wiederholen Sie „Ganze Note, Viertelnote, Viertelnote“ 2 mal":self.x_note_quarter(times),
            "Wiederholen Sie den Satz „Verwaltungsbezirk“ 3 mal und sagen Sie nach dem zweiten Mal den Satz „Hallo Welt“.":self.x_administrative_district(times),
            "Sagen Sie 5 mal „Hallo Welt“, aber sagen Sie nicht jedes Mal „Welt“.":self.x_hello_world_not_say_world_every_even_time(times),
            "Eine Wassermelone enthält 7 Samen. Wiederholen Sie „Sie sind köstlich“ einmal für jeden Samen.":self.x_watermelon_seeds(times),
            "Wochentage anzeigen, aber nur Wochenenden, 2 Mal":self.x_weekend_days(times)
        }
        if sent_origin in MAP:
            return MAP[sent_origin]