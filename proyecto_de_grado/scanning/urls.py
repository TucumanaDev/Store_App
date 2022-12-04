from django.contrib import admin
from django.urls import path
from scannig.views import pingIP

urlpatterns = [
    path("", pingIP),
]