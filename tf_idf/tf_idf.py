from typing import List
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

korean_stop_words_lentwo = [
    '에게','으로',
    '이나', '하지만', '그런데', '그래서', '때문에', '만약', '보다', '아니면', '또는',
    '하고', '그리고', '그러나', '그래도', '그러면', '그러므로', '하지만', '바로', '대신',
    '즉시', '바로','결국', '심지어', '다시', '여기', '거기',
    '어디', '언제', '누구', '어떻게', '이렇게', '저렇게', '많이', '조금', '정말', '아주',
    '너무', '같이','까지', '한다', '있다'
]


korean_stop_words = [
    '은', '는', '이', '가', '을', '를', '에', '에게', '로', '으로', '의', '와', '과',
    '이나', '나', '하지만', '그런데', '그래서', '때문에', '만약', '보다', '아니면', '또는',
    '하고', '그리고', '그러나', '그래도', '그러면', '그러므로', '하지만', '바로', '대신',
    '즉', '즉시', '바로', '곧', '결국', '심지어', '다시', '그', '이', '저', '여기', '거기',
    '어디', '언제', '왜', '누구', '어떻게', '이렇게', '저렇게', '많이', '조금', '정말', '아주',
    '너무', '다', '같이','까지', '한다', '있다'
]


def remove_attached_stop_words_adjusted(texts, stop_words):
    processed_texts = []
    for text in texts:
        # Directly remove stop words that are longer than two characters
        for stop_word in [sw for sw in stop_words if len(sw) > 2]:
            text = text.replace(stop_word, '')
        words = text.split()
        new_words = []
        for word in words:
            # Process for stop words that are one character long
            if len(word) > 1:  # Only proceed if the word has more than one character
                for stop_word in [sw for sw in stop_words if len(sw) == 1]:
                    if word.endswith(stop_word):
                        word = word[:-len(stop_word)]
                        break  # Assuming one stop word per word end
            # Append the word if it's not a stop word
            if word not in stop_words:
                new_words.append(word)
        processed_texts.append(' '.join(new_words))
    return processed_texts


def remove_all_stop_words(texts, stop_words):
    processed_texts = []
    for text in texts:
        # Directly replace each stop word with an empty string in the entire text
        for stop_word in stop_words:
            text = text.replace(stop_word, '')
        processed_texts.append(text)
    return processed_texts


def texts_to_tfidf_dense_matrix(texts: List[str]) -> np.ndarray:
    processed_texts = remove_all_stop_words(texts, korean_stop_words_lentwo)
    p_processed_texts = remove_attached_stop_words_adjusted(processed_texts, korean_stop_words)
    vectorizer = CountVectorizer(min_df=1)
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(p_processed_texts)
    dense_tfidf_matrix = np.array(tfidf_matrix.todense(), dtype='float32')
    return dense_tfidf_matrix
