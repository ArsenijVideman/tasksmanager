from django.urls import path
from .views import Feature

urlpatterns = [
    path('', Feature.index, name='home'),
    path('about/', Feature.about_me, name='about'),
    path('create/', Feature.create_new_task, name='create')
]
