from django.db.models import Count
from netbox.views import generic
from . import filtersets, forms, models, tables

# class TestView(LoginRequiredMixin, View):

#     def get(self, request):
#         # render_type = request.GET.get('render', None)

#         return render(request, "netbox_floorplan/t.html")
    
class FloorplanView(generic.ObjectView):
    queryset = models.Floorplan.objects.all()

class FloorplanListView(generic.ObjectListView):
    queryset = models.Floorplan.objects.all()
    table = tables.FloorplanTable
    
class FloorplanEditView(generic.ObjectEditView):
    queryset = models.Floorplan.objects.all()
    form = forms.FloorplanForm

class FloorplanDeleteView(generic.ObjectDeleteView):
    queryset = models.Floorplan.objects.all()