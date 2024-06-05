from django.contrib import admin
from django.urls import path
from article.views import home__view

urlpatterns = [
    path("", home__view, name="home"),
    path('admin/', admin.site.urls),
]
