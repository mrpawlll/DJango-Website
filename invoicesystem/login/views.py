from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import generic
from django.views.generic.base import TemplateView

class MyLoginView(LoginView):
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('login:menu')
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))


class MenuPageView(LoginRequiredMixin,TemplateView):
    template_name = "homepage/menu.html"
    login_url = reverse_lazy('login:login')
    
    def get_login_url(self):
        login_url = reverse_lazy('login:login')
        return login_url

class NoAccessView(LoginRequiredMixin,TemplateView):
    template_name="homepage/noaccess.html"
    login_url = reverse_lazy('login:noaccess')
