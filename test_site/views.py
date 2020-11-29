from django.shortcuts import render
from django.views.generic.base import View

from .models import Test


class TestsView(View):
    def get(self, request):
        tests = Test.objects.all()
        return render(request, "tests/test_list.html", {"test_list": tests})


class TestDetailView(View):
    def get(self, request, slug):
        test = Test.objects.get(url=slug)
        return render(request, "tests/test_detail.html", {"test": test})
