
import random
from collections import defaultdict
from math import log2

def load_inverted_index(filename):
    inverted_index = defaultdict(lambda: defaultdict(lambda: 0))

    with open(filename, "r") as f:
        lines = f.readlines()
        for linex in lines:
            
            # Remove trailing newline
            line = linex.rstrip()
            
            token, index_string = line.split(" : ")
            word_list = index_string.split()
            for word_string in word_list:
                word_string_2 = word_string[1:-1]
                word_string_split = word_string_2.split(',')
                doc, freq = word_string_split[0], word_string_split[1]
                inverted_index[token][int(doc)] = int(freq)
            
    return inverted_index

def load_document_index_mapping(filename):
    document_index_mapping = []

    with open(filename, "r") as f:
        lines = f.readlines()
        document_index_mapping = [None for i in range(len(lines) + 1)]
        for linex in lines:
            
            # Remove trailing newline
            line = linex.rstrip()
            
            doc_name, doc_id = line.split(" : ")
            document_index_mapping[int(doc_id)] = doc_name
            
    return document_index_mapping

def save_token_mapping_to_file(token_mapping):
    with open("token_mapping.txt", "w") as f:
        for filename, index in token_mapping.items():
            f.write(filename + " : " + str(index) + "\n")

#mapping is tuple
def frequency_mapper(inverted_index):
    
    # Term Document Freq f(i,j)
    tdf_mapping = dict()
    
    # Unique Term Freq n(i)
    utf_mapping = dict()

    for token, doc_dict in inverted_index.items():
        for doc, freq in doc_dict.items():
            tdf_mapping[(token,doc)] = freq
        utf_mapping[token] = len(doc_dict.keys())

    return tdf_mapping, utf_mapping

def doc_tf_mapper(tdf_mapping):

    # Document length mapping
    doc_tf_mapping = defaultdict(lambda: 0)
    for doc_dict in tdf_mapping.values():
        for doc_id in doc_dict.keys():
            doc_tf_mapping[doc_id] += 1

    return doc_tf_mapping

def calculate_bm1_score(common_tokens, N, utf_mapping):
    bm1_score = 0.0

    for token in common_tokens:
        ni = utf_mapping[token]
        bm1_score += log2(N - ni + 0.5/ni + 0.5)

    return bm1_score

def calculate_bm15_score(common_tokens, chosen_doc_index, G_jq, tf_factor_mapping, tf_query_factor_mapping, N, utf_mapping):
    bm15_score = G_jq

    for token in common_tokens:
        ni = utf_mapping[token]
        token_doc_tuple = (token, chosen_doc_index)
        bm15_score += tf_factor_mapping[token_doc_tuple] * tf_query_factor_mapping[token] * log2((N - ni + 0.5) / (ni + 0.5))
    
    return bm15_score

def calculate_bm11_score(common_tokens, chosen_doc_index, G_jq, tf_factor_mapping_with_dln, tf_query_factor_mapping, N, utf_mapping):
    bm11_score = G_jq

    for token in common_tokens:
        ni = utf_mapping[token]
        token_doc_tuple = (token, chosen_doc_index)
        bm11_score += (tf_factor_mapping_with_dln[token_doc_tuple] * tf_query_factor_mapping[token] * log2((N - ni + 0.5) / (ni + 0.5)))
    
    return bm11_score

def calculate_simple_bm15_score(common_tokens, chosen_doc_index, K1, tdf_mapping, N, utf_mapping):
    bm15_score = 0.0

    for token in common_tokens:
        ni = utf_mapping[token]
        token_doc_tuple = (token, chosen_doc_index)
        fij = tdf_mapping[token_doc_tuple]

        bm15_score += (((K1 + 1) * fij) / (K1 + fij)) * log2((N - ni + 0.5) / (ni + 0.5))
    
    return bm15_score

def calculate_simple_bm11_score(common_tokens, chosen_doc_index, K1, tdf_mapping, len_dj, avg_doclen, N, utf_mapping):
    bm11_score = 0.0

    for token in common_tokens:
        ni = utf_mapping[token]
        token_doc_tuple = (token, chosen_doc_index)
        fij = tdf_mapping[token_doc_tuple]

        bm11_score += (((K1 + 1) * fij) / (((K1 * len_dj) / avg_doclen) + fij)) * log2((N - ni + 0.5) / (ni + 0.5))
    
    return bm11_score

def tf_bm25_mapper(tdf_mapping, K1, b, len_dj, avg_doclen):
    tf_bm25_mapping = dict()

    for token_doc_tuple, fij in tdf_mapping.items():
        Bij = ((K1 + 1) * fij) / ((K1 * ((1 - b) + (b * (len_dj/avg_doclen)))) + fij)
        tf_bm25_mapping[token_doc_tuple] = Bij
    
    return tf_bm25_mapping

def calculate_bm25_score(common_tokens, tf_bm25_mapping, chosen_doc_index, N, utf_mapping):
    bm25_score = 0.0

    for token in common_tokens:
        ni = utf_mapping[token]
        token_doc_tuple = (token, chosen_doc_index)
        Bij = tf_bm25_mapping[token_doc_tuple]

        bm25_score += Bij * log2((N - ni + 0.5) / (ni + 0.5))
    
    return bm25_score

def main():
    inverted_index = load_inverted_index("./inverted_indices/lemmatized_inverted_index.txt")
    document_index_mapping = load_document_index_mapping("document_index_mapping.txt")

    tokens = list(inverted_index.keys())
    token_mapping = defaultdict(lambda: 0)
    inverse_token_mapping = dict()
    for token_id in range(len(tokens)):
        token_str = tokens[token_id]
        token_mapping[token_str] = token_id + 1
        inverse_token_mapping[token_id + 1] = token_str
    #save_token_mapping_to_file(token_mapping)

    tdf_mapping, utf_mapping = frequency_mapper(inverted_index)

    doc_tokens_mapping = defaultdict(lambda: set())
    for token_str, doc_ind in tdf_mapping.keys():
        doc_tokens_mapping[doc_ind].add(token_str)

    # Number of documents
    N = 100

    # Number of terms in doc
    doc_tf_mapping = doc_tf_mapper(inverted_index)
    
    doc_lens = list(doc_tf_mapping.values())
    avg_doclen = sum(doc_lens)/len(doc_lens)

    # Query length
    query_len = 5

    tdf_values = list(tdf_mapping.values())

    # Get random query
    query_doc_tokens = random.sample(tokens, query_len)
    query_doc_token_freq_mapping = dict()

    # Frequency of terms in query
    for qdt in query_doc_tokens:
        query_doc_token_freq_mapping[qdt] = random.choice(tdf_values)
    
    print("Query Q: ")
    
    for qdt, fiq in query_doc_token_freq_mapping.items():
        print("(" + str(qdt) + ", " + str(fiq) + "), ", end='')
    print()

    # constants
    K1 = 3
    S1 = K1 + 1
    K2 = 1.4
    K3 = 100
    S3 = K3 + 1

    # F(i,j)
    tf_factor_mapping = dict()
    
    # F'(i,j) or F(i,j) with Document Length Normalization
    tf_factor_mapping_with_dln = dict()

    for token_doc_tuple, fij in tdf_mapping.items():
        tf_factor_mapping[token_doc_tuple] = (S1 * fij) / (K1 + fij)

        doc_id = token_doc_tuple[1]
        len_dj = doc_tf_mapping[doc_id]
        tf_factor_mapping_with_dln[token_doc_tuple] = (S1 * fij) / (((K1 * len_dj) / avg_doclen) + fij)

    # Correction Factor
    correction_factor_mapping = dict()
    for doc_id, len_dj in doc_tf_mapping.items():
        correction_factor_mapping[doc_id] = K2 * query_len * ((avg_doclen - len_dj) / (avg_doclen + len_dj))

    # Additional factor for Term Frequncies within Queries
    tf_query_factor_mapping = dict()
    for qdt, fiq in query_doc_token_freq_mapping.items():
        tf_query_factor_mapping[qdt] = (S3 * fiq) / (K3 + fiq)

    print("Original BM modelling:")
    print("Constant values:")
    print("K1: " + str(K1) + ", K2: " + str(K2) + ", K3: " + str(K3))
    print("Scores:")
    print("Document Chosen\t\t\t\tBM1\t\t\tBM11\t\t\tBM15")
    
    for chosen_doc_index in range(1,101):

        chosen_doc_tokens = doc_tokens_mapping[chosen_doc_index]

        # Get intersection of the query and document
        common_tokens = set(query_doc_tokens).intersection(chosen_doc_tokens)

        G_jq = correction_factor_mapping[chosen_doc_index]

        # Initial scores
        bm1_score = calculate_bm1_score(common_tokens, N, utf_mapping)
        bm11_score = calculate_bm11_score(common_tokens, chosen_doc_index, G_jq, tf_factor_mapping_with_dln, tf_query_factor_mapping, N, utf_mapping)
        bm15_score = calculate_bm15_score(common_tokens, chosen_doc_index, G_jq, tf_factor_mapping, tf_query_factor_mapping, N, utf_mapping)
        
        print(str(document_index_mapping[chosen_doc_index][0:30] + ".txt").ljust(40) + str(bm1_score).ljust(20) + "\t" + str(bm11_score).ljust(20) + "\t" + str(bm15_score).ljust(20))

    print()
    
    # Constants for simplified calculation
    simple_K1 = 1.2

    print("Simplified BM modelling:")
    print("Constant values:")
    print("K1: " + str(simple_K1) + ", K2: 0, K3: inf")
    print("Scores:")
    print("Document Chosen\t\t\t\tBM1\t\t\tBM11\t\t\tBM15")

    for chosen_doc_index in range(1,101):
        chosen_doc_tokens = doc_tokens_mapping[chosen_doc_index]
        common_tokens = set(query_doc_tokens).intersection(chosen_doc_tokens)

        len_dj = doc_tf_mapping[chosen_doc_index]

        # Simplified scores
        # Simple BM1 same as original BM1
        simple_bm1_score = calculate_bm1_score(common_tokens, N, utf_mapping)
        simple_bm11_score = calculate_simple_bm11_score(common_tokens, chosen_doc_index, simple_K1, tdf_mapping, len_dj, avg_doclen, N, utf_mapping)
        simple_bm15_score = calculate_simple_bm15_score(common_tokens, chosen_doc_index, simple_K1, tdf_mapping, N, utf_mapping)
        
        print(str(document_index_mapping[chosen_doc_index][0:30] + ".txt").ljust(40) + str(simple_bm1_score).ljust(20) + "\t" + str(simple_bm11_score).ljust(20) + "\t" + str(simple_bm15_score).ljust(20))

    print()

    
    print("BM25 Modelling:")

    # Constants for BM25
    b = 0.2
    bm25_K1 = 1.3

    # B(i,j)
    tf_bm25_mapping = tf_bm25_mapper(tdf_mapping, bm25_K1, b, len_dj, avg_doclen)    

    print("With b: " + str(b) + " and K1: " + str(bm25_K1) + ", scores:")
    print("Document Chosen\t\t\t\tBM25")

    for chosen_doc_index in range(1,101):
        chosen_doc_tokens = doc_tokens_mapping[chosen_doc_index]
        common_tokens = set(query_doc_tokens).intersection(chosen_doc_tokens)
        bm25_score = calculate_bm25_score(common_tokens, tf_bm25_mapping, chosen_doc_index, N, utf_mapping)

        print(str(document_index_mapping[chosen_doc_index][0:30] + ".txt").ljust(40) + str(bm25_score).ljust(20))

    print()

    # Similar procedure for second case
    b_1 = 0.8
    bm25_K1_1 = 1.8
    tf_bm25_mapping_1 = tf_bm25_mapper(tdf_mapping, bm25_K1_1, b_1, len_dj, avg_doclen)

    print("With b: " + str(b_1) + " and K1: " + str(bm25_K1_1) + ", scores:")
    print("Document Chosen\t\t\t\tBM25")

    for chosen_doc_index in range(1,101):
        chosen_doc_tokens = doc_tokens_mapping[chosen_doc_index]
        common_tokens = set(query_doc_tokens).intersection(set(chosen_doc_tokens))
        bm25_score = calculate_bm25_score(common_tokens, tf_bm25_mapping_1, chosen_doc_index, N, utf_mapping)

        print(str(document_index_mapping[chosen_doc_index][0:30] + ".txt").ljust(40) + str(bm25_score).ljust(20))

if __name__ == '__main__':
    main()