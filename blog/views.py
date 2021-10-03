from django.shortcuts import render, redirect
from .forms import*
from .models import*


def Home(request):
    blogs = AddBlog.objects.all().order_by('-created')
    context = {'blogs': blogs}
    return render(request, 'home.html', context)

def Read(request, pk):
    blog = AddBlog.objects.get(pk=pk)
    context = {'blog': blog}
    return render(request, 'read.html', context)

def Create(request):
    if request.method == 'POST':
        form = AddBlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': AddBlogForm()}
    return render(request, 'add.html', context)

def Update(request, pk):
    blog = AddBlog.objects.get(id=pk)
    blogs = AddBlogForm(instance=blog)
    if request.method == 'POST':
        blogs = AddBlogForm(request.POST, instance=blog)
        if blogs.is_valid():
            blogs.save()
            return redirect('home')
    context = {'blogs': blogs}
    return render(request, 'update.html', context)

def Delete(request,pk):
    blog = AddBlog.objects.get(id=pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('home')
    context = {'blog': blog}
    return render(request, 'delete.html', context)

