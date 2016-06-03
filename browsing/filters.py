import django_filters

from bomber.models import Bomber

django_filters.filters.LOOKUP_TYPES = [
    ('icontains', 'Contains (case insensitive)'),
]


class BomberListFilter(django_filters.FilterSet):
    class Meta:
        model = Bomber
