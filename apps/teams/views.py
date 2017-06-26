from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from apps.teams.forms import TeamForm
from apps.teams.models import Team
from apps.players.models import Player

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
            return HttpResponseRedirect('/teams/index')
    else:
        form = TeamForm()
        data = {'form': form}
        return render(request, 'teams/create.html', data)

def edit(request, id):

    team = get_object_or_404(Team, id = id)

    if request.method == 'POST':
        form = TeamForm(request.POST, instance = team)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teams/index')
    else:
        form = TeamForm(instance = team)
        data = {'form': form}
        return render(request, 'teams/edit.html', data)

def delete(render, id):
    team = get_object_or_404(Team, id = id)
    team.delete()

    return HttpResponseRedirect('/teams/index')

def players(request, id):

    players = Player.objects.filter(team = id)
    team    = get_object_or_404(Team, id = id)

    if request.method == 'GET':
        data = {
            'players': players,
            'team': team,
            }
        return render(request, 'teams/players.html', data)