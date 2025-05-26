import os
import nltk
import string

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Ensure NLTK uses a custom data directory if set (e.g., in Docker/CI)
nltk_data_path = os.environ.get("NLTK_DATA")
if nltk_data_path:
    nltk.data.path.append(nltk_data_path)


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
