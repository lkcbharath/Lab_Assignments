import nltk
from nltk.corpus import gutenberg, brown

def download_nltk_libraries():
  nltk.download("gutenberg")
  nltk.download("brown")
  print()


def gutenberg_corpus():
  print("The files in the Gutenberg Corpus are:", ", ".join(gutenberg.fileids()), "\n")

  poems = gutenberg.words("blake-poems.txt")
  print("Number of words (including punctuation) in Poems by William Blake are:", len(poems))
  print("Some of the words are:", ", ".join(poems[:20]), "\n")

  hamlet_sent = gutenberg.sents("shakespeare-hamlet.txt")
  print("The number of sentences in Hamlet by Shakespeare are:", len(hamlet_sent))
  print("Some of the sentences are:")
  print(" ".join(hamlet_sent[0]),"\n"," ".join(hamlet_sent[1]),"\n")

  idx = 0
  sen_long = 0
  for i in range(len(hamlet_sent)):
    sentence = hamlet_sent[i]
    if len(sentence) > sen_long:
      sen_long = len(sentence)
      idx = i

  print("The longest sentence in Hamlet is of length: ", sen_long)
  print("The sentence is: ", " ".join([s for s in hamlet_sent[idx]]), "\n")


def brown_corpus():
  print("The categories in the Brown corpus are:", ", ".join(brown.categories()), "\n")

  humor_words = brown.words(categories='humor')
  print("The number of words in the Humor category are:", len(humor_words))
  print("Some of the words are:", ", ".join(humor_words[:10]))

  fiction_sents = brown.sents(categories="fiction")
  print("The number of sentences in the Fiction category are:", len(fiction_sents))
  print("Some of the sentences are:")
  print(" ".join(fiction_sents[0]))
  print(" ".join(fiction_sents[1]),"\n")

  idx = 0
  sen_long = 0
  for i in range(len(fiction_sents)):
    sentence = fiction_sents[i]
    if len(sentence) > sen_long:
      sen_long = len(sentence)
      idx = i

  print("The longest sentence in the Fiction category is of length: ", sen_long)
  print("The sentence is: ", " ".join([s for s in fiction_sents[idx]]), "\n")

  print("The Frequncy Distance between some words in the News category:")
  news_text = brown.words(categories='news')
  fdist = nltk.FreqDist(w.lower() for w in news_text)
  modals = ['can', 'could', 'may', 'might', 'must', 'will']
  for m in modals:
    print(m + ':' + str(fdist[m]), end=' ')
  print("\n")

  print("A Conditional Frequency Distance tabulation between some genres and words in the Brown Corpus:")

  cfd = nltk.ConditionalFreqDist(
    (genre, word) 
      for genre in brown.categories()
        for word in brown.words(categories=genre)
  )
  genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
  modals = ['can', 'could', 'may', 'might', 'must', 'will']
  cfd.tabulate(conditions=genres, samples=modals)

def main():
  download_nltk_libraries()
  gutenberg_corpus()
  brown_corpus()

if __name__ == '__main__':
  main()