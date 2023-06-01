from core.views import home_view, exchangeView, signupView, productCreateView,productList

from django.urls import path
from . import views



app_name = 'core'

urlpatterns = [
    path("", home_view.as_view(), name="home"),
    path("exchange/", exchangeView.as_view(), name= 'exchange'),
    path("signup/", signupView.as_view(), name= 'signup'),
    path("product/", productCreateView.as_view(), name ='product'),
    path("productlist/", productList.as_view(), name='productlist' ),
    path("login/", views.user_login, name='login'),
]
