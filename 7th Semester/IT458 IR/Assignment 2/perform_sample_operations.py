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
            #print(index_string)
            #index_set = 

            #inverted_index[token] = index_set
            
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

#mapping is tuple
def frequency_mapper(inverted_index):
    
    # Term Document Freq
    tdf_mapping = dict()
    
    # Unique Term Freq
    utf_mapping = dict()

    for token, doc_dict in inverted_index.items():
        for doc, freq in doc_dict.items():
            tdf_mapping[(token,doc)] = freq
        utf_mapping[token] = len(doc_dict.keys())
    
    return tdf_mapping, utf_mapping

def calculate_tf_idf_scores(tf_type, K, idf_type, tdf_mapping,utf_mapping,no_of_docs):
    tf_mapping = dict()
    idf_mapping = dict()

    #max token frequncy per doc
    mdf_mapping = defaultdict(lambda: 0)

    token_doc_tuples = tdf_mapping.keys()

    if tf_type == 1:
        for token_doc_tuple, freq in tdf_mapping.items():
            doc = token_doc_tuple[1]
            mdf_mapping[doc] = max(mdf_mapping[doc],freq)
    
    for token_doc_tuple, freq in tdf_mapping.items():
        
        # Log normalization
        if tf_type == 0:
            tf_mapping[token_doc_tuple] = 1 + log2(freq)
        
        # double normalization K
        elif tf_type == 1:
            doc = token_doc_tuple[1]
            tf_mapping[token_doc_tuple] = K + (1 - K) * (freq/mdf_mapping[doc])
        
    for token, no_of_app in utf_mapping.items():

        # inv freq smooth
        if idf_type == 0:
            idf_mapping[token] = log2(1 + (no_of_docs/no_of_app))

        # probablisitc inv freq
        elif idf_type == 1:
            idf_mapping[token] = log2((no_of_docs-no_of_app)/no_of_app)

    tf_idf_mapping = dict()
    for token_doc_tuple in token_doc_tuples:
        token = token_doc_tuple[0]
        tf_idf_mapping[token_doc_tuple] = tf_mapping[token_doc_tuple] * idf_mapping[token]
    
    return tf_idf_mapping

def generate_document_corpus(tf_idf_mapping, no_of_docs):
    document_corpus = [defaultdict(lambda: 0.0) for _ in range(no_of_docs + 1)]
    for token_doc_tuple, tf_idf_score in tf_idf_mapping.items():
        token, doc = token_doc_tuple[0], token_doc_tuple[1]
        document_corpus[doc][token] = tf_idf_score
    
    return document_corpus

def vsm_doc_string(token_dict, token_mapping):
    doc_string = ""
    for token, tf_idf_score in token_dict.items():
        token_string = str(round(tf_idf_score,2)) + "T" + str(token_mapping[token]) + " + "
        doc_string += token_string
    doc_string = doc_string[:-3]
    return doc_string

def vsm_doc_string_2(token_dict):
    doc_string = ""
    for token_id, tf_idf_score in token_dict.items():
        token_string = str(round(tf_idf_score,2)) + "T" + str(token_id) + " + "
        doc_string += token_string
    doc_string = doc_string[:-3]
    return doc_string

def save_document_corpus_to_file(document_corpus, document_index_mapping, token_mapping, no_of_docs):
    with open("document_corpus.txt", "w") as f:
        for doc_id in range(1, no_of_docs + 1):
            token_dict = document_corpus[doc_id]
            doc_string = vsm_doc_string(token_dict, token_mapping)
            f.write(document_index_mapping[doc_id] + " : " + doc_string + "\n\n")

def save_token_mapping_to_file(token_mapping):
    with open("token_mapping.txt", "w") as f:
        for filename, index in token_mapping.items():
            f.write(filename + " : " + str(index) + "\n")

# Using cosine similarity
def generate_ranking(query, document_corpus, inverse_token_mapping):
    doc_corp_len = len(document_corpus)
    cos_sim_values = [0 for i in range(doc_corp_len)] 
    for doc_id in range(1, doc_corp_len):
        doc_vsm = document_corpus[doc_id]
        weight_prod = 0.0
        weight_sum_1 = sum([pow(x,2) for x in doc_vsm.values()])
        weight_sum_2 = sum([pow(x,2) for x in query.values()])
        for token_id, token_qweight in query.items():
            token_name = inverse_token_mapping[token_id]
            if token_name in doc_vsm:
                weight_prod += token_qweight * doc_vsm[token_name]
        
        cos_sim_values[doc_id] = weight_prod / (pow(weight_sum_1*weight_sum_2,0.5))
    
    return cos_sim_values

def rank_doc_ids(cos_sim_values, doc_id_list):
    zipped_pairs = zip(cos_sim_values, doc_id_list)
    ranked_doc_ids = [x for _, x in sorted(zipped_pairs) if _ > 0.0]
    ranked_doc_ids.reverse()
    ranked_doc_ids = ranked_doc_ids[:-1]
    return ranked_doc_ids

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
    save_token_mapping_to_file(token_mapping)

    tdf_mapping, utf_mapping = frequency_mapper(inverted_index)
    token_doc_tuples = list(tdf_mapping.keys())


    K = 0.7
    no_of_docs = 100

    # TF-IDF 1
    tf_type = 0
    idf_type = 0
    tf_idf_mapping_1 = calculate_tf_idf_scores(tf_type,K,idf_type,tdf_mapping,utf_mapping,no_of_docs)
    
    print("Some TF-IDF scores corresponding to term-document pairs:")
    for i in range(10):
        token_doc_tuple = random.choice(token_doc_tuples)
        score_1 = tf_idf_mapping_1[token_doc_tuple]
        
        token_name, doc_name = token_doc_tuple[0], document_index_mapping[token_doc_tuple[1]]
        print("Term:", token_name, "\b, Document:",doc_name + ".txt","\b, Score:",score_1)
    
    print()

    min_tf_idf_1_value, max_tf_idf_1_value = min(tf_idf_mapping_1.values()), max(tf_idf_mapping_1.values())
    document_corpus_1 = generate_document_corpus(tf_idf_mapping_1, no_of_docs)
    save_document_corpus_to_file(document_corpus_1, document_index_mapping, token_mapping, no_of_docs)

    # TF-IDF 2
    tf_type = 1
    idf_type = 1
    tf_idf_mapping_2 = calculate_tf_idf_scores(tf_type,K,idf_type,tdf_mapping,utf_mapping,no_of_docs)
    min_tf_idf_2_value, max_tf_idf_2_value = min(tf_idf_mapping_2.values()), max(tf_idf_mapping_2.values())
    document_corpus_2 = generate_document_corpus(tf_idf_mapping_2, no_of_docs)

    # TF-IDF 3
    tf_type = 0
    idf_type = 1
    tf_idf_mapping_3 = calculate_tf_idf_scores(tf_type,K,idf_type,tdf_mapping,utf_mapping,no_of_docs)
    min_tf_idf_3_value, max_tf_idf_3_value = min(tf_idf_mapping_3.values()), max(tf_idf_mapping_3.values())
    document_corpus_3 = generate_document_corpus(tf_idf_mapping_3, no_of_docs)

    # TF-IDF 3
    tf_type = 1
    idf_type = 0
    tf_idf_mapping_4 = calculate_tf_idf_scores(tf_type,K,idf_type,tdf_mapping,utf_mapping,no_of_docs)
    min_tf_idf_4_value, max_tf_idf_4_value = min(tf_idf_mapping_4.values()), max(tf_idf_mapping_4.values())
    document_corpus_4 = generate_document_corpus(tf_idf_mapping_4, no_of_docs)
    
    print("Differences in TF-IDF scores on using 4 different combinations for some term-document pairs:")
    
    score_lists = set()
    for i in range(10):
        token_doc_tuple = random.choice(token_doc_tuples)
        score_1 = tf_idf_mapping_1[token_doc_tuple]
        score_2 = tf_idf_mapping_2[token_doc_tuple]
        score_3 = tf_idf_mapping_3[token_doc_tuple]
        score_4 = tf_idf_mapping_4[token_doc_tuple]
        score_list = (score_1,score_2,score_3,score_4)
        if score_list not in score_lists and len(set(score_list)) == 4:
            token_id, doc_id = token_mapping[token_doc_tuple[0]], token_doc_tuple[1]
            print("Term ID:", token_id, "\b, Document ID:",doc_id,"\b, Scores:",score_1,score_2,score_3,score_4)
        score_lists.add(score_list)
    
    print()


    min_tf_idf_value = max(min_tf_idf_1_value, min_tf_idf_2_value)
    max_tf_idf_value = min(max_tf_idf_1_value, max_tf_idf_2_value)


    for len_of_words in [5,10,15]:
        query = dict()
        for _1 in range(len_of_words):
            random_token_id = random.randint(1,len(tokens))
            random_token_weight = random.uniform(min_tf_idf_value,max_tf_idf_value)
            query[random_token_id] = random_token_weight

        print("Query: " + vsm_doc_string_2(query))

        # Using 1st
        cos_sim_values_1 = generate_ranking(query, document_corpus_1, inverse_token_mapping)
        doc_id_list = [i for i in range(0, no_of_docs + 1)]
        ranked_doc_ids_1 = rank_doc_ids(cos_sim_values_1, doc_id_list)

        # Using 2nd
        cos_sim_values_2 = generate_ranking(query, document_corpus_2, inverse_token_mapping)
        doc_id_list = [i for i in range(0, no_of_docs + 1)]
        ranked_doc_ids_2 = rank_doc_ids(cos_sim_values_2, doc_id_list)

        print("Doc. ID\t\tCos-sim Score - I\t\tCos-sim Score - II")
        for doc_id in range(1, no_of_docs+1):
            print(doc_id,"\t\t",cos_sim_values_1[doc_id],"\t\t\t",cos_sim_values_2[doc_id])
        print("Final Rankings (for positive scores):")
        print("I: " + ", ".join([str(x) for x in ranked_doc_ids_1]))
        print("II: " + ", ".join([str(x) for x in ranked_doc_ids_2]))
        print()


if __name__ == '__main__':
    main()