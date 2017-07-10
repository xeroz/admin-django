from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from django.core.urlresolvers import reverse_lazy
from apps.teams.forms import TeamForm, StadiumForm
from apps.teams.models import Team, Stadium
from apps.players.models import Player
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.
class IndexView(ListView):
    model = Team
    template_name = 'teams/index.html'

class CreateView(CreateView):
    model = Team
    form_class = TeamForm
    template_name = 'teams/create.html'
    success_url = reverse_lazy('teams:index')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['form_stadium'] = form_stadium
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form_stadium = StadiumForm(request.POST, request.FILES)
        if form.is_valid() and form_stadium.is_valid():
            return self.form_valid(form, form_stadium)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, form_stadium):
        self.team = form.save()
        form_stadium.instance.team = self.team
        form_stadium.save()
        return super(CreateView, self).form_valid(form)

class EditView(UpdateView):
    modal = Team
    form_class = TeamForm
    template_name = 'teams/edit.html'
    success_url = reverse_lazy('teams:index')
    queryset = Team.objects.all()

    def get_context_data(self, **kwargs):
        context = super(EditView, self).get_context_data(**kwargs)
        stadium = self.get_object().team_stadium
        form_stadium = StadiumForm(instance = stadium)
        context['form_stadium'] = form_stadium
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        stadium = self.get_object().team_stadium
        form_stadium = StadiumForm(request.POST, request.FILES, instance=stadium)
        if form.is_valid() and form_stadium.is_valid():
            return self.form_valid(form, form_stadium)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, form_stadium):
        self.team = form.save()
        form_stadium.instance.team = self.team
        form_stadium.save()
        return super(EditView, self).form_valid(form)

class DeleteView(DeleteView):
    modal = Team
    success_url = reverse_lazy('teams:index')
    queryset = Team.objects.all()

def players(request, id):

    players = Player.objects.filter(team = id)
    team    = get_object_or_404(Team, id = id)

    if request.method == 'GET':
        data = {
            'players': players,
            'team': team,
        }
        return render(request, 'teams/players.html', data)

def stadium(request, id):
    stadium = get_object_or_404(Stadium, id = id)

    if request.method == 'GET':
        data = {
            'stadium': stadium,
        }
        return render(request, 'teams/stadium.html', data)