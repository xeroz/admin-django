from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from apps.teams.forms import TeamForm, StadiumForm
from apps.teams.models import Team, Stadium
from apps.players.models import Player

# Create your views here.
class ListTeams(ListView):
    model = Team
    template_name = 'teams/index.html'

class CreateTeam(CreateView):
    model = Team
    form_class = TeamForm
    template_name = 'teams/create.html'
    success_url = reverse_lazy('teams:list')

    def get_context_data(self, **kwargs):
        context = super(CreateTeam, self).get_context_data(**kwargs)
        form_stadium = StadiumForm
        context['form_stadium'] = form_stadium
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        form_stadium = StadiumForm(request.POST, request.FILES)
        if form.is_valid() and form_stadium.is_valid():
            return self.form_valid(form, form_stadium)
        else:
            return self.form_invalid(form, form_stadium)

    def form_valid(self, form, form_stadium):
        self.team = form.save()
        form_stadium.instance.team = self.team
        form_stadium.save()
        return super(CreateTeam, self).form_valid(form)

    def form_invalid(self, form, form_stadium):
        return self.render_to_response(self.get_context_data(form=form))


class EditTeam(UpdateView):
    modal = Team
    form_class = TeamForm
    template_name = 'teams/edit.html'
    success_url = reverse_lazy('teams:list')
    queryset = Team.objects.all()

    def get_context_data(self, **kwargs):
        context = super(EditTeam, self).get_context_data(**kwargs)
        stadium = self.get_object().team_stadium
        form_stadium = StadiumForm(instance = stadium, prefix='stadium')
        context['form_stadium'] = form_stadium
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(request.POST, instance=self.object)
        stadium = self.get_object().team_stadium
        form_stadium = StadiumForm(request.POST, request.FILES, instance=stadium, prefix='stadium')
        if form.is_valid() and form_stadium.is_valid():
            return self.form_valid(form, form_stadium)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, form_stadium):
        self.object = form.save()
        form_stadium.save()
        return HttpResponseRedirect(self.get_success_url())


class DeleteTeam(DeleteView):
    modal = Team
    success_url = reverse_lazy('teams:list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


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

def stadium(request, id):
    stadium = Stadium.objects.get(team__pk = id)

    if request.method == 'GET':
        data = {
            'stadium': stadium,
        }
        return render(request, 'teams/stadium.html', data)