
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CreatePost
from .forms import CreatePostForm

@login_required
def Add_a_Trail(request):
    if request.method == 'POST':
        create_post_form = CreatePostForm(data=request.POST, files=request.FILES)
        if create_post_form.is_valid():
            createpost = create_post_form.save(commit=False)
            createpost.Creator = request.user
            createpost.approved = False  # Ensure the post is not approved yet
            createpost.save()
            messages.add_message(request, messages.SUCCESS, 'Thank you for your post submission. Your post has been submitted successfully and is awaiting approval!')
            return redirect('trails')  # Redirect after successful post
    else:
        create_post_form = CreatePostForm()
    
    return render(
        request, 'trails/addpost.html',
        {
            "create_post_form": create_post_form,
        }
    )