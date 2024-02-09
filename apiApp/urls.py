from django.urls import path

from .import views

urlpatterns = [
    path('blogsapi/', views.BlogApiList.as_view(), name="blogapiList"),
    path('usersapi/', views.User_ProfileApiList.as_view(), name="usersapiList"),
]
