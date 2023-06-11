from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_floorplan'

router = NetBoxRouter()
router.register('floorplans', views.FloorplanViewSet)
router.register('floorplan-objects', views.FloorplanObjectViewSet)

urlpatterns = router.urls