import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# CSV dosyasını oku
df = pd.read_csv('ogrenci_veri.csv')

# Türkçe karakter desteği
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']

# Görselleştirme için figure oluştur (2x2 grid)
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Ogrenci Verileri Analizi - 500 Ogrenci', fontsize=16, fontweight='bold')

# 1. Sinav Notu Histogrami
axes[0, 0].hist(df['sinav_notu'], bins=30, edgecolor='black', alpha=0.7)
axes[0, 0].set_xlabel('Sinav Notu', fontsize=12)
axes[0, 0].set_ylabel('Ogrenci Sayisi', fontsize=12)
axes[0, 0].set_title('Sinav Notu Dagilimi', fontsize=12, fontweight='bold')
axes[0, 0].grid(axis='y', alpha=0.3)

# 2. Calisma Saati Histogrami
axes[0, 1].hist(df['calisma_suresi'], bins=30, edgecolor='black', alpha=0.7)
axes[0, 1].set_xlabel('Gunluk Calisma Saati (h)', fontsize=12)
axes[0, 1].set_ylabel('Ogrenci Sayisi', fontsize=12)
axes[0, 1].set_title('Gunluk Calisma Saati Dagilimi', fontsize=12, fontweight='bold')
axes[0, 1].grid(axis='y', alpha=0.3)

# 3. Scatter Plot
axes[1, 0].scatter(df['calisma_suresi'], df['sinav_notu'], alpha=0.5)
axes[1, 0].set_xlabel('Gunluk Calisma Saati (h)', fontsize=12)
axes[1, 0].set_ylabel('Sinav Notu', fontsize=12)
axes[1, 0].set_title('Calisma Saati vs Sinav Notu', fontsize=12, fontweight='bold')
axes[1, 0].grid(alpha=0.3)

# Korelasyon
correlation = df['calisma_suresi'].corr(df['sinav_notu'])
axes[1, 0].text(0.05, 0.95, f'Korelasyon: {correlation:.3f}', 
                transform=axes[1, 0].transAxes, fontsize=11,
                verticalalignment='top',
                bbox=dict(boxstyle='round', alpha=0.5))

# 4. Box Plot
box_data = [df['sinav_notu'], df['calisma_suresi']]
axes[1, 1].boxplot(box_data, labels=['Sinav Notu', 'Calisma Saati'])
axes[1, 1].set_ylabel('Deger', fontsize=12)
axes[1, 1].set_title('Veri Istatistikleri (Box Plot)', fontsize=12, fontweight='bold')
axes[1, 1].grid(axis='y', alpha=0.3)

plt.tight_layout()

# PNG olarak kaydet
plt.savefig('tum_grafikler.png', dpi=300, bbox_inches='tight')
print("PNG kaydedildi: tum_grafikler.png")

# İstatistiksel Özet
print("\n" + "="*60)
print("İSTATİSTİKSEL ÖZET")
print("="*60)

print("\nSinav Notu İstatistikleri:")
print(df['sinav_notu'].describe())

print("\nGunluk Calisma Saati İstatistikleri:")
print(df['calisma_suresi'].describe())

print(f"\nKorelasyon Katsayisi: {correlation:.4f}")
print("="*60)

plt.show()

plt.savefig('tum_grafikler.png')

