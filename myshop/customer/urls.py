from django.urls import path
from . import views
# from .views import CustomerView

app_name = 'customer'

urlpatterns = [
    path('register/', views.registration, name='registration'),
    path('logout/', views.customer_logout, name='logout'),
    path('login/', views.customer_login, name='login'),
]