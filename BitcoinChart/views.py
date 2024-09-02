# Create your views here.
import requests
from .utils import get_crypto_prices
from django.shortcuts import render
from .sparkline_generator import generate_sparkline
import json

def bitcoin_chart(request):
    # Fetch Bitcoin price data from CoinGecko API
    url = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=30&interval=daily'
    response = requests.get(url)
    data = response.json()

    # Extract prices and dates, handling potential missing 'prices' key
    prices = data.get('prices', [])
    dates = [price[0] for price in prices]
    prices = [price[1] for price in prices]

    context = {
        'prices': prices,
        'dates': dates,
    }

    return render(request, 'regx/chart.html', context)





def market_cap_chart(request):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1,
        "sparkline": False
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    labels = [coin['name'] for coin in data]
    market_caps = [coin['market_cap'] for coin in data]
    
    context = {
        'labels': labels,
        'market_caps': market_caps,
    }
    
    return render(request, 'crypto/market_cap_chart.html', context)


def generate_market_cap_chart(coin_data):
    labels = [entry['date'] for entry in coin_data]
    market_cap_values = [entry['market_cap'] for entry in coin_data]
    
    chart_data = {
        'labels': labels,
        'datasets': [{
            'label': 'Market Cap',
            'data': market_cap_values,
            'borderColor': 'rgb(75, 192, 192)',
            'tension': 0.1
        }]
    }
    
    return json.dumps(chart_data)


def crypto_list(request):
    crypto_data = get_crypto_prices()
    return render(request, 'crypto/crypto_list.html', {'crypto_data': crypto_data})



def coin_detail(request, coin_id):
    crypto_data = get_crypto_prices()
    coin = next((coin for coin in crypto_data if coin['id'] == coin_id), None)
    context = {
        'coin': coin,
        'market_cap_chart': market_cap_chart
    }
    # Implement the get_market_cap_history function or import it if it's defined elsewhere
    from .utils import get_market_cap_history  # Assuming it's defined in a utils.py file
    
    market_cap_history = get_market_cap_history(coin_id)
    return render(request, 'crypto/coin_detail.html', context)
# 