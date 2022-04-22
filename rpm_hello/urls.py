from django.contrib import admin
from django.urls import path

from yo.views import YoTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", YoTemplateView.as_view())
]
