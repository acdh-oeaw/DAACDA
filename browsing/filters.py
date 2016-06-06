import django_filters

from bomber.models import Bomber
from crew.models import Person


django_filters.filters.LOOKUP_TYPES = [
    ('', '---------'),
    ('exact', 'Is equal to'),
    ('not_exact', 'Is not equal to'),
    ('lt', 'Lesser than'),
    ('gt', 'Greater than'),
    ('gte', 'Greater than or equal to'),
    ('lte', 'Lesser than or equal to'),
    ('startswith', 'Starts with'),
    ('endswith', 'Ends with'),
    ('contains', 'Contains'),
    ('not_contains', 'Does not contain'),
]


def generated_choices(ClassName, field_name):
    """returns the values of the field in a list of tuples"""
    return_choices = []
    picked_valued = ClassName.objects.values(field_name)
    for x in picked_valued:
        return_choices.append((x[field_name], x[field_name]))
    return list(set(return_choices))


class PersonListFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(
        lookup_expr='icontains', label="Person's first name")
    last_name = django_filters.CharFilter(
        lookup_expr='icontains', label="Person's last name")
    rank = django_filters.MultipleChoiceFilter(
        choices=generated_choices(Person, 'rank'))
    position = django_filters.MultipleChoiceFilter(
        choices=generated_choices(Person, 'position'), label="Position in the Aircraft")
    destiny_stated = django_filters.MultipleChoiceFilter(
        choices=generated_choices(Person, 'destiny_stated'))
    destiny_checked = django_filters.MultipleChoiceFilter(
        choices=generated_choices(Person, 'destiny_checked'))
    mia = django_filters.ChoiceFilter(
        choices=generated_choices(Person, 'mia'))
    comment = django_filters.CharFilter(
        lookup_expr='icontains', label="Look for a word/phrase in the comment field")

    class Meta:
        model = Person
        fields = []


class BomberListFilter(django_filters.FilterSet):
    air_force = django_filters.MultipleChoiceFilter(
        choices=generated_choices(Bomber, 'air_force'))
    plane_type = django_filters.MultipleChoiceFilter(
        choices=generated_choices(Bomber, 'plane_type'))
    crash_place__name = django_filters.CharFilter(
        lookup_expr='icontains', label="Place of the crash")
    target_place__name = django_filters.CharFilter(
        lookup_expr='icontains', label="The target of the attack")
    date_of_crash = django_filters.DateFromToRangeFilter(
        help_text="You have to provide a full date in the format 'YYYY-MM-DD'.")
    reason_of_crash = django_filters.MultipleChoiceFilter(choices=generated_choices(
        Bomber, 'reason_of_crash'))
    last_name = django_filters.MethodFilter(
        action='last_name_filter', label="(Part of) Any crew members last name")
    comment = django_filters.MethodFilter(
        action='first_name_filter', label="(Part of) Any crew members first name")

    def last_name_filter(self, queryset, value):
        return queryset.filter(person__last_name__icontains=value).distinct()

    def first_name_filter(self, queryset, value):
        return queryset.filter(person__first_name__icontains=value).distinct()

    class Meta:
        model = Bomber
        fields = []
