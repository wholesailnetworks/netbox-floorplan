from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseNotFound
from django.views import View
from django.shortcuts import render


class TestView(LoginRequiredMixin, View):

    def get(self, request):
        # render_type = request.GET.get('render', None)

        return render(request, "netbox_location_map/t.html")
