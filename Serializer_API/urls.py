from django.contrib import admin
from django.urls import path
from core.views import dataSetView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data/',dataSetView.as_view())
]
