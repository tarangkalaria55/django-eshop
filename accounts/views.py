from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import CustomUser

# Create your views here.
# @login_required
# def handle_login(request: HttpRequest):
#     # if the user has a freelance/biz acct -> take them to home
#     print(request.user)
#     return render(request, "0.html")


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "0.html"
