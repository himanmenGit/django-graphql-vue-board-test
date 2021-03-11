from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

User = get_user_model()


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('board_list')
    else:
        form = UserForm()

    for fieldname in ['username', 'password1', 'password2']:
        form.fields[fieldname].help_text = None
    return render(request, 'registration/signup.html', {'form': form})
