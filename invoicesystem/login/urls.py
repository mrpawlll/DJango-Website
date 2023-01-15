from django.urls import path, reverse_lazy
from .views import MyLoginView,HomePageView
from django.contrib.auth.views import LogoutView

app_name = 'login'

urlpatterns = [
    path('login/', MyLoginView.as_view(),name='login'),
    path('', HomePageView.as_view(),name='homepage'),
    path('logout/', LogoutView.as_view(next_page = ''),name='logout'),

]