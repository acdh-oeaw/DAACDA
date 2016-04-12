import django_tables2 as tables
from django_tables2.utils import A
from .models import Bomber


class BomberTable(tables.Table):
    macr_nr = tables.LinkColumn('bombers:bomber_detail', args=[A('pk')])
    crash_place = tables.LinkColumn('places:place_edit', args=[A('crash_place.id')])
# unit = tables.TemplateColumn('{{ record.bomber_group }} | {{ record.squadron }}')

    class Meta:
        model = Bomber
        fields = ("macr_nr", "date_of_crash", "crash_place")
#        exclude = ("comment", "lat", "lng", "last_seen", "target_place", "id", "name", "plane_id",)
        attrs = {"class": "table table-boarderd table-hover"}
