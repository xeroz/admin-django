from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from apps.players.forms import PlayerForm
from apps.players.models import Player
from django.views.generic import ListView

# Create your views here.
def index(request):

    players = Player.objects.all()

    data = {
        'players': players,
    }
    return render(request, 'players/index.html', data)

class IndexView(ListView):
    model = Player
    template_name = 'players/index.html'

def create(request):

    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/players/index')
    else:
        form = PlayerForm()
        data = {'form': form}
        return render(request, 'players/create.html', data)

def edit(request, id):

    player = get_object_or_404(Player, id = id)

    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES, instance = player)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/players/index')
    else:
        form = PlayerForm(instance = player)
        data = {'form': form}
        return render(request, 'players/edit.html', data)

def delete(render, id):

    player = get_object_or_404(Player, id = id)
    player.delete()

    return HttpResponseRedirect('/players/index')