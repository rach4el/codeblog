from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ContactUs
from .forms import ContactUsForm
from django.urls import reverse

@login_required
def contact_us(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST, request.FILES)
        if form.is_valid():
            form.request = request
            contact_us = form.save(commit=False)
            contact_us.author = request.user
            contact_us.save()
            messages.add_message(request, messages.SUCCESS, 'Your query has been submitted successfully!')
            return redirect('contact_us')
        else:
            print("Form invalid")
            for field, errors in form.errors.items():
                for error in errors:
                    print(f"Error in {field}: {error}")
    else:
        form = ContactUsForm()
    
    # This gets the current logged in users submission and displays them by passing them to the template
    user_submissions = ContactUs.objects.filter(author=request.user)

    return render(request, 'contact/contact_us.html', {
        'form': form,
        'submissions': user_submissions 
    })

@login_required
def edit_submission(request, submission_id):
    submission = get_object_or_404(ContactUs, id=submission_id, author=request.user)
    if request.method == 'POST':
        form = ContactUsForm(request.POST, request.FILES, instance=submission)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your submission has been updated successfully!')
            return redirect('contact_us')
    else:
        form = ContactUsForm(instance=submission)
    
    return render(request, 'contact/edit_submission.html', {'form': form, 'submission': submission})

@login_required
def confirm_delete(request, submission_id):
    submission = get_object_or_404(ContactUs, id=submission_id, author=request.user)
    if request.method == 'POST':
        submission.delete()
        messages.add_message(request, messages.SUCCESS, 'Your submission has been deleted successfully!')
        return redirect('contact_us')
    
    return render(request, 'contact/confirm_delete.html', {'submission': submission})