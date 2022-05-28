import tensorflow as tf
from tensorflow.keras.models import Model, load_model
from tensorflow.keras import preprocessing

class IntentModel:
    def __init__(self, model_name, proprocess):
        self.labels = {0: "안내", 1: "프랜차이즈", 2: "메뉴", 3: "알레르기 성분 표시",
        4: "알레르기 성분 입력", 5: "알레르기 성분 필터링",
        6: "메뉴 알레르기 성분 포함여부", 7: "입력 실패"}
        
        self.model = load_model(model_name)

        self.p = proprocess

    def predict_class(self, query):
        pos = self.p.pos(query)

        keywords = self.p.get_keywords(pos, with_tag=False)
        
        corpus = [preprocessing.text.text_to_word_sequence(text) for text in keywords]
        tokenizer = preprocessing.text.Tokenizer()
        tokenizer.fit_on_sequences(corpus)
        sequences = tokenizer.texts_to_sequences(corpus)

        padded_seqs = preprocessing.sequence.pad_sequences(sequences, maxlen=15, padding='post')

        predict = self.model.predict(padded_seqs)
        predict_class = tf.math.argmax(predict, axis=1)
        return predict_class.numpy()[0]