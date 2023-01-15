from django.urls import path, reverse_lazy
from .views import MyLoginView,HomePageView,MenuPageView
from django.contrib.auth.views import LogoutView

app_name = 'login'

urlpatterns = [
    path('login/', MyLoginView.as_view(),name='login'),
    path('', HomePageView.as_view(),name='homepage'),
    path('menu/',MenuPageView.as_view(),name='menu'),
    path('logout/', LogoutView.as_view(),name='logout'),
    
]