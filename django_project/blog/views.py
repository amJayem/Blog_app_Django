from django.shortcuts import render


posts = [
    {
        'author': 'Jayem',
        'title': 'blog post 1',
        'content': 'first post content',
        'date': 'jun 11, 2021',
    },

    {
        'author': 'Mahmud',
        'title': 'blog post 2',
        'content': 'second post content',
        'date': 'jun 11, 2021',
    }
]

def home(request):
    context = {
        'posts': posts,
    }
    return render(request,'blog/index.html',context)

def about(request):
    return render(request,'blog/about.html')