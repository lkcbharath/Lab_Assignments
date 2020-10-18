import re
from nltk.stem import PorterStemmer
from nltk import WordNetLemmatizer

def split_punctuation(token_dict):
    new_token_dict = {}
    for filename, words in token_dict.items():
        new_string = " ".join(words)
        new_words = re.split(', |\?|\. |_|-|!|\s+', new_string)
        new_token_dict[filename] = new_words
    return new_token_dict

def lowercase(token_dict):
    new_token_dict = {}
    for filename, words in token_dict.items():
        new_words = [word.lower() for word in words]
        new_token_dict[filename] = new_words
    return new_token_dict

# List of stopwords fetched from https://gist.github.com/sebleier/554280
def stopword_removal(token_dict):
    new_token_dict = {}

    with open("gist_stopwords.txt", "r") as f:
        content = f.read()
        stopwords = set(content.split(","))

    for filename, words in token_dict.items():
        new_words = [word for word in words if word not in stopwords]
        new_token_dict[filename] = new_words
    
    return new_token_dict

# Remove [citiation needed], [(number)]
def wikipedia(token_dict):
    new_token_dict = {}

    wikipedia_stopwords = ["[citation", "needed]"]
    for filename, words in token_dict.items():
        new_words = [re.sub('\[([0-9])?([0-9])?([0-9])\]', '', word) for word in words]
        new_words = [word.replace("[citation", "").replace("needed]","") for word in new_words]
        new_token_dict[filename] = new_words
    
    return new_token_dict

def symbol_removal(token_dict):
    new_token_dict = {}

    for filename, words in token_dict.items():
        new_words = [re.sub(r"[^\w\d'\s]+", '', word) for word in words]
        new_token_dict[filename] = new_words
    
    return new_token_dict

def stemming(token_dict):
    new_token_dict = {}
    ps = PorterStemmer()

    for filename, words in token_dict.items():
        new_words = [ps.stem(word) for word in words]
        new_token_dict[filename] = new_words
    
    return new_token_dict

def lemmatization(token_dict):
    new_token_dict = {}
    wnl = WordNetLemmatizer()

    for filename, words in token_dict.items():
        new_words = [wnl.lemmatize(word) for word in words]
        new_token_dict[filename] = new_words
    
    return new_token_dict