# -*- coding: utf-8 -*-
'''
Script to generate dataset of "Last Letter concat" Task 

'''
import glob
import os
import random
import requests
import argparse
import zipfile
from tqdm import tqdm
import pandas as pd
from typing import List, Tuple
import pandas as pd
import inflect  # using inflect==5.3.0

LANGUAGES = {
"EN":["Liam","Olivia","Noah","Emma","Oliver","Charlotte","James","Amelia","Elijah","Sophia","Mateo","Mia",
"Theodore","Isabella","Henry","Ava","Lucas","Evelyn","William","Luna","Benjamin","Harper","Levi","Sofia","Sebastian","Camila",
"Jack","Eleanor","Ezra","Elizabeth","Michael","Violet","Daniel","Scarlett","Leo","Emily","Owen","Hazel",
"Samuel","Lily","Hudson","Gianna","Alexander","Aurora","Asher","Penelope","Luca","Aria",
"Ethan","Nora","John","Chloe","David","Ellie","Jackson","Mila","Joseph","Avery","Mason","Layla","Luke","Abigail","Matthew","Ella",
"Julian","Isla","Dylan","Eliana","Elias","Nova","Jacob","Madison","Maverick","Zoe","Gabriel","Ivy","Logan","Grace","Aiden","Lucy",
"Thomas","Willow","Isaac","Emilia","Miles","Riley","Grayson","Naomi","Santiago","Victoria"],
"PT":["Maria","Jose","Ana","Joao", "Antonio", "Francisco", "Carlos", "Paulo", "Pedro", "Lucas", "Luiz",
          "Marcos", "Luis", "Gabriel","Rafael","Francisca","Daniel","Marcelo","Bruno", "Eduardo","Antonia",
          "Adriana","Juliana","Marcia","Fernanda","Patricia","Aline","Sandra","Camila","Amanda","Bruna","Jessica",
          "Leticia","Julia", "Luciana", "Vanessa", "Mariana"],
"ES":["Maria","Antonio","Manuel","Jose","Francisco","Carmen","Juan","Javier",
          "Carlos","Alejandro","Jesus","Isabel","Josefa","Miguel","Jose","Marta","Pablo",
          "Lucia","Angel","Sergio","Fernando","Jorge","Antonia","Alberto","Dolores","Paula","Alvaro"],
"DE":["Sabine","Susanne","Petra","Monika","Birgit","Stefanie","Karin","Anna",
          "Anja","Angelika","Martina","Brigitte","Heike","Katharina","Kerstin","Ute",
          "Ulrike","Bettina","Jutta","Bärbel","Ivonne","Thomas","Stefan","Hans","Klaus","Jan",
          "Wolfgang","Matthias","Jürgen","Bernd","Markus","Thorsten","Uwe","Jens","Jörg","Ralph",
          "Sven","Rainer","Manfred","Dirk","Philipp","Joachim"],
"RU":["иванов","иванова", "смирнова", "петров", "смирнов", "кузнецова", "кузнецов", "васильева", "петрова", "попов", "александръ", "александр", "серьгей", "сергейъ","сергей","сeргей","андрей","алексей", "дмиьтрий","дмитьрий","элена", "еленаъ", "елена", "оьлга","ольга", "олга", "анна", "ъирина", "ирина", "анастасия"],
"UA":["Злата", "Соломія", "Софія", "Емілія", "Мілана", "Меланія", "Уляна", "Єва", "Дарина",
          "Ангеліна", "Діана", "Анна", "Яна", "Мія", "Аліна", "Вікторія", "Олександра", "Аріна",
          "Єлизавета", "Анастасія", "Христина", "Вероніка", "Стефанія", "Заріна", "Квітослава",
          "Лея", "Еліна", "Естер", "Агата", "Суламіта", "Есфір", "Таїсія", "Аделіна",
          "Орися", "Ярина", "Емма", "Еріка", "Даяна", "Есмі", "Тіна", "Барбара", "Анісія",
          "Анелія", "Еліс", "Сарра", "Наомі", "Олівія", "Розалія", "Рахіль", "Магдалина",
          "Матвій", "Марк", "Макар", "Дмитро", "Денис", "Максим", "Даниїл", "Давид", "Данило",
          "Владислав", "Олександр", "Тимофій", "Арсен", "Ярослав", "Павло", "Назар", "Андрій",
          "Лука", "Роман", "Богдан", "Артем", "Нестор", "Захар", "Ярема", "Амір", "Яків",
          "Єфрем", "Єремія", "Тадей", "Левій", "Мартін", "Авенір","Тиміш", "Самуїл", "Міран",
          "Северин", "Ян", "Георгій", "Ельдар", "Лукас", "Аскольд", "Лео", "Леонард", "Алан",
          "Веремій", "Гордій", "Асаф", "Сінан", "Рамазан", "Леві", "Тальха", "Тім", "Еней",
          "Ілай", "Рувим", "Алім", "Тімур", "Лєтті"]
}

def build_names_set(min_len = 2,max_len=30,  size=500, name_list=[]):
  lenghts = [i for i in range(min_len, max_len)]
  samples_set = {'input':[], 'out':[], 'len':[]}

  for idx in range(0, size):
    if type(lenghts) is list:
      sample_names  = random.choices(name_list, k=random.choices(lenghts, k=1)[0])
    else:
      sample_names  = random.choices(name_list, k=min_len)
    samples_set['input'].append(' '.join(sample_names))
    samples_set['out'].append(''.join([list(item)[-1] for item in sample_names]))
    samples_set['len'].append(len(sample_names))
  return pd.DataFrame(samples_set)

def save(path, name, sub_set):
  pd.DataFrame(sub_set).to_csv(path+name+'.csv', index=None, header=False)


def check_bin(bins, sample):
  for bin_ in bins:
    if sample >= (bin_[0]) and sample < (bin_[1]):
      return str(bin_[0])+'~'+str(bin_[1])
  return False

def extract_bins(df, bins, colun_lens):
  # Determine the bin edges for the 10 bins based on min and max of 'len_input'
  bin_edges = pd.cut(df[colun_lens], bins=bins, retbins=True, include_lowest=True)[1]

  # Plotting the results
  bin_centers = [(bin_edges[i] + bin_edges[i+1]) / 2 for i in range(len(bin_edges) - 1)]
  bin_centers = [[int(bin_edges[i]),int(bin_edges[i+1])] for i in range(len(bin_edges)-1)]
  bin_centers[-1][-1]+=1
  bin_target = []
  for sample in df[colun_lens].to_list():
    bin_target.append(check_bin(bin_centers, sample))
  return bin_target

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Arguments used to generate Last Letter Concat Task")

    parser.add_argument(
        "--max_samples", default=12000,help="Total number of samples"
    )

    parser.add_argument(
        "--max_len",
        default=30,
        help="Maximum number of elements",
    )

    parser.add_argument(
        "--max_bins",
        default=4,
        help="Total number of bins that should be partitioned in the dataset",
    )

    parser.add_argument(
        "--output_path",
        required=True,
        help="folder to save files",
    )

    args = parser.parse_args()

    for lang in LANGUAGES:

      df_lens = build_names_set(min_len = 2,max_len=int(args.max_len), 
                                size = int(args.max_samples),  name_list=LANGUAGES[lang])
      df_lens = df_lens.drop_duplicates()
      #set bins
      df_lens['bins'] = extract_bins(df_lens, int(args.max_bins), 'len')

      # if you would like to sample stratified
      # where "total_sample_by_bin" is the number of samples that must be in each bin
      #df = df.groupby('bins', group_keys=False).apply(lambda x: x.sample(min(len(x), total_sample_by_bin)))
      df_lens.to_csv(args.output_path+lang+'_last_letter_concat_'+str(len(df_lens))+'.csv', index=False)

    print('Done!')
