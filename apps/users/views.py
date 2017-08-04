from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from apps.users.forms import Registrationform
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    users = User.objects.all()

    data = {
        'users': users,
    }
    return render(request, 'users/index.html', data)

def create(request):
    if request.method == 'POST':
        form = Registrationform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/users/index')
    else:
        form = Registrationform()
        data = {'form': form}
        return render(request, 'users/create.html', data)

    return render(request, 'users/create.html', {})

def edit(request, id):
    user = get_object_or_404(User, id = id)

    if request.method == 'POST':
        first_name = request.POST["first_name"]
        last_name  = request.POST["last_name"]
        username   = request.POST["username"]
        email      = request.POST["email"]

        user.first_name = first_name
        user.last_name  = last_name
        user.username   = username
        user.email      = email

        user.save()

        return HttpResponseRedirect('/users/index')

    data = {
        'user': user,
    }

    return render(request, 'users/edit.html', data)

def delete(render, id):
    user = get_object_or_404(User, id = id)
    user.delete()
    return HttpResponseRedirect('/users/index')

def register_user(request):
    if request.method == 'POST':
        form = Registrationform(request.POST)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'auth/register.html', {})
