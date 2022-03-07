import string
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords

stemmer = SnowballStemmer("english")

def clean(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

def stem(text):
    tokenize_text = word_tokenize(text)
    stemmed_text = []
    
    for token in tokenize_text :
        if not token in stopwords.words('english'):
            stemmed_word = stemmer.stem(token)
            stemmed_text.append(stemmed_word)
    
    return " ".join(stemmed_text)

def clean_and_stem(text):
    cleaned_text = clean(text)
    return stem(cleaned_text)