# -*- coding: utf-8 -*-
'''
Script adapted from the Object Countig task via BIG-bench
> https://github.com/google/BIG-bench/blob/main/bigbench/benchmark_tasks/object_counting/generate_task.py

'''
import json
import random
import argparse
from typing import List, Tuple
import pandas as pd
import inflect  # using inflect==5.3.0

COUNT = {'an':1 ,
         'a':1,
         "two":2,
         "three":3,
         "four":4,
         "five":5}

DATA = {
    "animals": [
        "cat", "rabbit", "donkey", "dog", "mouse", "cow", "snake", "fish",
        "bear", "snail", "chicken", "pig", "duck", "goat", "frog"
    ],
    "objects": [
        "car", "chair", "couch", "table", "bed", "lamp", "microwave", "oven",
        "stove", "fridge", "toaster"
    ],
    "vegetables": [
        "carrot", "head of broccoli", "cabbage", "yam", "garlic", "cauliflower",
        "lettuce head", "stalk of celery", "potato", "onion"
    ],
    "musical instruments": [
        "violin", "trumpet", "flute", "clarinet", "drum", "piano", "trombone",
        "accordion"
    ],
    "fruits": [
        "strawberry", "banana", "grape", "peach", "orange", "apple",
        "blackberry", "plum", "nectarine", "raspberry"
    ],
}

p = inflect.engine()

def get_counting_word(word: str, number: int) -> str:
  is_vowel = word[0] in "aeiou"
  article = "an" if is_vowel else "a"
  return [article, "two", "three", "four", "five"][number - 1]


def add_and(items: List[str]) -> List[str]:
  items[-1] = "and " + items[-1]


def add_count(items: List[str]) -> int:
  counts = {}

  for i in range(len(items)):
    word = items[i]
    number = random.choices([1, 2, 3, 4, 5], weights=[80, 10, 6, 3, 1])[0]
    counting_word = get_counting_word(word, number)
    word = p.plural(word, number)

    items[i] = f"{counting_word} {word}"
    counts[items[i]] = number

  return sum(counts.values())


def add_decoy(items: List[str], exclude_kind: str) -> List[str]:
  k = random.randint(1, 3)
  kind = random.choice([kind for kind in DATA if kind != exclude_kind])
  new_items = random.sample(DATA[kind], k)
  add_count(new_items)
  new_items.extend(items)
  random.shuffle(new_items)
  return new_items


def make_example() -> Tuple[str, str]:
  k = random.randint(2, 10)
  kind = random.choice(list(DATA))
  items = random.sample(DATA[kind], min(len(DATA[kind]), k))
  count = add_count(items)
  if random.random() > 0.75 and kind != "objects":
    items = add_decoy(items, kind)
  add_and(items)
  items = ", ".join(items)
  return (f"I have {items}. How many {kind} do I have?",
          (p.number_to_words(count), str(count)))

def read_json(path):
  with open(path) as json_file:
      data = json.load(json_file)
  return data

def get_output(target_output):
  return target_output[1]

def count_objects(sentence):
  tokens = sentence.split(' ')
  count=0
  for token in tokens:
    if token != 'and':
      if token in COUNT.keys():
        count+=COUNT[token]
  return count

def remove_query(sentence):
  sentence = sentence.split('How many')
  return sentence[0].strip()

def build_dataset(examples):
  dataset_ = {'input':[], 'target':[]}
  for item in examples:
    input_ = item[0]
    dataset_['input'].append(remove_query(input_))
    dataset_['target'].append(count_objects(input_))
  df_ = pd.DataFrame(dataset_)
  df_ = df_.drop_duplicates()
  return df_

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

    def ranged_type(value_type, min_value, max_value):
        """
        Return function handle of an argument type function for ArgumentParser checking a range:
            min_value <= arg <= max_value

        Parameters
        ----------
        value_type  - value-type to convert arg to
        min_value   - minimum acceptable argument
        max_value   - maximum acceptable argument

        Returns
        -------
        function handle of an argument type function for ArgumentParser


        Usage
        -----
            ranged_type(float, 0.0, 1.0)

        """

        def range_checker(arg: str):
            try:
                f = value_type(arg)
            except ValueError:
                raise argparse.ArgumentTypeError(f'must be a valid {value_type}')
            if f < min_value or f > max_value:
                raise argparse.ArgumentTypeError(f'must be within [{min_value}, {max_value}]')
            return f

        # Return function handle to checking function
        return range_checker
    parser = argparse.ArgumentParser(description="Arguments used to generate Object Couting Task")

    parser.add_argument(
        "--max_samples", required=True, help="Total number of samples"
    )

    parser.add_argument(
        "--max_len",
        required=True,
        help="Maximum number of elements",
    )

    parser.add_argument(
        "--max_bins",
        required=True,
        type=ranged_type(int, 2, 30),
        help="Total number of bins that should be partitioned in the dataset",
    )

    parser.add_argument(
        "--output_path",
        required=True,
        help="folder to save files",
    )

    args = parser.parse_args()

    examples = [make_example() for _ in range(int(args.max_samples)+100)]
    examples = list(set(examples))[:int(args.max_samples)]
    df = build_dataset(examples)
    df['bins'] = extract_bins(df, int(args.max_bins), 'target')
    # if you would like to sample stratified
    # where "total_sample_by_bin" is the number of samples that must be in each bin
    #df = df.groupby('bins', group_keys=False).apply(lambda x: x.sample(min(len(x), total_sample_by_bin)))
    df.to_csv(args.output_path+'object_countig_dataset_'+str(len(df))+'.csv', index=False)
    print('Done!')
