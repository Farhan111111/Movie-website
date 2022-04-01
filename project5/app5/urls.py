from django.urls import path
from . import views

app_name = 'app5'
urlpatterns = [
    path('', views.fun1, name='fun1'),
    path('movie/<int:movie_list>/', views.fun2, name='fun2'),
    path('add/', views.add_movie, name='add_movie'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]
