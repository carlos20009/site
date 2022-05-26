from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', TemplateView.as_view(template_name="blog/index.html")),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    ]