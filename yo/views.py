from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class YoTemplateView(TemplateView):
    template_name = "yo/base.html"
