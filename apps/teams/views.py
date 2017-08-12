from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    View
)
from django.core.urlresolvers import reverse_lazy
from django.core import serializers
from django.http import HttpResponse
from apps.teams.forms import TeamForm, StadiumForm
from apps.teams.models import Team, Stadium
from apps.players.models import Player, Statistics


from django.template.loader import get_template
from django.template import Context
import pdfkit

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
        print(form)
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
        form_stadium = StadiumForm(
            instance=stadium,
            prefix='stadium'
        )
        context['form_stadium'] = form_stadium
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(
            request.POST,
            request.FILES,
            instance=self.object
        )
        stadium = self.get_object().team_stadium
        form_stadium = StadiumForm(
            request.POST,
            request.FILES,
            instance=stadium,
            prefix='stadium'
        )
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


class ListPlayersByTeam(View):
    template_name = 'teams/players.html'

    def get(self, request, pk):
        players = Player.objects.filter(team__pk=pk)
        team = get_object_or_404(Team, id=pk)
        data = {
            'players': players,
            'team': team,
        }
        return render(request, self.template_name, data)


class ListStadiumByTeam(View):
    template_name = 'teams/stadium.html'
    model = Stadium

    def get(self, request, pk):
        stadium = Stadium.objects.get(team__pk=pk)
        data = {
            'stadium': stadium,
        }
        return render(request, self.template_name, data)


def get_players_by_country(request):
    country = request.GET.get('country')
    team_id = request.GET.get('team_id')
    players = Player.objects.filter(country=country, team=team_id)
    json_players = serializers.serialize('json', players)
    return HttpResponse(json_players, content_type="application/json")



def get_detail_player(request):
    player_id = request.GET.get('player_id')
    statistic = Statistics.objects.get(player__pk=player_id)
    json_statistic = serializers.serialize("json", [statistic])
    # query = Statistics.objects.get(player__pk=player_id)
    # .select_related('player')

    # print('sdd', query)
    # print(serializers.serialize("json", [player.statistic, player]))

    return HttpResponse(serializers.serialize("json", [statistic]), content_type="application/json")


def report_player(request):
    pass
