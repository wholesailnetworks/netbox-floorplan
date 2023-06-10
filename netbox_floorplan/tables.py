import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import Floorplan, FloorplanObject

class FloorplanTable(NetBoxTable):
    class Meta(NetBoxTable.Meta):
        model = Floorplan
        fields = ('pk', 'site', 'location', 'background_image', 'scale')
        default_columns = ('pk', 'site', 'location', 'background_image', 'scale')