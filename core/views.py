from django.shortcuts import render, redirect
from django.views.generic import View,TemplateView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin #para Classes Based Views
from django.contrib.auth.decorators import login_required #para Functions Based Views

from django.db.models import Sum, Avg, F
from django.db.models.functions import Coalesce


import json
import datetime

from core.models import Reporter, Article

# Create your views here.
class IndexTemplateView(TemplateView):
    template_name = "core/index.html"