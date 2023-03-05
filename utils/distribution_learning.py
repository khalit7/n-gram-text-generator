'''
This file is NOT used, I wanted to implement the same model in a different way
for a 3-gram model, instead of estimating the propability P(A,B,C,D)/P(B,C,D), I wanted to experiment with estimating the propability P(B,C,D/A)*P(A)/P(B,C,D).
if you are reading this comment, it means I didn't finish this part :)
'''

# import numpy as np
# import constants as CONSTANTS

# from collections import defaultdict


# def create_co_occurance_matrix(data_itr,vocab,tokenizer):
    
#     n = len(vocab)
#     co_occurance_mat = np.zeros((n,n))
#     for x in data_itr:
#         tokens = tokenizer(x)
#         tokens.insert(0,"<SOS>")
#         tokens.append("<EOS>")
#         for i in range( len(tokens) ) :
#             middle_word_idx = vocab[ tokens[i] ]
#             left_end  = max(i-CONSTANTS.context_size,0)
#             right_end = min(i+CONSTANTS.context_size+1,len(tokens))
#             # iterate through context words and add their co-occurance with the middle word by 1
#             for t in tokens[left_end:i] + tokens[i+1:right_end]:
#                 context_word_idx = vocab[ t ]
#                 co_occurance_mat[middle_word_idx,context_word_idx]+=1
                
                
#     assert (co_occurance_mat.T == co_occurance_mat).all(),"Co occurance matrix is not symmetric for some reason :/ check your code"
#     # cap result
#     co_occurance_mat[co_occurance_mat>CONSTANTS.x_max_co_occurance] = CONSTANTS.x_max_co_occurance
#     # normalize to get a distribution
#     co_occurance_mat = co_occurance_mat/co_occurance_mat.sum(axis=1)
    
#     return co_occurance_mat.T


# def get_unigram_distribution(data_itr,vocab,tokenizer):
#     unigram_distrib = np.zeros(len(vocab))
#     num_of_sentences = 0
#     for x in data_itr:
#         num_of_sentences+=1
#         tokens = tokenizer(x)
        
#         for t in tokens:
#             unigram_distrib[ vocab[t] ] += 1
            
#     unigram_distrib[vocab["<SOS>"]] = num_of_sentences
#     unigram_distrib[vocab["<EOS>"]] = num_of_sentences
    
#     # cap counts
#     unigram_distrib[unigram_distrib>CONSTANTS.x_max_unigram] = CONSTANTS.x_max_unigram
#     # normalize to create a propability distribution
#     normalizer = sum(unigram_distrib)
#     unigram_distrib = unigram_distrib/normalizer

#     #assert unigram_distrib.sum() == 1, f"probabilities don't sum up to 1, they sum to {unigram_distrib.sum()} :/"
    
    
#     return unigram_distrib

# # def get_contextgram_distribution(data_itr,vocab,tokenizer):
    
# #     counter = defaultdict(int)
    
# #     for x in data_itr:
# #         tokens = tokenizer(x)
# #         if not tokens:
# #             continue
# #         adds_number = CONSTANTS.context_size - 1
# #         # add EOS
# #         tokens =  tokens + ["<EOS>"]*adds_number
# #         # add SOS
# #         tokens = ["<SOS>"]*adds_number + tokens
        
# #         for i in range(adds_number,len(tokens)):
# #             context = "_".join(tokens[i-adds_number:i+1])
# #             counter[context] += 1
            
# #     normalizer = sum(counter.values())
# #     for k,v in counter.items():
# #         counter[k] = v/normalizer

# #     return counter


# def get_prop_dist_given_context(context,unigram_dist,co_occurance):
    
#     vocab_size = len(unigram_dist)
#     log_cond_prop_dist = np.zeros(vocab_size)
    
#     for i in range(vocab_size):
#         unigram_prop = unigram_dist[i]
#         log_prop_of_context_given_word_i = 0
#         for c in context:
#             log_prop_of_context_given_word_i += np.log(1+co_occurance[i,c])
            
#         log_cond_prop_dist[i] = log_prop_of_context_given_word_i+ np.log(1+unigram_prop)
        
#     return (log_cond_prop_dist*-1) / (log_cond_prop_dist*-1).sum()

    
    
    
    
# def generate_text():
#     pass