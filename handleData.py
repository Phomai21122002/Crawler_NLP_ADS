from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

import json

with open('json_data_1.json') as f:
    data = json.load(f)

# for item in data:
#     print(item)

sentences = []
for item in data:
    sentences.append(item['content'])
print(sentences)

tokenizer = Tokenizer(oov_token='<OOV>')
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index
    
sequences = tokenizer.texts_to_sequences(sentences)
# print(sequences)

padded = pad_sequences(sequences, padding='post')
print(padded)
