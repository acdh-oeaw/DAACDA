from django.shortcuts import render
from django_tables2 import RequestConfig
from django.views.generic.detail import DetailView
from django.db.models import Count

from .models import Person
from .tables import PersonTable


def person(request):
    table = PersonTable(Person.objects.all())
    RequestConfig(request).configure(table)
    destiny = Person.objects.values('destiny_checked').annotate(total=Count('destiny_checked')).order_by('destiny_checked')
    person_nr = len(Person.objects.all())
    return render(request, 'crew/list_person.html',
        {'table': table, 'destiny': destiny, 'person_nr': person_nr})


class PersonDetailView(DetailView):
    model = Person

    def get_context_data(self, **kwargs):
        context = super(PersonDetailView, self).get_context_data(**kwargs)
        return context
