from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from apps.teams.forms import TeamForm
from apps.teams.models import Team

# Create your views here.
def index(request):

    teams = Team.objects.all()

    data = {
        'teams': teams,
    }
    return render(request, 'teams/index.html', data)

def create(request):

    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/users/index')
    else:
        form = TeamForm()
        data = {'form': form}
        return render(request, 'teams/create.html', data)

    # return render(request, 'teams/create.html', {})