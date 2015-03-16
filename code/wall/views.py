from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm
from .models import Post, Comment


def example_html_view(request):
    return render(request, 'example_view.html', {})


def post_list(request):
    posts = Post.objects.all()
    return render(
        request,
        'wall/post_list.html', {
            'wall_posts': posts,
        }
    )


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(
        request,
        'wall/post_details.html', {
            'post': post,
        }
    )


def post_write_new(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_wall')
    else:
        form = PostForm()

    return render(
        request,
        'wall/post_new.html', {
            'form': form,
        }
    )


def comment_write_new(request, post_pk):
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Post.objects.get(pk=post_pk)
            comment.save()
            return redirect('post_detail', pk=post_pk)
    else:
        form = CommentForm()

    return render(
        request,
        'wall/comment_new.html', {
            'form': form,
            'post_pk': post_pk,
        }
    )


def comment_edit(request, pk):

    obj = get_object_or_404(Comment, pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=obj.post.pk)
    else:
        form = CommentForm(instance=obj)

    return render(
        request,
        'wall/comment_edit.html', {
            'form': form,
        }
    )
