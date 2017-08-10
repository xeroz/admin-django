from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from apps.competitions.models import Competition
from apps.competitions.forms import CompetitionForm

# Create your views here.


def index(request):
    competitions = Competition.objects.all()

    data = {
        'competitions': competitions,
    }
    return render(request, 'competitions/index.html', data)


def create(request):
    if request.method == 'POST':
        form = CompetitionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/competitions/index')
    else:
        form = CompetitionForm()
        data = {'form': form}
        return render(request, 'competitions/create.html', data)


def teams(request, id):
    return render(request, 'competitions/teams.html', {})


def edit(request, id):
    competition = get_object_or_404(Competition, id=id)

    if request.method == 'POST':
        form = CompetitionForm(
            request.POST,
            request.FILES,
            instance=competition
        )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/competitions/index')
    else:
        form = CompetitionForm(instance=competition)
        data = {'form': form}
        return render(request, 'competitions/edit.html', data)
