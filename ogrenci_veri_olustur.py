import pandas as pd
import numpy as np

# Seed ayarla (tekrarlanabilir sonuçlar için)
np.random.seed(42)

# 500 öğrenci verisi oluştur
n_students = 500
data = {
    'ID': range(1, n_students + 1),
    'Exam Score': np.round(np.random.uniform(60, 100, n_students), 2),
    'Daily Study Hours': np.round(np.random.uniform(1, 8, n_students), 2)
}

# DataFrame oluştur
df = pd.DataFrame(data)

# CSV dosyasına kaydet (temiz format)
df.to_csv('ogrenci_veri.csv', index=False, encoding='utf-8')

print("✅ CSV dosyası başarıyla oluşturuldu!")
print(f"\n📊 Dosya Bilgisi:")
print(f"  - Toplam Kayıt: {len(df)}")
print(f"  - Sütunlar: {list(df.columns)}")
print(f"  - Dosya: ogrenci_veri.csv")
print(f"\n📋 İlk 5 satır:")
print(df.head())
print(f"\n📈 İstatistikler:")
print(df.describe())