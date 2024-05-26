from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ContactUsForm
from .models import ContactUs, RESOLVED_CHOICES
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse



#Contact form view for logged in users only


@login_required
def contact_us(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            messages.success(request, 'Thank you for reaching out, your query has been successfully submitted and will be reviewed by our admin team.')
            return render(request, 'contact/contact_us.html', {'form': ContactUsForm(), 'success': True})
    else:
        form = ContactUsForm()
    return render(request, 'contact/contact_us.html', {'form': form})

