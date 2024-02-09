from django.shortcuts import get_object_or_404, redirect, render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required

from django.views.generic import CreateView, ListView, DetailView, UpdateView, View, TemplateView, DeleteView
from .models import Blog, Comment, Likes, Catagory,Tag
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
from django.db.models import Q

from . forms import CommentForm
from django.contrib import messages



class CreateBlog(LoginRequiredMixin, CreateView):
    template_name = 'App_Blog/create_blog.html'
    model = Blog
    fields = ('blog_title', 'catagori_name', 'tags','blog_content', 'blog_image')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        title = obj.blog_title
        obj.slug = title.replace(' ', '-') + "-" + str(uuid.uuid4())
        obj.save()
        return HttpResponseRedirect(reverse('home'))


# Create your views here.
def index(request):
    return HttpResponseRedirect(reverse('bloglist'))


class BlogList(ListView):
    template_name = 'App_Blog/blogs.html'
    model = Blog
    context_object_name = 'blogs'


@login_required
def blogDetails(request, slug):
    blog_obj = Blog.objects.get(slug=slug)
    cat_blog = Blog.objects.filter(Q(catagori_name = blog_obj.catagori_name)).exclude(pk = blog_obj.pk)
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.blog = blog_obj
            obj.save()
            return HttpResponseRedirect(reverse('blogdetails', kwargs={'slug': slug}))

    return render(request, 'App_Blog/blog_details.html', {'blog_obj': blog_obj, 'cat_blog':cat_blog,'current_user':current_user})

class myBlogs(LoginRequiredMixin,TemplateView):
    template_name = 'App_Blog/myblogs.html'

class UpdateBlog(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name = 'App_Blog/updateblog.html'
    fields = ('blog_title', 'blog_content','tags','catagori_name', 'blog_image')
    context_object_name = 'blogss'

    def form_valid(self, form):
        messages.success(self.request, f'{form.instance.blog_title} update was successful.')
        return super().form_valid(form)

    def get_success_url(self,**kwargs):      
        return reverse_lazy('blogdetails', kwargs={'slug':self.object.slug})


# def liked(request,pk):
#     blog = Blog.objects.get(pk=pk)
#     user = request.user

#     already_liked = Blog.objects.filter (blog=blog, user=user)
#     if not already_liked:
#         like_post = Likes(blog=blog, user=user)
#         like_post.save()
#     return HttpResponseRedirect(reverse('blogdetails', kwargs={'slug':blog.slug}))

# def unlike(request, pk):
#     blog = Blog.objects.get(pk=pk)
#     user = request.user
#     already_liked = Blog.objects.filter (blog=blog, user=user)
#     already_liked.delete()
#     return HttpResponseRedirect(reverse('blogdetails'kwargs={'slug':blog.slug}))


@login_required
def delete_blog(request, slug):
    blog = get_object_or_404(Blog, slug=slug)

    if request.method == 'POST':
        blog.delete()
        return redirect('profile-url')  # Change this to the appropriate URL

    return render(request, 'App_Blog/delete_blog.html', {'title': 'Delete Blog', 'blog': blog}) 

def blogs_by_category(request, slug):
    category = Catagory.objects.get(slug=slug)
    blogs = Blog.objects.filter(catagori_name=category.pk)
    print(blogs)

    context = {
        'category': category,
        'blogs': blogs,
    }

    return render(request, 'App_Blog/blogs_by_category.html', context)

def blogs_by_tags(request, slug):
    tag = Tag.objects.get(slug=slug)
    blogs = Blog.objects.filter(tags=tag)
    print(blogs)

    context = {
        'tags': tag,
        'blogs': blogs,
    }

    return render(request, 'App_Blog/blogs_by_tags.html', context)