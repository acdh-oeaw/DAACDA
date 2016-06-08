import django_tables2 as tables
from django_tables2.utils import A
from .models import Bomber


class BomberTable(tables.Table):
    macr_nr = tables.LinkColumn('bombers:bomber_detail', args=[A('pk')])
    crash_place = tables.LinkColumn(
        'places:place_edit', args=[A('crash_place.id')], order_by="crash_place.name")

    class Meta:
        model = Bomber
        fields = ("macr_nr", "date_of_crash", "crash_place")
        attrs = {"class": "table table-boarderd table-hover"}
