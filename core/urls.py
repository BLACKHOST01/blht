from core.views import(home_view,
                       exchangeView,
                       signup, 
                       productCreateView,
                       productList,
                       dashboard)

from django.urls import path
from . import views



app_name = 'core'

urlpatterns = [
    path("", home_view.as_view(), name="home"),
    path("exchange/", exchangeView.as_view(), name= 'exchange'),
    path("signup/", views.signup, name= 'signup'),
    path("product/", productCreateView.as_view(), name ='product'),
    path("productlist/", productList.as_view(), name='productlist' ),
    path("login/", views.log_in, name='login'),
    path("logout/", views.log_out, name="logout"),
    path("dashboard/p", views.dashboard, name='dashboard')
    
    
    
]
