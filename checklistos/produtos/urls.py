from django.urls import path

from checklistos.produtos import views


app_name = 'produtos'
urlpatterns = [
    path('', views.index, name='index'),
]
