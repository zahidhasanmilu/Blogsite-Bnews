from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required

from django.views.generic import CreateView, ListView, DetailView, UpdateView, View, TemplateView, DeleteView
from .models import Blog, Comment, Likes
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid

from . forms import CommentForm


class CreateBlog(LoginRequiredMixin, CreateView):
    template_name = 'App_Blog/create_blog.html'
    model = Blog
    fields = ('blog_title', 'blog_content', 'blog_image')

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
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.blog = blog_obj
            obj.save()
            return HttpResponseRedirect(reverse('blogdetails', kwargs={'slug': slug}))

    return render(request, 'App_Blog/blog_details.html', {'blog_obj': blog_obj})

class myBlogs(LoginRequiredMixin,TemplateView):
    template_name = 'App_Blog/myblogs.html'

class UpdateBlog(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name = 'App_Blog/updateblog.html'
    fields = ('blog_title', 'blog_content', 'blog_image')
    context_object_name = 'blogss'

    def get_success_url(self, **kwargs):
        return reverse_lazy('blogdetails', kwargs={'slug':self.object.slug})