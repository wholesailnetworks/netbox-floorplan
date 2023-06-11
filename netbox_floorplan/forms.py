from netbox.forms import NetBoxModelForm
from .models import Floorplan, FloorplanObject
from dcim.models import Rack

class FloorplanForm(NetBoxModelForm):
        class Meta:
            model = Floorplan
            fields = ['site', 'location', 'background_image', 'scale']

class FloorplanRackFilterForm(NetBoxModelForm):
      class Meta:
            model = Rack
            fields = ['site', 'location', 'background_image', 'scale', 'measurement_unit']

