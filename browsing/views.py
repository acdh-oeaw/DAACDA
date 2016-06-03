from django_tables2 import SingleTableView, RequestConfig
from bomber.models import Bomber
from places.models import *
from .filters import BomberListFilter
from .forms import GenericFilterFormHelper
from .tables import BomberTable


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


class BomberListView(GenericListView):
    model = Bomber
    table_class = BomberTable
    template_name = 'browsing/bomber_list_generic.html'
    filter_class = BomberListFilter
    formhelper_class = GenericFilterFormHelper

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        # edition_names = []
        # for edition in Bomber.objects.all():
        #     edition_names.append(edition.name)
        # context["edition_names"] = set(edition_names)
        # manager_names = []
        # for person in Person.objects.all():
        #     manager_names.append(person.name)
        # context["manager_names"] = set(manager_names)
        # institution_names = []
        # for inst in Institution.objects.all():
        #     institution_names.append(inst.name)
        # context["institution_names"] = set(institution_names)
        return context
