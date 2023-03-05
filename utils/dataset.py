from torchtext.datasets import WikiText2
from torchtext.data import get_tokenizer

import numpy as np

import constants as CONSTANTS


def _get_data_itr (split):
    
    data_itr = WikiText2(split=split)
    
    return data_itr

def _get_tokenizer():
    
    return get_tokenizer("basic_english")