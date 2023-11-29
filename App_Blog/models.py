from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey(User, related_name='post_author', on_delete=models.CASCADE)
    blog_title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    blog_content = models.TextField(blank=True, null= True)
    blog_image = models.ImageField(upload_to='Uploaded/Blog_App/Blog_Posts_Image/')
    publish_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.blog_title} , Author: {str(self.author)}'

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

class Comment(models.Model):
    user = models.ForeignKey(User, related_name='user_comment', on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, related_name='blog_comment', on_delete=models.CASCADE)
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

class Likes(models.Model):
    user = models.ForeignKey(User, related_name='user_like', on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, related_name='blog_like', on_delete=models.CASCADE)

    def __str__(self):
        return f'{str(self.user)} -- {self.blog}'

    class Meta:
        verbose_name = 'Likes'
        verbose_name_plural = 'Likess'
