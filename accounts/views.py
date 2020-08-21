from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from accounts.forms import UserForm
# from django.contrib import auth

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('accounts:login')
    else:
        form = UserForm()
    return render(request, 'accounts/signup.html', {'form': form})

# def signup(request):
#     pass
#     if request.method == "POST":
#         if request.POST["password1"] == request.POST['password2']:
#             user = User.object.creat_user(
#                 username=request.POST["username"], password=request.POST['password1'])
#             auth.login(request, user)
#             return redirect('home')
#         return render(request, 'signup.html')
#     return render(request, 'signup.html')


# def login(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(request, username=username, password=password)
#         if user is not None:
#             auth.login(request, user)
#             return redirect('home')
#         else:
#             return render(request, 'login.html', {'error': 'username of password is incorrect'})
#     else:
#         return render(request, 'login.html')
#
#
# def logout(request):
#     auth.logout(request)
#     return redirect('home')
# #
