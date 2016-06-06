import django_tables2 as tables
from django_tables2.utils import A
from bomber.models import Bomber
from crew.models import Person


class BomberTable(tables.Table):
    macr_nr = tables.LinkColumn('bombers:bomber_detail', args=[A('pk')])
    crash_place = tables.LinkColumn('places:place_edit', args=[A('crash_place.id')])

    class Meta:
        model = Bomber
        fields = ("macr_nr", "date_of_crash", "crash_place")
        attrs = {"class": "table table-boarderd table-hover"}


class PersonTable(tables.Table):
    last_name = tables.LinkColumn('crew:person_detail', args=[A('pk')])
    bomber = tables.LinkColumn('bombers:bomber_detail', args=[A('bomber.id')])

    class Meta:
        model = Person
        fields = ("last_name", "first_name", "bomber", "destiny_checked")
        attrs = {"class": "table table-boarderd table-hover"}
