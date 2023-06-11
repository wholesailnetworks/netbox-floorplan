from rest_framework import serializers
from dcim.api.serializers import NestedRackSerializer, NestedSiteSerializer
from netbox.api.serializers import NetBoxModelSerializer
from ..models import Floorplan, FloorplanObject

class FloorplanSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='plugins-api:netbox_floorplan-api:floorplan-detail')
    site = NestedSiteSerializer()
    class Meta:
        model = Floorplan
        fields = ['id', 'url', 'site', 'location', 'background_image', 'scale', 'tags', 'custom_fields', 'created', 'last_updated']

class FloorplanObjectSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='plugins-api:netbox_floorplan-api:floorplanobject-detail')
    rack = NestedRackSerializer()
    class Meta:
        model = FloorplanObject
        fields = [ 'id', 'url', 'rack', 'location', 'floorplan', 'x_coordinate', 'y_coordinate', 'tags', 'custom_fields', 'created', 'last_updated']