from django.shortcuts import render
from django.views.generic import CreateView


# Create your views.py here.
class RegisterView(CreateView):
    print('Test verions')