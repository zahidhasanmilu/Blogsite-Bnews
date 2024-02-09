from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='home'),
    path('blogs/', views.BlogList.as_view(), name='bloglist'),
    path('Create-blog-page/', views.CreateBlog.as_view(), name='createblog'),
    path('blog-details/<slug>/', views.blogDetails, name='blogdetails'),
    path('my-Blogs/', views.myBlogs.as_view(), name='myblogs'),
    path('my-UpdateBlog/<pk>/', views.UpdateBlog.as_view(), name='updateblog'),
    path('<slug:slug>/delete-conformation/', views.delete_blog, name='delete_blog'),
    path('blogs_by_category/<slug:slug>/', views.blogs_by_category, name='blogs_by_category'),
    path('blogs_by_tags/<slug:slug>/', views.blogs_by_tags, name='blogs_by_tags'),
]
