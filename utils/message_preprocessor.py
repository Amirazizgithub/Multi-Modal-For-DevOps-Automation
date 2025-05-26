import os
import nltk
import string

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Add local nltk_data path
local_nltk_path = os.path.join(os.path.dirname(__file__), "nltk_data")
nltk.data.path.append(local_nltk_path)


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
