from netbox.forms import NetBoxModelForm
from .models import Floorplan, FloorplanObject

class FloorplanForm(NetBoxModelForm):
        class Meta:
            model = Floorplan
            fields = ['site', 'location', 'background_image', 'scale']
