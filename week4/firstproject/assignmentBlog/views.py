from django.shortcuts import render,get_object_or_404
from .models import Blog

# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    return render(request, 'blogHome.html', {'blogs':blogs})

def detail(request, id):
    blog = get_object_or_404(Blog,pk = id)
    return render(request, 'blogDetail.html', {'blog':blog})
