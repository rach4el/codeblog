from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm

# About page information text and collaborate form


def about_me(request):
    """
    Renders the About page
    """
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(request,
                                 messages.SUCCESS,
                                 "Thank you for submitting your collaboration request, please await a response within 3 business days")

    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form
        },
    )
