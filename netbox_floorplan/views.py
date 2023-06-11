from django.db.models import Count
from netbox.views import generic
from . import filtersets, forms, models, tables
from dcim.models import Site, Rack
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseNotFound
from django.views import View
from django.shortcuts import render

import json

from utilities.views import ViewTab, register_model_view
from dcim.models import Site

class TestView(LoginRequiredMixin, View):

    def get(self, request):
        # render_type = request.GET.get('render', None)

        return render(request, "netbox_floorplan/t.html")
    
@register_model_view(Site,name='floorplans',path='test')
class FloorplanView(LoginRequiredMixin, View):
    #queryset = models.Floorplan.objects.all()
    tab = ViewTab(
        label='Floor Plan',
    )
    def get(self, request,pk):
        return render(request, "netbox_floorplan/t.html")
class FloorplanListView(generic.ObjectListView):
    queryset = models.Floorplan.objects.all()
    table = tables.FloorplanTable
    
class FloorplanEditView(generic.ObjectEditView):
    queryset = models.Floorplan.objects.all()
    form = forms.FloorplanForm

class FloorplanDeleteView(generic.ObjectDeleteView):
    queryset = models.Floorplan.objects.all()


class FloorplanMapEditView(LoginRequiredMixin, View):
    def get(self, request, pk):
        site = Site.objects.get(id=pk)
        racklist = Rack.objects.filter(site=site)
        objectlist = models.Floorplan.objects.get(site=site.id)
        # existingracks = []
        # canvas = json.loads(objectlist.canvas)
        # for object in canvas:
        #     existingracks.append(object.id)
        form = forms.FloorplanRackFilterForm
        return render(request, "netbox_floorplan/floorplan_edit.html", {"form": form, "site": site, "racklist": racklist})
