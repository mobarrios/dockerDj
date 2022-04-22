from django.urls import path
from gestor.views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('clients/',clients, name='clients'),
    path('login/',login, name='login'),

    # path('end/<int:ano>/<int:actual>', chau), #pasar parametros 
    # path('hija1/',hija1),
    # path('search/',search)
]

