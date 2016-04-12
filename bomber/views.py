from django.shortcuts import render
from django_tables2 import RequestConfig
from django.views.generic.detail import DetailView
from django.db.models import Count

from crew.models import Person
from .models import Bomber
from .tables import BomberTable


def bomber(request):
    table = BomberTable(Bomber.objects.all())
    RequestConfig(request).configure(table)
    object_list = Bomber.objects.all()
    return render(request, 'bomber/list_bomber.html', {'table': table, 'object_list': object_list})


class BomberDetailView(DetailView):
    model = Bomber

    def get_context_data(self, **kwargs):
        context = super(BomberDetailView, self).get_context_data(**kwargs)
        current_object = self.object
        context['destiny'] = Person.objects.filter(bomber=current_object.id).values('destiny_checked').annotate(total=Count('destiny_checked')).order_by('destiny_checked')
        context['crew_list'] = Person.objects.filter(bomber=current_object.id).order_by('destiny_checked')
        return context
