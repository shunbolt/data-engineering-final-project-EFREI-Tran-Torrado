import pandas as pd
import string
import re 
import nltk
import gensim
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
from nltk.tokenize import word_tokenize
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize


def prediction():

    df = pd.read_csv("../data/tweets.csv")
    topn = 20

    model= Doc2Vec.load("../model/d2v.model")
    #to find the vector of a document which is not in training data
    test_data = word_tokenize("make america great again".lower())
    v1 = model.infer_vector(test_data)


    similar_doc = model.docvecs.most_similar([v1],topn=topn)
    result = []
    score = []

    for  n in range(topn):
        res = df["text"][int(similar_doc[n][0])], similar_doc[n][1]
        result.append(res)
    for  n in range(topn):
        res = df["text"][int(similar_doc[n][0])]
        sim = similar_doc[n][1]
        result.append(res)
        score.append(sim)   
        
    return result, score
