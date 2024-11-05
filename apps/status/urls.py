from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import PageViewset, ComponentViewset, IncidentViewset, SystemMetricViewset

router = DefaultRouter()
router.register(r'pages', PageViewset)
router.register(r'components', ComponentViewset)
router.register(r'incidents', IncidentViewset)
router.register(r'system-metrics', SystemMetricViewset)

urlpatterns  = [
    path('', include(router.urls)),
]