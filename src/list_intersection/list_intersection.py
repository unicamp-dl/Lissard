# -*- coding: utf-8 -*-
'''
Script to generate dataset of "Find Intersection" Task 

'''
import os
import argparse
import random
import glob
import pandas as pd
import zipfile
import requests
from itertools import product
from tqdm import tqdm

LANGUAGES = ['en','pt','es','de','ru','ua']

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

def sample_a_b_list(words=None, len_words=2):
  list_a = random.sample(words, len_words)
  aux_b = [w for w in words if w not in list_a]
  list_b = random.sample(aux_b, len_words)
  return list_a, list_b


def build_intersection(list_a, list_b, len_words=2):
  lens = [i for i in range(0, (len_words+1))]
  inter_fac = random.choice(lens)

  if inter_fac == 0:
    return list_a, list_b, [str(None)], inter_fac
  if inter_fac == len_words:
    return list_a, list_a, list_a, inter_fac
  list_aux = random.sample(list_a, inter_fac)
  len_list_b = len_words - len(list_aux)
  intersection = random.sample(list_b, len_list_b) + list_aux
  random.shuffle(intersection)
  return list_a, intersection, list_aux, inter_fac

def build_dataset(list_words, max_sample, max_lenght):

  if max_lenght >= len(list_words):
    max_lenght = len(list_words)

  dataset = {'input':[],'out':[], 'len':[], 'total_inter':[],'A':[], 'B':[]}
  compose_lens = [l for l in range(2, (max_lenght+2))]
  for i in range(0,max_sample):
    len_ = random.choice(compose_lens)
    list_words_a, list_words_b = sample_a_b_list(words=list_words,len_words=len_)
    list_a_first, list_b_second, true_out, number_inter = build_intersection(list_words_a, list_words_b,len_words=len_)

    dataset['input'].append(f'A: {"/".join(list_a_first).strip()}\nB: {"/".join(list_b_second).strip()}')
    dataset['A'].append("/".join(list_a_first).strip())
    dataset['B'].append("/".join(list_b_second).strip())

    dataset['out'].append(" ".join(true_out).strip())
    dataset['len'].append(len_)
    dataset['total_inter'].append(number_inter)
  return pd.DataFrame(dataset)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Arguments used to generate Find Intersection Task")

    parser.add_argument(
        "--max_samples", default=300, help="Total number of samples"
    )

    parser.add_argument(
        "--max_len",
        default=180,
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
      all_words_lang = pd.read_csv(f'freq_words/{lang}.csv')

      df = build_dataset(list_words=all_words_lang['word'].to_list(),
                        max_sample=int(args.max_samples), max_lenght=int(args.max_len))

      df['bins'] = extract_bins(df, int(args.max_bins), 'len')

      # if you would like to sample stratified
      # where "total_sample_by_bin" is the number of samples that must be in each bin
      #df = df.groupby('bins', group_keys=False).apply(lambda x: x.sample(min(len(x), total_sample_by_bin)))
      df.to_csv(args.output_path+lang+'_find_intersection_'+str(len(df))+'.csv', index=False)
    print('Done!')
