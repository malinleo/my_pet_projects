from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required

from .models import Test, Question


class TestsView(ListView):
    model = Test
    queryset = Test.objects.all()
    template_name = 'tests/test_list.html'


class TestDetailView(DetailView):
    model = Test
    slug_field = "url"
    template_name = 'tests/test_detail.html'
