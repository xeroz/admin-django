from django.shortcuts import render

# Create your views here.
def home(request):
    data = {'user' : request.user}
    return render(request, 'home.html', data)