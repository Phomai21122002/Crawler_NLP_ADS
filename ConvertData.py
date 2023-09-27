import pandas as pd
from sklearn.model_selection import train_test_split
import torch
from transformers import BertTokenizer, BertModel

df = pd.read_csv('tryData.csv')

data = df

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(data[['header', 'content']], data['subHeader'], test_size=0.2, random_state=42)


# Xem thông tin về tập huấn luyện và tập kiểm tra
print(f"Số mẫu trong tập huấn luyện: {len(X_train)}")
print(f"Số mẫu trong tập huấn luyện y: {y_train.sum()}")
print(f"Số mẫu trong tập kiểm tra: {len(X_test)}")
print(f"Số mẫu trong tập kiểm tra y: {y_test.sum()}")

# Khởi tạo BERT tokenizer và model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')
# Hàm biểu diễn dữ liệu sử dụng BERT
def represent_with_bert(text):
    # Tokenize văn bản và chuyển đổi thành tensor
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    
    # Forward pass qua BERT model
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Lấy ra embedding của token [CLS] (được sử dụng cho phân loại)
    cls_embedding = outputs.last_hidden_state[:, 0, :]
    
    return cls_embedding

# Tạo một danh sách để lưu trữ các biểu diễn
representations = []

# Lặp qua các mẫu dữ liệu
for content in data['content']:
    content = eval(content)  # Chuyển đổi từ chuỗi thành danh sách
    content = ' '.join(content)  # Nối các từ lại thành một chuỗi
    representation = represent_with_bert(content)
    representations.append(representation)

# In ra kết quả biểu diễn của mỗi mẫu dữ liệu
for i, representation in enumerate(representations):
    print(f"Biểu diễn của mẫu {i + 1}:")
    print(representation)
    print("="*50)