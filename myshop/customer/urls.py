from django.urls import path
from . import views
from .views import CustomerRegisterView
from .views import CustomerLoginView

app_name = 'customer'

urlpatterns = [
    path('register/', CustomerRegisterView.as_view(), name='registration'),
    path('logout/', views.customer_logout, name='logout'),
    path('login/', CustomerLoginView.as_view(), name='login'),
]