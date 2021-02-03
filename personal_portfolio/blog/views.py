from django.shortcuts import render
from .models import Post, Comment

# Create your views here.
def blog_index(request):
    posts = Post.objects.all()
    
    data = {
        'posts': posts,
    }

    return render(request, 'blogs/blog_index.html', data)


def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by('-created_on')
    
    data={

        'posts': posts,
        'category': category,
    }

    return render(request, 'blogs/blog_category.html', data)

def blog_detail(request, id):
    post = Post.objects.get(pk = id)
    comments = Comment.objects.filter(post=post)

    data= {
        'post': post,
        'comments':comments,
    }

    return render(request, 'blogs/blog_detail.html', data)

