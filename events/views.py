from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import EventRegistrationForm


def event_registration(request):
    if request.method == 'POST':
        form = EventRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('registration_success'))
    else:
        form = EventRegistrationForm()

    return render(request, 'events/register.html', {'form': form})


def registration_success(request):
    return render(request, 'events/success.html')
