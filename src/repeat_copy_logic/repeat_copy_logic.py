# -*- coding: utf-8 -*-
'''
Script to generate dataset of "Repeat Copy Logic" Task 

'''
import re
import argparse
import pandas as pd
import inflect
import random
from english import English
from german import German
from portuguese import Portuguese
from spanish import Spanish
from russian import Rusian
from ukrainian import Ukrainian

LANGUAGES = {
  'EN':English(),
  'DE':German(),
  'PT':Portuguese(),
  'ES':Spanish(),
  'RU':Rusian(),
  'UA':Ukrainian()
}

p = inflect.engine()


def build_extrapolation(sentence):
  extract_value = re.search(r'\b5|4|2|7|3|6\b',sentence).group()
  replace_int = [value for value in range(0, 10+2*20, 2)][2:]
  samples = [sentence.replace(extract_value, str(extrapolation_value)) for extrapolation_value in replace_int]

  return samples

def build_extrapolation_by_len(sentence, extrapolation_val):
  # print('SENTENCE: ',sentence)
  extract_value = re.search(r'\b5|4|2|7|3|6\b',sentence).group()
  extrapolation_sent = sentence.replace(extract_value, str(extrapolation_val))
  return extrapolation_sent


def build_dataset_max_lenght(total_samples, lang_obj=None, max_lengh=52):
  dataset = {"input_origin":[],"input_extrapolation":[], 'output':[], 'len':[]}

  lenghts = [i for i in range(2, max_lengh)]
  for i in range(0, total_samples):
    command = random.choice(lang_obj.COMMANDS)
    lenght = random.choice(lenghts)
    input_extrapolation = build_extrapolation_by_len(command, lenght)

    dataset['input_origin'].append(command)
    dataset['input_extrapolation'].append(input_extrapolation)
    dataset['len'].append(lenght)
    dataset['output'].append(lang_obj.fill_output(command, input_extrapolation).lower())
  return pd.DataFrame(dataset)

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

    parser = argparse.ArgumentParser(description="Arguments used to generate Vowel Grouping Task")

    parser.add_argument(
        "--max_samples", default=300, help="Total number of samples"
    )

    parser.add_argument(
        "--max_len",
        default=34,
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
      print('Language: ', lang)
      df = build_dataset_max_lenght(args.max_samples, lang_obj=LANGUAGES[lang], max_lengh=args.max_len)
      df = df.drop_duplicates(subset='input_extrapolation')

      # print('total samples: ', len(df))
      df['bins'] = extract_bins(df, int(args.max_bins), 'len')


      # if you would like to sample stratified
      # where "total_sample_by_bin" is the number of samples that must be in each bin
      #df = df.groupby('bins', group_keys=False).apply(lambda x: x.sample(min(len(x), total_sample_by_bin)))
      df.to_csv(args.output_path+lang+'_repeat_copy_logic_'+str(len(df))+'.csv', index=False)
    print('Done!')
