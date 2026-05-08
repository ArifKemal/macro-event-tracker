import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 1. Zaman Parametrelerinin Ayarlanması
event_time = datetime(2024, 5, 15, 15, 30)
start_time = event_time - timedelta(hours=1)
end_time = event_time + timedelta(hours=2)
timestamps = pd.date_range(start=start_time, end=end_time, freq='1min')

n_points = len(timestamps)
event_idx = list(timestamps).index(event_time)

# 2. Mock Data Fonksiyonu
def generate_asset_path(start_price, shock_pct, drift, volatility, n_points, event_idx):
    prices = [start_price]
    for i in range(1, n_points):
        change = np.random.normal(drift, volatility)
        if i == event_idx:
            change += shock_pct
        new_price = prices[-1] * (1 + change)
        prices.append(new_price)
    return prices

# 3. Varlıkların Simüle Edilmesi
np.random.seed(42)

data = {
    'Timestamp': timestamps,
    'SPY': generate_asset_path(520.0, -0.015, -0.0001, 0.0008, n_points, event_idx),
    'DXY': generate_asset_path(105.0, 0.008, 0.00005, 0.0004, n_points, event_idx),
    'US10Y': generate_asset_path(4.5, 0.02, 0.0001, 0.0015, n_points, event_idx),
    'VIX': generate_asset_path(14.0, 0.10, 0.0002, 0.005, n_points, event_idx)
}

# 4. DataFrame Oluşturma ve Kaydetme
df = pd.DataFrame(data)
df.to_csv('macro_event_data.csv', index=False)
print("macro_event_data.csv başarıyla oluşturuldu.")
