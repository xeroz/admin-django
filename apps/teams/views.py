from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views import View
from django.core import serializers
from django.http import HttpResponse
import json
from apps.teams.forms import TeamForm, StadiumForm
from apps.teams.models import Team, Stadium
from apps.players.models import Player


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
        form_stadium = StadiumForm
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

class DeleteView(DeleteView):
    modal = Team
    success_url = reverse_lazy('teams:index')
    queryset = Team.objects.all()

class Players(View):
    template_name = 'teams/players.html'

    def get(self, request, pk):
        players = Player.objects.filter(team__pk = pk)
        team    = get_object_or_404(Team, id = pk)        
        print(players)
        data = {
            'players': players,
            'team': team,
        }

        return render(request, self.template_name, data)

class Stadiu(View):
    template_name = 'teams/stadium.html'
    model = Stadium

    def get(self, request, pk):    
        stadium = Stadium.objects.get(team__pk = pk)
        print(stadium)

        data = {
            'stadium': stadium,
        }
        return render(request, self.template_name, data)

def fbview(request):
    return HttpResponse(serializers.serialize('json', Stadium.objects.all()), content_type="application/json")

def get_players_by_country(request):
    country = request.GET.get('country')
    team_id = request.GET.get('team_id')

    players = Player.objects.filter(country=country).filter(team=team_id)

    return HttpResponse(serializers.serialize('json', players), content_type="application/json")