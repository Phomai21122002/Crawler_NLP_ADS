import re
import pandas as pd
from pyvi import ViTokenizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')

# Danh sách stopwords tiếng Việt
stopwords_vietnamese = set([
    "bị", "cả", "các", "cái", "cần", "càng", "chỉ", "chiếc", "cho", "chứ", "chưa", "chuyện", "có", "cứ", "của", "cùng", 
    "cũng", "đã", "đang", "đây", "để", "đều", "điều", "do", "đó", "được", "dưới", "gì", "khi", "không", "là", 
    "lại", "lên", "lúc", "mà", "mỗi", "này", "nên", "nếu", "ngay", "nhiều", "như", "nhưng", "những", "nơi", 
    "nữa", "phải", "qua", "ra", "rằng", "rất", "rất nhiều", "rồi", "sau", "sẽ", "so", "sự", "tại", "theo", "thì", "trên", 
    "trước", "từ", "từng", "và", "vẫn", "vào", "vậy", "vì", "việc", "với"
])

# Đọc file CSV và tạo DataFrame
df = pd.read_csv('data.csv', sep=',', error_bad_lines=False)

# Loại bỏ các phần tử trùng nhau
df = df.drop_duplicates()
# Loại bỏ các hàng có giá trị None
df = df.dropna()

# Hàm để xóa đường dẫn trong cột 'content'
def remove_links(text):
    return ' '.join([word for word in text.split() if not word.startswith('http')])

# Hàm để xóa dấu câu và ký tự đặt biệt trong cột 'content'
def remove_special_characters(text):
    return re.sub(r'[^\w\s]', '', text)

def tokenize_text(text):
    return word_tokenize(text)

# Hàm để xóa stopwords tiếng Việt từ văn bản
def remove_stopwords_vietnamese(text):
    words = ViTokenizer.tokenize(text).split()
    filtered_words = [word for word in words if word not in stopwords_vietnamese]
    return ' '.join(filtered_words)

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word not in stop_words]
    return ' '.join(filtered_text)

# Loại bỏ từ dài hoặc ngắn quá
def remove_short_content(df):
    # Lọc ra các dòng có độ dài content lớn hơn hoặc bằng 5 từ
    df_filtered = df[df['content'].apply(lambda x: len(x.split()) >= 5)]
    return df_filtered

# # Tách từ và gán nhãn (tùy chọn)
# def lemmatize_text(text):
#     lemmatizer = WordNetLemmatizer()
#     words = word_tokenize(text)
#     lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
#     return ' '.join(lemmatized_words)

# Tien xu ly du lieu
# xoa /r
df['content'] = df['content'].str.replace('\r', '')

# Áp dụng hàm remove_links vào cột 'content'
df['content'] = df['content'].apply(remove_links)

# Áp dụng hàm lower() vào cột 'content'
df['content'] = df['content'].str.lower()

# Hàm để xóa dấu câu và ký tự đặt biệt trong cột 'content'
df['content'] = df['content'].apply(remove_special_characters)

# Áp dụng hàm remove_stopwords vietnamese vào cột 'content'
df['content'] = df['content'].apply(remove_stopwords_vietnamese)

# Áp dụng hàm remove_stopwords english vào cột 'content'
df['content'] = df['content'].apply(remove_stopwords)

df = remove_short_content(df)

# tokenization
df['content'] = df['content'].apply(tokenize_text)

# tach data
df_subheader_1 = df[df['subHeader'] == '1']
df_subheader_0 = df[df['subHeader'] == '0']

# Chuyển DataFrame thành chuỗi JSON
json_data_1 = df_subheader_1.to_json(orient='records')
json_data_0 = df_subheader_0.to_json(orient='records')


# Ghi chuỗi JSON vào file
with open('json_data_1.json', 'w') as file:
    file.write(json_data_1)

with open('json_data_0.json', 'w') as file:
    file.write(json_data_0)

# print(df['content'])
df.to_csv('tryData.csv',encoding='utf-8',mode='a', index=False)