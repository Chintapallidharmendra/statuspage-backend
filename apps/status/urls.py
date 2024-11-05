from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import PageViewset, ComponentViewset, IncidentViewset, SystemMetricViewset, SubscriberViewset

router = DefaultRouter()
router.register(r'pages', PageViewset)
router.register(r'components', ComponentViewset)
router.register(r'incidents', IncidentViewset)
router.register(r'system-metrics', SystemMetricViewset)
router.register(r'subscribers', SubscriberViewset)


urlpatterns  = [
    path('', include(router.urls)),
]