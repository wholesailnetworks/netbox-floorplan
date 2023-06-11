from django.db import models
from django.urls import reverse

from netbox.models import NetBoxModel
from .utils import file_upload


class Floorplan(NetBoxModel):
    site = models.ForeignKey(
        to='dcim.Site',
        on_delete=models.PROTECT
    )
    location = models.ForeignKey(
        to='dcim.Location',
        blank=True,
        null=True,
        on_delete=models.PROTECT
    )
    background_image = models.ImageField(
        upload_to=file_upload,
        blank=True,
        null=True
    )
    scale = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    measurement_choices = [
        ('ft', 'Feet'),
        ('m', 'Meters')
    ]
    measurement_unit = models.CharField(
        max_length=2,
        choices=measurement_choices,
        default='m'
    )
    
    canvas = models.JSONField(default=dict)

    class Meta:
        ordering = ('site', 'location', 'background_image', 'scale', 'measurement_unit')

    def get_absolute_url(self):
        return reverse('plugins:netbox_floorplan:floorplan', args=[self.pk])


class FloorplanObject(NetBoxModel):
    rack = models.ForeignKey(
        to='dcim.Rack',
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    location = models.ForeignKey(
        to='dcim.Location',
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    floorplan = models.ForeignKey(
        to='Floorplan',
        on_delete=models.PROTECT
    )
    x_coordinate = models.DecimalField(
        max_digits=100,
        decimal_places=50
    )
    y_coordinate = models.DecimalField(
        max_digits=100,
        decimal_places=50
    )
    rotation = models.IntegerField(
        default=0
    )

    class Meta:
        ordering = ('floorplan', 'rack', 'location',
                    'x_coordinate', 'y_coordinate', 'rotation')

    def get_absolute_url(self):
        return reverse('plugins:netbox_floorplan:floorplanobject', args=[self.pk])
