from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm


def login_view(request):
    """
    :param request:
    :return: This function returns the login view.
    """
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to main page upon successful login
        else:
            messages.error(request, 'Invalid username or password')  # Display error message for unsuccessful login
    return render(request, 'users/login.html')


def register_view(request):
    """
    :param request:
    :return: This function returns the register view.
    """
    if request.method == 'POST':
        form = UserForm(request.POST)
        print(form.data)
        if form.is_valid():
            user = User.objects.create_superuser(
                username=form.data['email'],
                email=form.data['email'],
                password=form.data['password'],
                first_name=form.data['first_name'],
                last_name=form.data['last_name'],
            )
            user.save()  # Save the user to the database
            messages.success(request, 'Registro realizado com sucesso.')
            return redirect('login')  # Redirect to a success page
        else:
            messages.error(request, "Houve um erro no registro.")
            return render(request, 'users/register.html', {'form': form, 'form_data': request.POST})  # Redirect to a success page

    else:
        form = UserForm()
    return render(request, 'users/register.html', {'form': form})
