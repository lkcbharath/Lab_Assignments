import random

def load_inverted_index(filename):
    inverted_index = {}

    with open(filename, "r") as f:
        lines = f.readlines()
        for linex in lines:
            
            # Remove trailing newline
            line = linex.rstrip()
            
            token, index_string = line.split(" : ")
            index_set = set([int(x) for x in index_string.split(", ")])

            inverted_index[token] = index_set
            
    return inverted_index

def main():
    filename = ""
    inverted_index = load_inverted_index("./inverted_indices/lemmatized_inverted_index.txt")
    tokens = list(inverted_index.keys())

    token_1 = random.choice(tokens)
    token_2 = random.choice(tokens)
    token_3 = random.choice(tokens)

    print(token_1,token_2,token_3)

    index_1 = inverted_index[token_1]
    index_2 = inverted_index[token_2]
    index_3 = inverted_index[token_3]

    print(index_1,index_2,index_3)

    # Operation 1: term1 and term2 and term3

    final_indices = index_1 & index_2 & index_3
    print(final_indices)

    # Operation 2: termi or term2 and not term3

    final_indices = index_1 | index_2 - index_3
    print(final_indices)



if __name__ == '__main__':
    main()