import pandas as pd
import numpy as np

# 1. Veriyi Yükleme
df = pd.read_csv('macro_event_data.csv')
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# 2. Olay Anının Belirlenmesi (t=0)
# Mock datada 15:30 olarak ayarlamıştık
event_time = pd.Timestamp(2024, 5, 15, 15, 30)

# 3. Normalizasyon (Indexing to 100 at t=0)
# Amacımız her varlığın t=0 anındaki değerini 100 yapmak ve sonrasını buna göre oranlamak.
assets = ['SPY', 'DXY', 'US10Y', 'VIX']
df_norm = df.copy()

for asset in assets:
    # Olay anındaki fiyatı bul
    base_price = df.loc[df['Timestamp'] == event_time, asset].values[0]
    
    # Tüm seriyi bu fiyata bölüp 100 ile çarp (Indexed Return)
    # Formül: (Fiyat_t / Fiyat_event) * 100
    df_norm[f'{asset}_idx'] = (df[asset] / base_price) * 100

# 4. Alternatif: Yüzdesel Değişim (Cumulative Return from t=0)
# Bu da t=0'ı 0% yapar, sonrasını % değişim olarak gösterir.
for asset in assets:
    base_price = df.loc[df['Timestamp'] == event_time, asset].values[0]
    df_norm[f'{asset}_pct'] = (df[asset] / base_price - 1) * 100

# Sonuçları kontrol edelim
print("Normalizasyon Tamamlandı.")
print(f"Olay anındaki ({event_time}) değerler 100'e sabitlendi.")
print(df_norm[df_norm['Timestamp'] == event_time][['Timestamp'] + [f'{a}_idx' for a in assets]])
df_norm.to_csv('macro_event_processed.csv', index=False)
