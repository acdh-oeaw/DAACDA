from django_tables2 import SingleTableView, RequestConfig
from bomber.models import Bomber
from crew.models import Person
from places.models import Place
from .filters import BomberListFilter, PersonListFilter
from .forms import GenericFilterFormHelper
from bomber.tables import BomberTable
from crew.tables import PersonTable


def get_autocompomplete_places(ClassName, field_name):
    """ helper function to return name values of Place objects """
    return_list = []
    for x in ClassName.objects.values(field_name):
            place = Place.objects.get(id=x[field_name])
            return_list.append(place.name)
    return list(set(return_list))


class GenericListView(SingleTableView):
    filter_class = None
    formhelper_class = None
    context_filter_name = 'filter'
    paginate_by = 25

    def get_queryset(self, **kwargs):
        qs = super(GenericListView, self).get_queryset()
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        self.filter.form.helper = self.formhelper_class()
        return self.filter.qs

    def get_table(self, **kwargs):
        table = super(GenericListView, self).get_table()
        RequestConfig(self.request, paginate={
            'page': 1, 'per_page': self.paginate_by}).configure(table)
        return table

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        return context


class PersonListView(GenericListView):
    model = Person
    table_class = PersonTable
    template_name = 'browsing/person_list_generic.html'
    filter_class = PersonListFilter
    formhelper_class = GenericFilterFormHelper

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        return context


class BomberListView(GenericListView):
    model = Bomber
    table_class = BomberTable
    template_name = 'browsing/bomber_list_generic.html'
    filter_class = BomberListFilter
    formhelper_class = GenericFilterFormHelper

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        qs = super(GenericListView, self).get_queryset()
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        self.filter.form.helper = self.formhelper_class()
        crash_places = []
        for x in self.filter.qs.values('crash_place'):
            place = Place.objects.get(id=x['crash_place'])
            crash_places.append(place.name)
        context['crash_places'] = list(set(crash_places))
        target_places = []
        for x in self.filter.qs.values('target_place'):
            place = Place.objects.get(id=x['target_place'])
            target_places.append(place.name)
        context['target_places'] = list(set(target_places))
        return context
