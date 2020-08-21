from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Post, Comments
from posts.forms import PostForm, CommentsForm


def p_list(request):
    my_list = Post.objects.all().order_by('-id')
    context = {'posts': my_list}
    return render(request, 'list.html', context)


def p_create(request):

    if request.method == 'POST':  # POST 방식으로 호출될 때
        post_form = PostForm(request.POST)

        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.auth_author = request.user
            post.save()
            return redirect('posts:list')

    else:         # GET 방식으로 호출될 때
        post_form = PostForm()

    return render(request, 'create.html', {'post_form': post_form})

 # form외에는 다 get방식이라고 보면 됨/


def p_delete(request, post_id):
    post = Post.objects.get(id=post_id)   # id대신 pk로 해도 됨
    post.delete()

    return redirect('posts:list')


def p_update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)

        if post_form.is_valid():
            post_form.save()
            return redirect('posts:list')

    else:
        post_form = PostForm(instance=post)

    return render(request, 'create.html', {'post_form': post_form})

def p_read(request, post_id):

    post = Post.objects.get(id=post_id)
    comments = post.comments_set.all()              ## 여기서 계속 애먹었었음

    if request.method == 'POST':  # POST 방식으로 호출될 때
        comments_form = CommentsForm(request.POST)
        if comments_form.is_valid():
            com = comments_form.save(commit=False)
            com.post_id = post.pk
            com.save()
            return redirect('posts:read', post_id=post.pk)

    else:
        comments_form = CommentsForm()

    context = {"post": post,
               "comments": comments,
               "Comments_Form": comments_form}

    return render(request, 'contents.html', context)




def c_delete(request, comments_id):
    comments = Comments.objects.get(id=comments_id)
    comments.delete()

    return redirect('posts:read', post_id=comments.post_id)

