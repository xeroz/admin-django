
from django.shortcuts import HttpResponseRedirect, render, HttpResponse
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.core.urlresolvers import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from apps.players.forms import PlayerForm, StatisticForm
from apps.players.models import Player

from django.template.loader import get_template
from django.template import Context
import pdfkit

# Create your views here.


class ListPlayer(ListView):
    model = Player
    template_name = 'players/index.html'


class CreatePlayer(CreateView):
    model = Player
    form_class = PlayerForm
    template_name = 'players/create.html'
    success_url = reverse_lazy('players:list')

    def get_context_data(self, **kwargs):
        context = super(CreatePlayer, self).get_context_data(**kwargs)
        form_statistic = StatisticForm
        context['form_statistic'] = form_statistic
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form_statistic = StatisticForm(request.POST)
        if form.is_valid() and form_statistic.is_valid():
            return self.form_valid(form, form_statistic)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, form_statistic):
        self.player = form.save()
        form_statistic.instance.player = self.player
        form_statistic.save()
        return super(CreatePlayer, self).form_valid(form)


class EditPlayer(UpdateView):
    model = Player
    form_class = PlayerForm
    template_name = 'players/edit.html'
    success_url = reverse_lazy('players:list')

    def get_context_data(self, **kwargs):
        context = super(EditPlayer, self).get_context_data(**kwargs)
        try:
            statistic = self.get_object().statistic
            form_statistic = StatisticForm(instance=statistic)
        except ObjectDoesNotExist:
            form_statistic = StatisticForm()
        context['form_statistic'] = form_statistic
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(self.object)
        form = self.form_class(
            request.POST,
            request.FILES,
            instance=self.object
        )
        print(form)
        statistic = self.get_object().statistic
        form_statistic = StatisticForm(request.POST, instance=statistic)
        if form.is_valid() and form_statistic.is_valid():
            return self.form_valid(form, form_statistic)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, form_statistic):
        self.object = form.save()
        form_statistic.save()
        return HttpResponseRedirect(self.get_success_url())


class DeletePlayer(DeleteView):
    model = Player
    success_url = reverse_lazy('players:list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


def report_player(request, pk):
    print('fdkjhjfhdlkl')
    host = request.get_host()
    print(host)
    template = get_template('reports/players/by_player.html')
    print('fdkjfn', template)
    html = template.render()
    print('fdkjfnwwwwwwwwww', html)

    pdf = pdfkit.from_string(html, 'fvl.pdf')
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ourcodeworld.pdf"'

    return response  # returns the response.

def test_report(request):

    return render(request, 'reports/players/by_player.html', {})

def send_email(request):
    pass
