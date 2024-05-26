
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import generic
from .models import CreatePost
from .forms import CreatePostForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse



@login_required
def Add_a_Trail(request):
    if request.method == 'POST':
        create_post_form = CreatePostForm(request.POST, request.FILES)
        if create_post_form.is_valid():
            createpost = create_post_form.save(commit=False)
            createpost.Creator = request.user
            createpost.approved = False  
            createpost.save()
            messages.add_message(request, messages.SUCCESS, 'Thank you for your post submission. Your post has been submitted successfully and is awaiting approval!')
            return redirect('trails')  
    else:
        create_post_form = CreatePostForm()
    
    return render(
        request, 'trails/addpost.html',
        {
            "create_post_form": create_post_form,
        }
    )