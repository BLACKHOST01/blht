
import requests
import time
from .sparkline_generator import generate_sparkline

def get_crypto_prices():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 110,
    "page": 1,
    "sparkline": False,
    "price_change_percentage": "1h,24h,7d",
    "include_24hr_vol": True,
    "include_market_cap": True,
    "include_ath": True,
    "include_ath_change_percentage": True,
    "include_24hr_high_low": True,
    "include_7d_high_low": True
}

    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        for coin in data:
            coin['price_change_percentage_1h'] = coin.get('price_change_percentage_1h_in_currency', 0)
            coin['price_change_percentage_24h'] = coin.get('price_change_percentage_24h_in_currency', 0)
            coin['price_change_percentage_7d'] = coin.get('price_change_percentage_7d_in_currency', 0)
            coin['market_cap'] = coin.get('market_cap', 0)
            coin['volume_24h'] = coin.get('total_volume', 0)
            coin['circulating_supply'] = coin.get('circulating_supply', 0)
            sparkline_data = coin.get('sparkline_in_7d', {}).get('price', [])
            coin['sparkline'] = generate_sparkline(sparkline_data)
     
            
            for period in ['1h', '24h', '7d']:
                change = coin[f'price_change_percentage_{period}']
                coin[f'price_change_color_{period}'] = 'green' if change >= 0 else 'red'
        
        return data
    else:
        print(f"Error: Unable to fetch data. Status code: {response.status_code}")
        return None


def get_market_cap_history(coin_id):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart?vs_currency=usd&days=30&interval=daily"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        market_cap_history = [
            {"date": entry[0], "market_cap": entry[1]}
            for entry in data["market_caps"]
        ]
        return market_cap_history
    else:
        return []
