import pandas as pd
import matplotlib.pyplot as plt

# CSV dosyasını oku
df = pd.read_csv('ogrenci_veri.csv')

# Görselleştirme için figure oluştur (2x2 grid)
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Öğrenci Verileri Analizi - 500 Öğrenci', fontsize=16, fontweight='bold')

# 1. Sınav Notu Histogramı
axes[0, 0].hist(df['Exam Score'], bins=30, color='skyblue', edgecolor='black', alpha=0.7)
axes[0, 0].set_xlabel('Sınav Notu', fontsize=12)
axes[0, 0].set_ylabel('Öğrenci Sayısı', fontsize=12)
axes[0, 0].set_title('Sınav Notu Dağılımı', fontsize=12, fontweight='bold')
axes[0, 0].grid(axis='y', alpha=0.3)

# 2. Çalışma Saati Histogramı
axes[0, 1].hist(df['Daily Study Hours'], bins=30, color='lightcoral', edgecolor='black', alpha=0.7)
axes[0, 1].set_xlabel('Günlük Çalışma Saati (h)', fontsize=12)
axes[0, 1].set_ylabel('Öğrenci Sayısı', fontsize=12)
axes[0, 1].set_title('Günlük Çalışma Saati Dağılımı', fontsize=12, fontweight='bold')
axes[0, 1].grid(axis='y', alpha=0.3)

# 3. Scatter Plot
axes[1, 0].scatter(df['Daily Study Hours'], df['Exam Score'], alpha=0.5, s=30, color='green')
axes[1, 0].set_xlabel('Günlük Çalışma Saati (h)', fontsize=12)
axes[1, 0].set_ylabel('Sınav Notu', fontsize=12)
axes[1, 0].set_title('Çalışma Saati vs Sınav Notu', fontsize=12, fontweight='bold')
axes[1, 0].grid(alpha=0.3)

correlation = df['Daily Study Hours'].corr(df['Exam Score'])
axes[1, 0].text(0.05, 0.95, f'Korelasyon: {correlation:.3f}', 
                transform=axes[1, 0].transAxes, fontsize=11,
                verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# 4. Box Plot
box_data = [df['Exam Score'], df['Daily Study Hours']]
axes[1, 1].boxplot(box_data, labels=['Sınav Notu', 'Çalışma Saati'])
axes[1, 1].set_ylabel('Değer', fontsize=12)
axes[1, 1].set_title('Veri İstatistikleri (Box Plot)', fontsize=12, fontweight='bold')
axes[1, 1].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('ogrenci_veri_gorsellestirme.png', dpi=300, bbox_inches='tight')
print("✅ PNG kaydedildi: ogrenci_veri_gorsellestirme.png")

# İstatistiksel Özet
print("\n" + "="*60)
print("📊 İSTATİSTİKSEL ÖZET")
print("="*60)
print("\n📈 Sınav Notu İstatistikleri:")
print(df['Exam Score'].describe())
print("\n⏱️ Günlük Çalışma Saati İstatistikleri:")
print(df['Daily Study Hours'].describe())
print(f"\n🔗 Korelasyon Katsayısı: {correlation:.4f}")

cd 3.hafta
python veri_gorsellestir.py
print("="*60)

git add .
git commit -m "Add proper visualization PNG"
git push origin main
