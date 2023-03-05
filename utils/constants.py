import yaml
with open("config.yaml", 'r') as stream:
    config = yaml.safe_load(stream)



context_size = config["context_size"]
x_max_unigram= config["x_max_unigram"]
x_max_co_occurance= config["x_max_co_occurance"]