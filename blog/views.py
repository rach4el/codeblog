from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Post, Comment, SUGGESTED_RIDING_ABILITY, Upvote, Downvote
from .forms import CommentForm, PostForm
from django.shortcuts import redirect
from django.urls import reverse


# Create your views here.

# Upvote /downvote

@login_required
def upvote_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user in post.downvotes.all():
        Downvote.objects.filter(user=request.user, post=post).delete()
    if not Upvote.objects.filter(user=request.user, post=post).exists():
        Upvote.objects.create(user=request.user, post=post)
    return redirect('post_detail', slug=slug)


@login_required
def downvote_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user in post.upvotes.all():
        Upvote.objects.filter(user=request.user, post=post).delete()
    if not Downvote.objects.filter(user=request.user, post=post).exists():
        Downvote.objects.create(user=request.user, post=post)
    return redirect('post_detail', slug=slug)

# Post form function


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.request = request
            post = form.save(commit=False)
            post.status = 3
            post.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Thank you for your post submission.Your post has been submitted successfully and is awaiting approval!')
            return redirect('/create/')
        else:
            print("form invalid")
            for field, errors in form.errors.items():
                for error in errors:
                    print(f"Error in {field}: {error}")
    else:

        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

# Post list view


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog/index.html"
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        suggested_riding_ability = self.request.GET.get('suggested_riding_ability')
        county = self.request.GET.get('county')

        if suggested_riding_ability:
            queryset = queryset.filter(suggested_riding_ability=suggested_riding_ability)
        if county:
            queryset = queryset.filter(county=county)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['SUGGESTED_RIDING_ABILITY'] = dict(SUGGESTED_RIDING_ABILITY)
        context['counties'] = Post.objects.values_list('county', flat=True).distinct()
        return context

# Post detail function


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(
                request, messages.ERROR,
                'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):

    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))