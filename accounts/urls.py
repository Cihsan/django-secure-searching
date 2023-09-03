from django.urls import path
from . import views 
urlpatterns = [
    path('login/', views.login, name='login'),    
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    # path('resetPassword/', views.resetPassword, name='resetPassword'),
    # path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
    
    path('register/', views.register, name='register'),
    # path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('delete/<int:id>/', views.delete_content,name='delete_content'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.dashboard, name='dashboard'),
    path('', views.delete_content, name='delete_content'),
    # path('edit_profile/', views.edit_profile, name='edit_profile'),
    
]