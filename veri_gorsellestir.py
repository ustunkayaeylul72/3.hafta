import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# CSV dosyasını oku
df = pd.read_csv('ogrenci_veri.csv')

# Sütun adlarını kontrol et
print("Sütun adları:", df.columns.tolist())
print(f"Veri boyutu: {df.shape}")

# Görselleştirme için figure oluştur (2x3 grid)
fig = plt.figure(figsize=(16, 12))
fig.suptitle('Ogrenci Verileri Analizi - 500 Ogrenci', fontsize=18, fontweight='bold', y=0.995)

# 1. Sinav Notu Histogrami
ax1 = plt.subplot(2, 3, 1)
ax1.hist(df['Exam Score'], bins=30, color='skyblue', edgecolor='black', alpha=0.7)
ax1.set_xlabel('Sinav Notu', fontsize=11, fontweight='bold')
ax1.set_ylabel('Ogrenci Sayisi', fontsize=11, fontweight='bold')
ax1.set_title('Sinav Notu Dagilimi', fontsize=12, fontweight='bold')
ax1.grid(axis='y', alpha=0.3)
ax1.set_facecolor('#f9f9f9')

# 2. Calisma Saati Histogrami
ax2 = plt.subplot(2, 3, 2)
ax2.hist(df['Daily Study Hours'], bins=25, color='lightcoral', edgecolor='black', alpha=0.7)
ax2.set_xlabel('Gunluk Calisma Saati (h)', fontsize=11, fontweight='bold')
ax2.set_ylabel('Ogrenci Sayisi', fontsize=11, fontweight='bold')
ax2.set_title('Gunluk Calisma Saati Dagilimi', fontsize=12, fontweight='bold')
ax2.grid(axis='y', alpha=0.3)
ax2.set_facecolor('#f9f9f9')

# 3. Scatter Plot - Calisma Saati vs Sinav Notu
ax3 = plt.subplot(2, 3, 3)
scatter = ax3.scatter(df['Daily Study Hours'], df['Exam Score'], alpha=0.6, s=50, 
                     c=df['Exam Score'], cmap='viridis', edgecolors='black', linewidth=0.5)
ax3.set_xlabel('Gunluk Calisma Saati (h)', fontsize=11, fontweight='bold')
ax3.set_ylabel('Sinav Notu', fontsize=11, fontweight='bold')
ax3.set_title('Calisma Saati vs Sinav Notu Iliskisi', fontsize=12, fontweight='bold')
ax3.grid(alpha=0.3)
ax3.set_facecolor('#f9f9f9')

# Korelasyon hesapla
correlation = df['Daily Study Hours'].corr(df['Exam Score'])
ax3.text(0.05, 0.95, f'Korelasyon: {correlation:.3f}', 
         transform=ax3.transAxes, fontsize=11, fontweight='bold',
         verticalalignment='top', bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))
plt.colorbar(scatter, ax=ax3, label='Sinav Notu')

# 4. Box Plot
ax4 = plt.subplot(2, 3, 4)
box_data = [df['Exam Score'], df['Daily Study Hours']]
bp = ax4.boxplot(box_data, labels=['Sinav Notu', 'Calisma Saati'], patch_artist=True)
for patch, color in zip(bp['boxes'], ['lightblue', 'lightcoral']):
    patch.set_facecolor(color)
ax4.set_ylabel('Deger', fontsize=11, fontweight='bold')
ax4.set_title('Veri Istatistikleri (Box Plot)', fontsize=12, fontweight='bold')
ax4.grid(axis='y', alpha=0.3)
ax4.set_facecolor('#f9f9f9')

# 5. Sinav Notu Dagilim Egrisi (KDE)
ax5 = plt.subplot(2, 3, 5)
df['Exam Score'].plot(kind='density', ax=ax5, color='blue', linewidth=2.5, label='Sinav Notu')
ax5.fill_between(ax5.lines[0].get_xdata(), ax5.lines[0].get_ydata(), alpha=0.3, color='blue')
ax5.set_xlabel('Sinav Notu', fontsize=11, fontweight='bold')
ax5.set_ylabel('Yogunluk', fontsize=11, fontweight='bold')
ax5.set_title('Sinav Notu Dagilim Egrisi (Density)', fontsize=12, fontweight='bold')
ax5.grid(alpha=0.3)
ax5.set_facecolor('#f9f9f9')
ax5.legend(fontsize=10)

# 6. İstatistiksel Bilgiler
ax6 = plt.subplot(2, 3, 6)
ax6.axis('off')

# İstatistik hesapla
stats_text = f"""
ISTATISTIKSEL OZET
{'='*40}

SINAV NOTU:
  Ortalama: {df['Exam Score'].mean():.2f}
  Medyan: {df['Exam Score'].median():.2f}
  Std. Sapma: {df['Exam Score'].std():.2f}
  Minimum: {df['Exam Score'].min():.2f}
  Maksimum: {df['Exam Score'].max():.2f}

GUNLUK CALISMA SAATI:
  Ortalama: {df['Daily Study Hours'].mean():.2f}
  Medyan: {df['Daily Study Hours'].median():.2f}
  Std. Sapma: {df['Daily Study Hours'].std():.2f}
  Minimum: {df['Daily Study Hours'].min():.2f}
  Maksimum: {df['Daily Study Hours'].max():.2f}

KORELASYON:
  Pearson r: {correlation:.4f}
  Toplam Kayit: {len(df)}
"""

ax6.text(0.1, 0.95, stats_text, transform=ax6.transAxes, fontsize=10,
         verticalalignment='top', fontfamily='monospace',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

plt.tight_layout()
plt.savefig('tum_grafikler.png', dpi=300, bbox_inches='tight')
print("\n✅ PNG kaydedildi: tum_grafikler.png")
print("📊 BASARILI - Gorsellestime tamamlandi!")
print(f"📈 Korelasyon Katsayisi: {correlation:.4f}")
print(f"📋 Toplam Veri: {len(df)} adet")
plt.show()

