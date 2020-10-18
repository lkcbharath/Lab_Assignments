import nltk
import sklearn
from nltk.corpus import stopwords
from nltk.util import bigrams, ngrams, everygrams


def download_nltk_libraries():
  nltk.download("stopwords")
  nltk.download("punkt")
  nltk.download("wordnet")
  print()


def stopword_removal(test_para):
  stopwords_set = set(stopwords.words('english')) 
  stopwordless_text = " ".join([word for word in test_para.split() if word not in stopwords_set])
  print("After removing stopwords using those defined in the NLTK library:", stopwordless_text)
  print()


def tokenization(test_para):
  sent_tokenized_text = nltk.tokenize.sent_tokenize(test_para)
  print("After tokenizing using sent_tokenize:", " ".join(sent_tokenized_text))

  word_tokenized_text = nltk.tokenize.word_tokenize(test_para)
  print("After tokenizing using word_tokenize:", " ".join(word_tokenized_text))

  wnt = nltk.tokenize.WordPunctTokenizer()
  word_punc_tokenized_text = wnt.tokenize(test_para)
  print("After tokenizing using WordPunctTokenizer:", " ".join(word_punc_tokenized_text))
  
  print()


def stemming(test_para):
  ps = nltk.stem.PorterStemmer()
  porter_stemmed_text = " ".join([ps.stem(word) for word in test_para.split()])
  print("After stemming using PorterStemmer:", porter_stemmed_text)

  ls = nltk.stem.LancasterStemmer()
  lancaster_stemmed_text = " ".join([ls.stem(word) for word in test_para.split()])
  print("After stemming using LancasterStemmer:", lancaster_stemmed_text)

  ss = nltk.stem.SnowballStemmer("english")
  snowball_stemmed_text = " ".join([ss.stem(word) for word in test_para.split()])
  print("After stemming using SnowballStemmer:", snowball_stemmed_text)
  
  print()


def lemmatization(test_para):
  wnl = nltk.stem.WordNetLemmatizer()
  wordnet_lemmatized_text = " ".join([wnl.lemmatize(word) for word in test_para.split()])
  print("After lemmatization using WordNetLemmatizer:", wordnet_lemmatized_text)
  
  print()


def stem_lem_diff():
  ps = nltk.stem.PorterStemmer()
  wnl = nltk.stem.WordNetLemmatizer()

  print("Differences in words between Stemming and Lemmatization respectively:")
  print(ps.stem("bats"),wnl.lemmatize("bats"))
  print(ps.stem("caring"),wnl.lemmatize("caring","n"),wnl.lemmatize("caring","v"))
  print(ps.stem("saw"),wnl.lemmatize("saw"))
  print(ps.stem("feet"),wnl.lemmatize("feet"))
  print(ps.stem("stripes"),wnl.lemmatize("stripes","n"),wnl.lemmatize("stripes","v"))
  
  print()


def vocab_model(test_para):
  cvr = sklearn.feature_extraction.text.CountVectorizer()
  features = cvr.fit_transform(test_para.split(".")).todense()
  print("There are ",len(cvr.vocabulary_),"distinct words in the text. Their occurences are:\n",cvr.vocabulary_)
  
  print()


def ngram_modelling():
  text = [['d', 'e', 'f'], ['a', 'c', 'd', 'c', 'e', 'f']]
  print(list(bigrams(text[0])))
  print(list(ngrams(text[1],n=2)))
  print(list(ngrams(text[1],n=3,pad_right=True,right_pad_symbol="<\s>")))
  print(list(ngrams(text[1],n=3,pad_right=True,right_pad_symbol="<\s>",pad_left=True,left_pad_symbol="<\s>")))
  print(list(everygrams(text[0],max_len=3,pad_left=True,pad_right=True,right_pad_symbol="<\s>",left_pad_symbol="<\s>")))
  print()


def main():
  download_nltk_libraries()

  test_para = ""
  with open("test_para.txt", "r") as f:
    test_para = f.readline()

  stopword_removal(test_para)
  tokenization(test_para)
  stemming(test_para)
  lemmatization(test_para)
  stem_lem_diff()
  vocab_model(test_para)
  ngram_modelling()


if __name__ == '__main__':
  main()