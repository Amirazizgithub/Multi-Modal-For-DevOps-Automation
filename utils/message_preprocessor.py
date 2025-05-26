import nltk

nltk.download("punkt_tab")
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import string


class MessagePreprocessor:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words("english"))

    def preprocess(self, text: str) -> str:
        # 1. Lowercasing and Tokenization
        tokens = word_tokenize(text.lower())

        tokens = [
            token.translate(str.maketrans("", "", string.punctuation))
            for token in tokens
        ]
        # Remove empty strings that might result from punctuation removal
        tokens = [token for token in tokens if token]

        # 3. Stopword Removal
        filtered_tokens = [word for word in tokens if word not in self.stop_words]

        lemmatized_tokens = [
            self.lemmatizer.lemmatize(word) for word in filtered_tokens
        ]

        return " ".join(lemmatized_tokens)


message_preprocessor = MessagePreprocessor()
