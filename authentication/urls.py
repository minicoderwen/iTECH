from django.urls import path
from authentication import views

app_name = 'authentication'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('set_username/', views.set_username, name='set_username'),
    path('set_email/', views.set_email, name='set_email'),
    path('set_avatar/', views.set_avatar, name='set_avatar'),
    path('set_password/', views.set_password, name='set_password'),
    path('block_user/<int:user_id>', views.block_user, name='block_user'),
    path('password_reset/', views.password_reset, name='password_reset'),
    
    path('password_reset_confirm/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
]
