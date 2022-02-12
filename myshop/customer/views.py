from django.shortcuts import render, redirect
from .forms import CustomerRegistrationForm
from django.contrib.auth.models import User


def registration(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            new_user = User.objects.create(username=username, email=email, password=password)
            form.instance.user = new_user
            customer.save()
            return redirect('/')
    else:
        form = CustomerRegistrationForm()
    return render(request, 'customer/registration.html', {'form': form})


