from django.shortcuts import render, HttpResponseRedirect
from apps.users.forms import Registrationform

# Create your views here.
def index(request):

    data = {}
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