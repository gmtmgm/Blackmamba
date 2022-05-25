import tensorflow as tf
from tokenizing import *
import cx_Oracle as cx
from tensorflow.keras import preprocessing
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Embedding, Dense, Dropout, Conv1D, GlobalMaxPool1D, concatenate
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

q_list = []
i_list = []

dsn = cx.makedsn("localhost", 1521, service_name= "XE")
db = cx.connect(user="c##Blackmamba", password="blackmamba", dsn=dsn)

cur = db.cursor()
questiondata = cur.execute("select question from 메세지")

for q in questiondata:
    qq = list(q)
    for r in qq:
        q_list.append(str(r))

cur = db.cursor()
intentdata = cur.execute("select intent_id from 메세지")

for i in intentdata:
    ii = list(i)
    for r in ii:
        i_list.append(r)

cur.close()
db.close()

corpus = [preprocessing.text.text_to_word_sequence(text) for text in q_list]
tokenizer = preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(corpus)
sequences = tokenizer.texts_to_sequences(corpus)
word_index = tokenizer.word_index

MAX_SEQ_LEN = 15
padded_seqs = preprocessing.sequence.pad_sequences(sequences, maxlen=MAX_SEQ_LEN, padding='post')

ds = tf.data.Dataset.from_tensor_slices((padded_seqs, i_list))
ds = ds.shuffle(len(q_list))

train_size = int(len(padded_seqs) * 0.7)
val_size = int(len(padded_seqs) * 0.2)
test_size = int(len(padded_seqs) * 0.1)

train_ds = ds.take(train_size).batch(20)
val_ds = ds.skip(train_size).take(val_size).batch(20)
test_ds = ds.skip(train_size + val_size).take(test_size).batch(20)

dropout_prob = 0.5
EMB_SIZE = 128
EPOCH = 5
VOCAB_SIZE = len(word_index) + 1

input_layer = Input(shape=(MAX_SEQ_LEN,))
embedding_layer = Embedding(VOCAB_SIZE, EMB_SIZE, input_length=MAX_SEQ_LEN)(input_layer)
dropout_emb = Dropout(rate=dropout_prob)(embedding_layer)

conv1 = Conv1D(
    filters=128, 
    kernel_size=3,
    padding='valid',
    activation=tf.nn.relu)(dropout_emb)
pool1 = GlobalMaxPool1D()(conv1)

conv2 = Conv1D(
    filters=128, 
    kernel_size=4,
    padding='valid',
    activation=tf.nn.relu)(dropout_emb)
pool2 = GlobalMaxPool1D()(conv2)

conv3 = Conv1D(
    filters=128, 
    kernel_size=5,
    padding='valid',
    activation=tf.nn.relu)(dropout_emb)
pool3 = GlobalMaxPool1D()(conv3)

concat = concatenate([pool1, pool2, pool3])

hidden = Dense(128, activation=tf.nn.relu)(concat)
dropout_hidden = Dropout(rate=dropout_prob)(hidden)
logits = Dense(7, name='logits')(dropout_hidden)
predictions = Dense(7, activation=tf.nn.softmax)(logits)

model = Model(inputs=input_layer, outputs=predictions)
model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

model.fit(train_ds, validation_data=val_ds, epochs=EPOCH, verbose=1)

loss, accuracy = model.evaluate(test_ds, verbose=1)
print('Accuracy: %f' % (accuracy * 100))
print('loss: %f' % (loss))

model.save('cnn_model.h5')
