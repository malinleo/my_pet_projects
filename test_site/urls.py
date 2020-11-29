from django.urls import path

from . import views


urlpatterns = [
    path("", views.TestsView.as_view(), name="tests"),
    path("<slug:slug>/", views.TestDetailView.as_view(), name="test_detail"),
]