from django.urls import path
from django.contrib.auth.views import LoginView
from .forms import LoginForm

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html', authentication_form=LoginForm), name='login'),
    ]
