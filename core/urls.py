from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_person, name='index'),
    #path('export/', views.export_users_xls, name='export'),
]
