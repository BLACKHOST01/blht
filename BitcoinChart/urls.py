from django.contrib import admin
from django.urls import path
from .views import (bitcoin_chart, market_cap_chart, crypto_list, coin_detail )


app_name = 'BitcoinChart'
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', bitcoin_chart, name='bitcoin_chart'),
    path('market_cap_chart/', market_cap_chart, name='market_cap_chart'),
    path('cryptoList', crypto_list, name='crypto_list'),
    path('coin/<str:coin_id>/', coin_detail, name='coin_detail'),
]
