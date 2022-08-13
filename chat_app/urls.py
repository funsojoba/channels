from .views import index
from django.urls import path


urlpatterns = [
    path('<str:room_name>', index, name='index'),
]
