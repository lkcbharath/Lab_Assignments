import glob
import re 
from pathlib import Path
from collections import defaultdict
import preprocessor

def loader():
    filenames = glob.glob("./original_articles/*.txt")
    total_tokens = {}
    file_mapping = {}

    file_index = 1
    for filename in filenames:
        with open(filename, "r") as f:
            interim_tokens = []
            lines = f.readlines()
            for linex in lines:
                
                # Remove trailing newline
                line = linex.rstrip()
                
                words = line.split()
                #words = re.split(', |\?|\.|_|-|!|\s+', line)
                interim_tokens.extend(words)
            
            base_filename = Path(filename).stem
            total_tokens[base_filename] = interim_tokens
        file_mapping[base_filename] = file_index
        file_index += 1
            
    return [total_tokens, file_mapping]

# use dictionary
def construct_inverted_index(token_dict, document_index_mapping):
    inverted_index = defaultdict(set)
    for filename, words in token_dict.items():
        file_index = document_index_mapping[filename]
        for word in words:
            inverted_index[word].add(file_index)
    
    return inverted_index

def save_inverted_index_to_file(inverted_index,filename):
    with open(filename, "w") as f:
        for word, indice_set in inverted_index.items():
            indice_list = [str(x) for x in sorted(list(indice_set))]
            f.write(word + " : " + ", ".join(indice_list) + "\n")

def save_document_index_mapping_to_file(document_index_mapping):
    with open("document_index_mapping.txt", "w") as f:
        for filename, index in document_index_mapping.items():
            f.write(filename + " : " + str(index) + "\n")


def main():
    original_token_dict, document_index_mapping = loader()
    save_document_index_mapping_to_file(document_index_mapping)
    original_inverted_index = construct_inverted_index(original_token_dict, document_index_mapping)

    print("Number of tokens after initial loading:", len(original_inverted_index))

    split_punc_token_dict = preprocessor.split_punctuation(original_token_dict)
    split_punc_ii = construct_inverted_index(split_punc_token_dict, document_index_mapping)

    print("Number of tokens after splitting based on punctuation:", len(split_punc_ii))

    lowercase_token_dict = preprocessor.lowercase(split_punc_token_dict)
    lowercase_ii = construct_inverted_index(lowercase_token_dict, document_index_mapping)

    print("Number of tokens after making all tokens lowercase:", len(lowercase_ii))

    no_wikipedia_token_dict = preprocessor.wikipedia(lowercase_token_dict)
    no_wikipedia_ii = construct_inverted_index(no_wikipedia_token_dict, document_index_mapping)

    print("Number of tokens after removing Wikipedia noise:", len(no_wikipedia_ii))

    no_sym_token_dict = preprocessor.symbol_removal(no_wikipedia_token_dict)
    no_sym_ii = construct_inverted_index(no_sym_token_dict, document_index_mapping)

    print("Number of tokens after removing symbols:", len(no_sym_ii))

    no_stopword_token_dict = preprocessor.stopword_removal(no_sym_token_dict)
    no_stopword_ii = construct_inverted_index(no_stopword_token_dict, document_index_mapping)

    print("Number of tokens after removing stopwords:", len(no_stopword_ii))

    stemmed_token_dict = preprocessor.stemming(no_stopword_token_dict)
    stemmed_ii = construct_inverted_index(stemmed_token_dict, document_index_mapping)

    print("Finally,")
    print("1) Number of tokens after stemming all tokens:", len(stemmed_ii))

    save_inverted_index_to_file(stemmed_ii, "./inverted_indices/stemmed_inverted_index.txt")

    lemmatized_token_dict = preprocessor.lemmatization(no_stopword_token_dict)
    lemmatized_ii = construct_inverted_index(lemmatized_token_dict, document_index_mapping)

    print("2) Number of tokens after lemmatizing all tokens:", len(lemmatized_ii))

    save_inverted_index_to_file(lemmatized_ii, "./inverted_indices/lemmatized_inverted_index.txt")
    
        
if __name__ == '__main__':
    main()
