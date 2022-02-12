from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages

from .forms import CustomerRegistrationForm, CustomerLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


def registration(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            # customer = form.save(commit=False)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            new_user = User.objects.create_user(username, email, password)
            form.instance.user = new_user
            new_user.save()
            login(request, new_user)

            return redirect('/')
    else:
        form = CustomerRegistrationForm()
    return render(request, 'customer/registration.html', {'form': form, 'error': 'Invalid Credentials'})


def customer_logout(request):
    logout(request)
    return redirect('/')


def customer_login(request):
    form = CustomerLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'username or password not correct')
            return redirect('customer:login')
    return render(request, "customer/login.html", {'form': form})


# class CustomerView(CreateView):
#     template_name = 'customer/registration.html'
#     form_class = CustomerRegistrationForm
#     success_url = reverse_lazy('shop:product_list')
#
#     def form_valid(self, form):
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password')
#         email = form.cleaned_data.get('email')
#
#         user = User.objects.create_user(username, email, password)
#         form.instance.user = user
#         login(self.request, user)
#
#         return super().form_valid(form)

