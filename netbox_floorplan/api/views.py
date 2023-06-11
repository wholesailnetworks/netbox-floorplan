from netbox.api.viewsets import NetBoxModelViewSet

from .. import filtersets, models
from .serializers import FloorplanSerializer, FloorplanObjectSerializer

class FloorplanViewSet(NetBoxModelViewSet):
    queryset = models.Floorplan.objects.all()
    serializer_class = FloorplanSerializer
    filterset_class = filtersets.FloorplanFilterSet
    # search_fields = ['^name', 'slug']
    # bulk_update_fields = ['site', 'location', 'background_image', 'scale']

class FloorplanObjectViewSet(NetBoxModelViewSet):
    queryset = models.FloorplanObject.objects.all()
    serializer_class = FloorplanObjectSerializer
    # filterset_class = filtersets.FloorplanObjectFilterSet
    # search_fields = ['^name', 'slug']
    # bulk_update_fields = ['rack', 'location', 'floorplan', 'x_coordinate', 'y_coordinate']