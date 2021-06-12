from django.contrib.auth.forms import UserCreationForm
from core.models import User
from django.contrib.auth import get_user_model
from django.views.generic import CreateView
from django.urls import reverse_lazy

User= get_user_model()
# Create your views here.


class SignUpView(CreateView):
    form_class= UserCreationForm
    success_url= reverse_lazy('login')
    template_name= 'registration/signup.html'