import os
import nltk
import string

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Ensure required NLTK data is available (safe for CI/CD)
try:
    stopwords.words("english")
except LookupError:
    nltk.download("stopwords")
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")
try:
    nltk.data.find("corpora/wordnet")
except LookupError:
    nltk.download("wordnet")


class MessagePreprocessor:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words("english"))

    def preprocess(self, text: str) -> str:
        """
        Preprocess a given message:
        1. Lowercase and tokenize
        2. Remove punctuation
        3. Remove stopwords
        4. Lemmatize
        Returns a cleaned string.
        """
        # Lowercasing and tokenization
        tokens = word_tokenize(text.lower())

        # Remove punctuation
        tokens = [
            token.translate(str.maketrans("", "", string.punctuation))
            for token in tokens
        ]
        tokens = [token for token in tokens if token]  # Remove empty tokens

        # Remove stopwords
        filtered_tokens = [word for word in tokens if word not in self.stop_words]

        # Lemmatize remaining tokens
        lemmatized_tokens = [
            self.lemmatizer.lemmatize(word) for word in filtered_tokens
        ]

        return " ".join(lemmatized_tokens)


# Singleton instance for reuse
message_preprocessor = MessagePreprocessor()
