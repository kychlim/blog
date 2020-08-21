from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('list/', views.p_list, name='list'),
    path('create/', views.p_create, name='create'),
    path('<int:post_id>/delete/', views.p_delete, name='delete'),
    path('<int:post_id>/update/', views.p_update, name='update'),
    path('<int:post_id>/read/', views.p_read, name='read'),
    path('<int:comments_id>/c_delete/', views.c_delete, name='c_delete'),
    # path('<int:comments_id>/c_create/', views.c_create, name='c_create')

]

