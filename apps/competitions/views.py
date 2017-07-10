from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from apps.competitions.models import Competition
from apps.competitions.forms import CompetitionForm
from django.views.generic import ListView

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

class IndexView(ListView):
    model = Competition
    template_name = 'competitions/index.html'
        