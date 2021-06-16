from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView,DeleteView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request,'blog/index.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html' # <app>/<model>_<Listview>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    
class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin ,CreateView):
    model = Post
    fields = ['title','content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def about(request):
    return render(request,'blog/about.html')