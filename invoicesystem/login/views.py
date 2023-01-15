from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import generic
from django.views.generic.base import TemplateView

class MyLoginView(LoginView):
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('login:homepage')
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))


class HomePageView(TemplateView):
    template_name = "homepage/homepage.html"

class MenuPageView(TemplateView):
    template_name = "homepage/menu.html"

