import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Veriyi Yükleme
df = pd.read_csv('macro_event_processed.csv')
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# 2. Stil Ayarları
sns.set_theme(style="whitegrid", palette="muted")
plt.figure(figsize=(12, 7))

# 3. Çizim (Indexed Columns)
assets_map = {
    'SPY_idx': 'S&P 500 (SPY)',
    'DXY_idx': 'US Dollar Index (DXY)',
    'US10Y_idx': '10Y Treasury Yield',
    'VIX_idx': 'Volatility Index (VIX)'
}

for col, label in assets_map.items():
    sns.lineplot(data=df, x='Timestamp', y=col, label=label, linewidth=2)

# 4. Olay Anı (t=0) İşaretleme
event_time = pd.Timestamp(2024, 5, 15, 15, 30)
plt.axvline(x=event_time, color='red', linestyle='--', linewidth=1.5, alpha=0.8)
plt.text(event_time, plt.ylim()[1], ' CPI Release', color='red', 
         verticalalignment='top', fontweight='bold', fontsize=12)

# 5. Grafik Detayları
plt.title('Macro Event Impact Tracker: US CPI Surprise (Simulation)', fontsize=16, pad=20)
plt.xlabel('Time (1-Minute Intervals)', fontsize=12)
plt.ylabel('Indexed Performance (t=0 @ 100)', fontsize=12)
plt.legend(title='Assets', bbox_to_anchor=(1.05, 1), loc='upper left')

# X ekseni formatlama (Sadece saatleri gösterelim)
import matplotlib.dates as mdates
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

plt.tight_layout()

# Grafiği Kaydetme
plt.savefig('macro_impact_chart.png', dpi=300)
print("Grafik 'macro_impact_chart.png' olarak kaydedildi.")
# Not: Jupyter Notebook'ta çalışırken plt.show() eklenebilir.
