from django.urls import path

from post import views

urlpatterns = [

    path('hello/',views.hello_django_bbs)
]