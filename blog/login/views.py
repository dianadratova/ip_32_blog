from django.shortcuts import render,redirect
from .models import User,Role
from .forms import UserForm, RoleForm


def users(request):
    users = User.objects.all()
    return render (request, 'user.html', {'users': users})
# def role(request):
#     role=Role.objects.all()
#     return render(request,'role.html', {'role': role})

def add_user(request):
    if request.method == "POST":
        user = UserForm(request.POST)
        if user.is_valid():
            user.save()
        return redirect('/users/')
    else:
        form = UserForm()
        return render (request, "add_user.html", {'form': form})
# Create your views here.
def add_role(request):
    if request.method == "POST":
        role = RoleForm(request.POST)
        if role.is_valid():
            role.save()
        return redirect('/users/')
    else:
        form = RoleForm()
        return render (request, "add_role.html", {'form': form})

