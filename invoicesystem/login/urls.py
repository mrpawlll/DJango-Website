from django.urls import path, reverse_lazy
from .views import MyLoginView,MenuPageView
from django.contrib.auth.views import LogoutView

app_name = 'login'

urlpatterns = [
    path('', MyLoginView.as_view(),name='login'),
    path('menu/', MenuPageView.as_view(),name='menu'),
    path('logout/', LogoutView.as_view(),name='logout'),
]