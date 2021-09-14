from django.urls import path, include
from basic_app import views 

#Template Tagging
app_name = 'basic_app' #app name

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other')
]
