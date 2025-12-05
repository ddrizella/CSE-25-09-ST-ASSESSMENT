from django.urls import path
from .import views
 
urlpatterns=[
    path('upload/', views.upload_song, name='upload_song')
]