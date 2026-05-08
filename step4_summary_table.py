import pandas as pd

# 1. Veriyi Yükleme
df = pd.read_csv('macro_event_processed.csv')
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# 2. Zaman Noktalarının Belirlenmesi
event_time = pd.Timestamp(2024, 5, 15, 15, 30)
t_15 = event_time + pd.Timedelta(minutes=15)
t_60 = event_time + pd.Timedelta(minutes=60)

# 3. Özet Tablosunun Hazırlanması
summary_data = []
assets = ['SPY', 'DXY', 'US10Y', 'VIX']

for asset in assets:
    # t=15 ve t=60'daki yüzdesel değişimleri al (zaten _pct olarak hesaplamıştık)
    pct_15 = df.loc[df['Timestamp'] == t_15, f'{asset}_pct'].values[0]
    pct_60 = df.loc[df['Timestamp'] == t_60, f'{asset}_pct'].values[0]
    
    summary_data.append({
        'Asset': asset,
        '15-Min Impact (%)': round(pct_15, 2),
        '60-Min Impact (%)': round(pct_60, 2)
    })

summary_df = pd.DataFrame(summary_data)

# 4. Tabloyu Güzelleştirelim (Görünüm amaçlı)
print("\n--- MACRO EVENT IMPACT SUMMARY ---")
print(summary_df.to_string(index=False))

# CSV olarak da kaydedelim (Opsiyonel)
summary_df.to_csv('event_impact_summary.csv', index=False)
