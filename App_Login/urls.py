from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register-url'),
    path('signin/', views.signin, name='signin-url'),
    path('logout/', views.signout, name='signout-url'),
    path('profile/', views.profile, name='profile-url'),
    path('profileUpdate/', views.profileUpdate, name='profileupdate-url'),
    path('addProfile_pic/', views.addProfile_pic, name='addProfile_pic-url'),
    path('update_profile_pic/', views.update_profile_pic, name='update_profile_pic-url'),

]
