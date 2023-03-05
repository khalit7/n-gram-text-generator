import sys
sys.path.append("utils")
import os

import dataset
import model
import constants as CONSTANTS



if __name__ == '__main__':
    tokenizer = dataset._get_tokenizer()
    data_itr  = dataset._get_data_itr("train")
    
    n = CONSTANTS.context_size
    print(f"Creating the {n}_gram_model ... (change the number of grams by editing the context_size in the config.yaml)",end=" ",flush=True)
    n_gram_model = model.NgramModel(n,data_itr,tokenizer)
    print("Done!")
    
    while True:
        
        starting_text = input("write the starting text:  ")
        n_gram_model.generate_text(starting_text = starting_text)
        print()
        print()
        input("Press anything to try again .... ")
        os.system('clear')