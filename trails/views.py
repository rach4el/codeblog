
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import generic
from .models import CreatePost
from .forms import CreatePostForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse

# View for the suggest page

@login_required
def Add_a_Trail(request):
    if request.method == 'POST':
        create_post_form = CreatePostForm(request.POST, request.FILES)
        if create_post_form.is_valid():
            createpost = create_post_form.save(commit=False)
            createpost.creator = request.user
            createpost.approved = False  
            createpost.save()
            messages.add_message(request, messages.SUCCESS, 'Thank you for your suggestion. Your submission has been successfully passed on to our admin team and is awaiting approval!')
            return redirect('suggest')  
        else:
            print("Form invalid")
            for field, errors in create_post_form.errors.items():
                for error in errors:
                    print(f"Error in {field}: {error}")
    else:
        create_post_form = CreatePostForm()
    
    return render(
        request, 'trails/suggestpost.html',
        {
            "create_post_form": create_post_form,
        }
    )