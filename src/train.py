import pandas as pd
import string
import re 
import nltk
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
from nltk.tokenize import word_tokenize
import gensim
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize

max_epochs = 100
vec_size = 20
alpha = 0.025

def clean(data):
    data_clean = re.sub(r"\d+", "", data)
    data_clean = re.sub('\n',  ' ', data_clean)
    data_clean = data_clean.lower()
    data_clean = data_clean.translate(str.maketrans(' ', ' ', string.punctuation))
    data_clean = data_clean.strip()
    data_clean = re.sub('pictwitter',  ' ', data_clean)
    data_clean = re.sub('\xa0',  ' ', data_clean)
    data_clean = re.sub("(?P<url>https?://[^\s]+)", '', data_clean)
    data_clean = re.sub("http", '', data_clean)
    data_clean = re.sub(r'//t\.co.+', '', data_clean)
    # Remove retweets
    data_clean = re.sub(r'^RT @.+\:', '', data_clean)
    data_clean = re.sub('@', '', data_clean)
    # Remove new line characters
    data_clean = re.sub(r'\s+', ' ', data_clean)
    # Remove distracting single quotes
    data_clean = re.sub(r"\'", "", data_clean)
    return data_clean

def tokenize(data):
    tokens = word_tokenize(data)
    result = [i for i in tokens if not i in stop_words]
    return result

def listToString(data):
    data_clean = ' '.join([str(elem) for elem in data])
    return data_clean

df = pd.read_csv("../data/tweets.csv")
df_clear = df.drop(columns=["Unnamed: 0","date","id","retweet","author"])
df_clear = df_clear.dropna()

df_clear2 = [clean(x) for x in df_clear['text']]

df_clear3 = [tokenize(x) for x in df_clear2]

df_clear4 = [listToString(x) for x in df_clear3]


tagged_data = [TaggedDocument(words=word_tokenize(_d.lower()), tags=[str(i)]) for i, _d in enumerate(df_clear4)]


model = Doc2Vec(vector_size=vec_size,
                alpha=alpha, 
                min_alpha=0.00025,
                min_count=1,
                dm =1)

model.build_vocab(tagged_data)

for epoch in range(max_epochs):
    print('iteration {0}'.format(epoch))
    model.train(tagged_data,
                total_examples=model.corpus_count,
                epochs=model.iter)
    # decrease the learning rate
    model.alpha -= 0.0002
    # fix the learning rate, no decay
    model.min_alpha = model.alpha

model.save("../model/d2v.model")
print("Model Saved")