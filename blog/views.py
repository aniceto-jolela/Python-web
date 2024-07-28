from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': 'Aniceto',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'José',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    },
    {
        'author': 'Miranda',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': 'August 29, 2018'
    },
]

def home(request):
  context = {
    'posts':Post.objects.all()
  }
  return render(request,'blog/home.html',context)

def about(request):
  return render(request,'blog/about.html', {'title': 'About'})