from multiprocessing import context
from unicodedata import category
from django.shortcuts import get_object_or_404, redirect, render
from blog.models import Category, Post
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import CategoryModelForm, PostModelForm
from django.contrib import messages


# Create your views here.

def HomeVeiw(request):
    featuredPosts = Post.objects.order_by('-id')[:3]
    PostList = Post.objects.order_by('-id')
    Categories = Category.objects.order_by('-id')

    paginator = Paginator(PostList, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        'featuredPosts': featuredPosts,
        'posts': posts,
        'Categories': Categories
    }
    return render(request, "blog/index.html", context)
    
@login_required
# Display category list
def CategoryViewList(request):
    cat = Category.objects.order_by('-id')
    
    context = {
        'categories': cat
    }
    print(cat)
    return render(request, 'blog/category.html', context)

@login_required
def CategoryUpdateView(request, pk):
    cat_id = get_object_or_404(Category, pk=pk)
    form = CategoryModelForm(request.POST or None, instance=cat_id)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.updated_by = request.user.id
        obj.save()
        messages.success(request, "Category Updated Successfully.")
        return redirect("/category/")
    context = {
        'form': form,
        'valueBtn': "Update",
        'title': "Update Category"
    }
    return render(request, "blog/category-form.html", context)

@login_required
def CategoryDeleteView(request, pk):
    query = get_object_or_404(Category, pk=pk)
    query.delete()
    messages.success(request, f"You Successed to delete this category {query}.")
    return redirect("/category/")

@login_required
def CategoryCreateView(request):
    form = CategoryModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.created_by = request.user.id
        obj.save()
        messages.success(request, "Category Added Successfully.")
        return redirect("/category/")
    context = {
        'form': form,
        'valueBtn': "Add",
        'title': "Add New Category"
    }
    return render(request, "blog/category-form.html", context)

@login_required
def PostCreateView(request):
    form = PostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.created_by = request.user.username
        obj.save()
        messages.success(request, "Post created Successfully")
        return redirect("/")

    context = {
        "form" : form,
        "valueBtn": "Add",
        "title": "Created Post"
    }
    return render(request, "")
