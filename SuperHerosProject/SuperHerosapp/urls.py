from . import views
from django.urls import path


app_name = 'SuperHerosapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:superhero_id>', views.detail, name='detail'),
    path('new/', views.create, name='create'),
    path('change/<int:superhero_id>', views.change, name='change'),
    path('delete/<int:superhero_id>', views.delete, name='delete')
]