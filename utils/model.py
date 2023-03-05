from collections import defaultdict
import time
import random
from random import choices

class NgramModel():
    
    def __init__(self,n,data_itr,tokenizer):
        self.n = n
        self.data_itr = data_itr
        self.tokenizer = tokenizer
        self.n_gram_counter,self.context_counter,self.vocab = self.get_models_params()
        
    
    def get_models_params(self):
        
        n_gram_counter  = defaultdict(int)
        context_counter = defaultdict(int)
        vocab = set()
        for x in self.data_itr:
            tokens = self.tokenizer(x)
            if not tokens:
                continue
            tokens = self.n*["<SOS>"] + tokens
            tokens =  tokens + ["<EOS>"]
            vocab.add("<SOS>")
            vocab.add("<EOS>")
            for i in range(self.n,len(tokens)):
                context = tuple(tokens[i-self.n:i])
                curr_word = tokens[i]
                
                vocab.add(curr_word)
                context_counter[(context,curr_word)] +=1
                n_gram_counter[context] +=1
                
                
                
        return n_gram_counter,context_counter,vocab
    
    
    def generate_text(self,starting_text="",max_words=50,print_as_you_generate=True):
        
        if print_as_you_generate:
            print(starting_text,end=" ",flush=True)
            
        text = starting_text
        dist = {}
        for i in range(max_words):
            tokens = self.tokenizer(text)
            if len(tokens) < self.n:
                num_of_sos = self.n - len(tokens)
                tokens = self.n*["<SOS>"] + tokens

            context = tokens[-self.n:]
            for v in self.vocab:
                if self.n_gram_counter[tuple(context)] == 0:
                    dist[v] = 0
                else:
                    dist[v] = self.context_counter[(tuple(context),v)]/ self.n_gram_counter[tuple(context)]
                    
            try:
                generated_word = " ".join( choices(list(dist.keys()),list(dist.values())) )
            except:
                generated_word = " ".join( random.sample(list(self.vocab),1) )
            if print_as_you_generate:
                # add some random delay to make it look cool
                time.sleep(random.uniform(0.1, 0.3)) # sleep beetween 0.2 and 0.9 seconds
                print(generated_word,end=" ",flush=True)
                
            text += f" {generated_word}"
            
        return text
            