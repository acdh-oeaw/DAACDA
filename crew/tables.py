import django_tables2 as tables
from django_tables2.utils import A
from .models import Person


class PersonTable(tables.Table):
    last_name = tables.LinkColumn('crew:person_detail', args=[A('pk')])
    bomber = tables.LinkColumn('bombers:bomber_detail', args=[A('bomber.id')])

    class Meta:
        model = Person
        fields = ("last_name", "first_name", "bomber", "destiny_checked")
        attrs = {"class": "table table-boarderd table-hover"}
