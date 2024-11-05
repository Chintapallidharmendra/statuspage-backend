from rest_framework import viewsets, permissions

from .models import Page, Component, Incident, SystemMetric
from .serializers import PageSerializer, ComponentSerializer, IncidentSerializer, SystemMetricSerializer

class PageViewset(viewsets.ModelViewSet):

    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Page.objects.filter(account__owner=user)

class ComponentViewset(viewsets.ModelViewSet):

    queryset = Component.objects.all()
    serializer_class = ComponentSerializer

class IncidentViewset(viewsets.ModelViewSet):

    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    permission_classes = [permissions.IsAuthenticated]

class SystemMetricViewset(viewsets.ModelViewSet):

    queryset = SystemMetric.objects.all()
    serializer_class = SystemMetricSerializer
    permission_classes = [permissions.IsAuthenticated]