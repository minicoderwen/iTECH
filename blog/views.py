from django.shortcuts import render
from .models import Blog
from .forms import BlogForm


def index(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        else:
            print(form.errors)

        context_dict = {'message': "have a good day"}
        # 得到所有的blogs
        blogs = Blog.objects.all()
        context_dict['blogs'] = blogs
        # 将表单传递给模板
        form = BlogForm()
        context_dict['form'] = form

        return render(request, 'blog/index.html', context=context_dict)


    else:

        context_dict = {'message': "have a good day"}
        # 得到所有的blogs
        blogs = Blog.objects.all()
        context_dict['blogs'] = blogs
        # 将表单传递给模板
        form = BlogForm()
        context_dict['form'] = form

        return render(request, 'blog/index.html', context=context_dict)