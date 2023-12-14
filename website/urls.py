from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.project_record, name='record'),
    path('delete_project/<int:pk>', views.delete_project, name='delete_project'),
    path('add_project/', views.add_project, name='add_project'),
    path('update_project/<int:pk>', views.update_project, name='update_project'),
]