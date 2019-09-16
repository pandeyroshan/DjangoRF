from django.contrib import admin
from django.urls import path
from core.views import dataSetView
from core.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data/',dataSetView.as_view()),
    path('login/',login)
]
