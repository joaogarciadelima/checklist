from django.urls import path

from checklistos.servicos import views


app_name = 'servicos'
urlpatterns = [
    path('', views.index, name='index'),
]
