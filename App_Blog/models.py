from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from autoslug import AutoSlugField
# import uuid


# Create your models here.


class Catagory(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    class Meta:
        verbose_name = 'Catagory'
        verbose_name_plural = 'Catagories'

class Tag(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Blog(models.Model):
    author = models.ForeignKey(
        User, related_name='post_author', on_delete=models.CASCADE)
    catagori_name = models.ForeignKey(
        Catagory, related_name='catagori_blog', on_delete=models.CASCADE, blank=True, null=True)
    blog_title = models.CharField(max_length=1000)
    tags = models.ManyToManyField(Tag,blank=True, related_name='tag_blogs')
    slug = AutoSlugField(populate_from='blog_title', unique=True)
    # slug = models.SlugField(unique=True, blank=True, null=True)
    blog_content = models.TextField(blank=True, null=True)
    blog_image = models.ImageField(
        upload_to='Uploaded/Blog_App/Blog_Posts_Image')
    publish_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def save(self, *args, **kwargs):
    #     # Generate a UUID
    #     unique_id = uuid.uuid4()
    #     title = slugify(self.blog_title)
        
    #     # Convert the UUID to a string and slugify it        
    #     self.slug = title.replace(' ', '-') + "-" + (str(unique_id))[0:6]
    #     # self.slug = slugify(t)+'-'+(str(unique_id))[0:6]
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.blog_title} , Author: {str(self.author)}'

    class Meta:
        ordering = ['-publish_date']
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'


class Comment(models.Model):
    user = models.ForeignKey(
        User, related_name='user_comment', on_delete=models.CASCADE)
    blog = models.ForeignKey(
        Blog, related_name='blog_comment', on_delete=models.CASCADE)
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class Likes(models.Model):
    user = models.ForeignKey(
        User, related_name='user_like', on_delete=models.CASCADE)
    blog = models.ForeignKey(
        Blog, related_name='blog_like', on_delete=models.CASCADE)

    def __str__(self):
        return f'{str(self.user)} -- {self.blog}'

    class Meta:
        verbose_name = 'Likes'
        verbose_name_plural = 'Likess'
